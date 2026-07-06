from __future__ import annotations

import json
from pathlib import Path

from boe.utils.archive import extract_archive

ROOT = Path.cwd()

WORKSPACE = ROOT / "workspace"
EXTRACTED = WORKSPACE / "extracted"

TOOLS = ROOT / "tools"


def run_extract(firmware: Path):

    seven_zip = TOOLS / "7zip" / "7z.exe"

    print("[1/4] Extracting firmware...")

    extract_archive(
        firmware,
        EXTRACTED,
        seven_zip,
    )

    print("[2/4] Building inventory...")

    files = []

    for item in EXTRACTED.rglob("*"):

        if item.is_file():

            files.append(
                {
                    "path": str(item.relative_to(EXTRACTED)),
                    "size": item.stat().st_size,
                }
            )

    inventory = {
        "firmware": firmware.name,
        "file_count": len(files),
        "files": files,
    }

    inventory_path = WORKSPACE / "inventory.json"

    with inventory_path.open(
        "w",
        encoding="utf-8",
    ) as fp:
        json.dump(
            inventory,
            fp,
            indent=4,
        )

        print("[3/4] Building inventory...")

    files = []

    flashfile = None
    servicefile = None
    build_prop = None

    sparse = []
    boot = None
    vendor_boot = None
    vbmeta = None
    dtbo = None

    for item in EXTRACTED.rglob("*"):

        if not item.is_file():
            continue

        rel = item.relative_to(EXTRACTED)

        files.append(
            {
                "path": str(rel),
                "size": item.stat().st_size,
            }
        )

        name = item.name.lower()

        if name == "flashfile.xml":
            flashfile = rel

        elif name == "servicefile.xml":
            servicefile = rel

        elif name == "build.prop":
            build_prop = rel

        elif name.startswith("super.img_sparsechunk"):
            sparse.append(rel)

        elif name == "boot.img":
            boot = rel

        elif name == "vendor_boot.img":
            vendor_boot = rel

        elif name == "vbmeta.img":
            vbmeta = rel

        elif name == "dtbo.img":
            dtbo = rel

    inventory = {
        "firmware": firmware.name,
        "file_count": len(files),
        "flashfile": str(flashfile) if flashfile else None,
        "servicefile": str(servicefile) if servicefile else None,
        "build_prop": str(build_prop) if build_prop else None,
        "sparsechunks": len(sparse),
        "boot": str(boot) if boot else None,
        "vendor_boot": str(vendor_boot) if vendor_boot else None,
        "vbmeta": str(vbmeta) if vbmeta else None,
        "dtbo": str(dtbo) if dtbo else None,
        "files": files,
    }

    inventory_path = WORKSPACE / "inventory.json"

    with inventory_path.open("w", encoding="utf-8") as fp:
        json.dump(inventory, fp, indent=4)

    print()

    print("========== Motorola Firmware ==========")
    print(f"Firmware         : {firmware.name}")
    print(f"flashfile.xml    : {'YES' if flashfile else 'NO'}")
    print(f"servicefile.xml  : {'YES' if servicefile else 'NO'}")
    print(f"boot.img         : {'YES' if boot else 'NO'}")
    print(f"vendor_boot.img  : {'YES' if vendor_boot else 'NO'}")
    print(f"vbmeta.img       : {'YES' if vbmeta else 'NO'}")
    print(f"dtbo.img         : {'YES' if dtbo else 'NO'}")
    print(f"Sparsechunks     : {len(sparse)}")
    print("=======================================\n")
