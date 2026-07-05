from pathlib import Path
import zipfile


def extract_zip(file: Path, out: Path):
    out.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(file, "r") as z:
        z.extractall(out)


def is_zip(file: Path) -> bool:
    return file.suffix.lower() == ".zip"
