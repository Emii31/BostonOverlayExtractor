from __future__ import annotations

from pathlib import Path
import shutil

from boe.utils.sparse import convert_sparse_to_raw


WORKSPACE = Path("workspace/extracted")
MERGED = Path("workspace/merged")
SPARSE_OUTPUT = MERGED / "super_sparse.img"
RAW_OUTPUT = MERGED / "super.img"


def run_merge():
    print("[1/5] Preparing merge workspace...")

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

    print(f"[2/5] Found {len(chunks)} chunks")

    # Create file list for 7z concatenation
    list_file = MERGED / "chunks.txt"

    with list_file.open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(str(c) + "\n")

    print("[3/5] Merging chunks...")

    # Windows-safe binary merge using Process abstraction
    with SPARSE_OUTPUT.open("wb") as out:
      for chunk in chunks:
            with chunk.open("rb") as inp:
                shutil.copyfileobj(inp, out)

    print("[4/5] Sparse merge complete")

    print("[5/5] Converting sparse → raw")

    convert_sparse_to_raw(
    SPARSE_OUTPUT,
    RAW_OUTPUT
)

print("[OK] Raw super.img created")
