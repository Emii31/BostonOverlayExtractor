import platform
import subprocess
from pathlib import Path


class SparseError(Exception):
    pass


def convert_sparse_to_raw(
    sparse: Path,
    raw: Path
):

    if platform.system() == "Windows":

        print("[BOE] Using WSL simg2img backend")

        cmd = [
            "wsl",
            "simg2img",
            linux_path(sparse),
            linux_path(raw)
        ]

    else:

        print("[BOE] Using native simg2img")

        cmd = [
            "simg2img",
            str(sparse),
            str(raw)
        ]


    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )


    if result.returncode != 0:
        raise SparseError(
            result.stderr
            or "simg2img failed"
        )


def linux_path(path: Path):

    path = path.resolve()

    drive = path.drive[0].lower()

    rest = str(path).replace(
        "\\",
        "/"
    )[3:]

    return f"/mnt/{drive}/{rest}"
