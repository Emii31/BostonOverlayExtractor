import platform
import sys
import shutil

from boe.core.tool_manager import TOOLS


def run_doctor() -> None:
    print("\n========== BOE DOCTOR ==========\n")

    print(f"OS      : {platform.system()}")
    print(f"Python  : {sys.version.split()[0]}")

    print("\nTools:\n")

    for name, path in TOOLS.items():
        status = "✓ FOUND" if shutil.which(path) or __exists(path) else "✗ MISSING"
        print(f"{name:10} : {status}")

    print("\n================================\n")


def __exists(path: str) -> bool:
    from pathlib import Path
    return Path(path).exists()
