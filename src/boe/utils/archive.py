from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class ArchiveError(RuntimeError):
    pass


def extract_archive(
    archive: Path,
    destination: Path,
    seven_zip: Path,
) -> None:
    """
    Extract an archive using 7-Zip.
    """

    if not archive.exists():
        raise ArchiveError(f"Firmware not found:\n{archive}")

    if not seven_zip.exists():
        raise ArchiveError(f"7-Zip not found:\n{seven_zip}")

    if destination.exists():
        shutil.rmtree(destination)

    destination.mkdir(parents=True)

    cmd = [
        str(seven_zip),
        "x",
        str(archive),
        f"-o{destination}",
        "-y",
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise ArchiveError(result.stderr)

    if not any(destination.iterdir()):
        raise ArchiveError("Extraction produced no files.")
