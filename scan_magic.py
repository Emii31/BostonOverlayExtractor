from pathlib import Path

path = Path("workspace/merged/super.img")

chunk_size = 1024 * 1024
offset = 0

with path.open("rb") as f:
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            print("LPG0 not found")
            break

        pos = chunk.find(b"LPG0")
        if pos != -1:
            print("Found at", offset + pos)
            break

        offset += len(chunk)
