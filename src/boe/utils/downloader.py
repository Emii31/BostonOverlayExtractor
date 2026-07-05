import urllib.request
from pathlib import Path


def download(url: str, dest: str) -> None:
    path = Path(dest)
    path.parent.mkdir(parents=True, exist_ok=True)

    print(f"[DOWNLOAD] {url}")

    urllib.request.urlretrieve(url, path)

    print(f"[OK] Saved to {dest}")
