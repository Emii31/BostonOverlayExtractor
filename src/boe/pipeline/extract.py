from pathlib import Path
import shutil

from boe.utils.archive import extract_zip, is_zip


WORKSPACE = Path("workspace/extracted")


def run_extract(firmware: Path):

    print("\n[BOE] Extract Engine Starting...\n")

    if WORKSPACE.exists():
        shutil.rmtree(WORKSPACE)

    WORKSPACE.mkdir(parents=True, exist_ok=True)

    if is_zip(firmware):
        print("[+] ZIP detected")
        extract_zip(firmware, WORKSPACE)

    else:
        print("[!] Unsupported format")
        return

    files = list(WORKSPACE.rglob("*"))

    print(f"\n[OK] Extracted files: {len(files)}")

    for f in files[:20]:
        print(" -", f.name)

    print("\n[BOE] Extraction complete.\n")
