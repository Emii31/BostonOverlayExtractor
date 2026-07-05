from __future__ import annotations

import shutil
from pathlib import Path

TOOLS = {
    "7z": "tools/7zip/7z.exe",
    "apktool": "tools/apktool/apktool.jar",
    "aapt2": "tools/aapt2/aapt2.exe",
    "lpunpack": "tools/lpunpack/lpunpack.exe",
    "simg2img": "tools/simg2img/simg2img.exe",
}


def find_tool(path: str) -> bool:
    return Path(path).exists()


def setup_tools() -> None:
    print("[BOOT] Checking tools...\n")

    for name, path in TOOLS.items():
        if find_tool(path):
            print(f"[OK] {name}")
        else:
            print(f"[MISSING] {name} -> {path}")

    print("\n[BOOT] Tool check complete.")
