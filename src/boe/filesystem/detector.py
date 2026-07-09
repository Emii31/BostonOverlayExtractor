from pathlib import Path

EXT4_MAGIC_OFFSET = 0x438
EXT4_MAGIC = b"\x53\xEF"

EROFS_MAGIC = b"EROFS"


def detect(image: Path) -> str:
    with image.open("rb") as f:
        # EXT4 magic
        f.seek(EXT4_MAGIC_OFFSET)
        if f.read(2) == EXT4_MAGIC:
            return "ext4"

        # EROFS magic
        f.seek(1024)
        if f.read(5) == EROFS_MAGIC:
            return "erofs"

    return "unknown"
