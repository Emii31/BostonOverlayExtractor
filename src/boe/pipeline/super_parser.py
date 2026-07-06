from pathlib import Path
import struct
import shutil

MAGIC = b"LP"


def find_lp_metadata(img_path: Path):
    """
    Stream scan instead of loading full 7GB into RAM.
    """
    MAGIC = b"LP"

    with img_path.open("rb") as f:
        offset = 0

        while True:
            chunk = f.read(1024 * 1024)  # 1MB chunks
            if not chunk:
                break

            pos = chunk.find(MAGIC)
            if pos != -1:
                return offset + pos

            offset += len(chunk)

    return None


def run_super_parse(super_img: Path, out_dir: Path):
    print("[BOE] Scanning super.img metadata...")

    offset = find_lp_metadata(super_img)

    if offset is None:
        print("[WARN] No LP metadata found. Falling back raw mode.")
        return False

    print(f"[OK] LP metadata found at offset: {offset}")

    print("[BOE] Creating partition workspace...")

    partitions = [
        "system",
        "vendor",
        "product",
        "system_ext",
        "odm"
    ]

    for p in partitions:
        (out_dir / p).mkdir(parents=True, exist_ok=True)

    print("[BOE] Partition structure initialized")
    return True
