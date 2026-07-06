from __future__ import annotations

import shutil
from pathlib import Path

from boe.core.process import Process


WORKSPACE = Path("workspace/extracted")
MERGED = Path("workspace/merged")
OUTPUT = MERGED / "super.img"


def run_merge():
    print("[1/4] Preparing merge workspace...")

    if MERGED.exists():
        shutil.rmtree(MERGED)

    MERGED.mkdir(parents=True, exist_ok=True)

    chunks = sorted(
        WORKSPACE.glob("super.img_sparsechunk.*"),
        key=lambda x: int(x.name.split(".")[-1])
    )

    if not chunks:
        print("[ERROR] No sparsechunks found")
        return

    print(f"[2/4] Found {len(chunks)} chunks")

    # Create file list for 7z concatenation
    list_file = MERGED / "chunks.txt"

    with list_file.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(str(c) + "\n")

    print("[3/4] Merging chunks...")

    # Windows-safe binary merge using Process abstraction
    with OUTPUT.open("wb") as out:
        for chunk in chunks:
            with chunk.open("rb") as inp:
                shutil.copyfileobj(inp, out)

    print("[4/4] super.img created")

    print("\n========== MERGE COMPLETE ==========")
    print(f"Output: {OUTPUT}")
    print("====================================\n")
