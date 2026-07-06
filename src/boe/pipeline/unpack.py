from pathlib import Path
import shutil
from boe.pipeline.super_parser import run_super_parse

MERGED = Path("workspace/merged")
OUT = Path("workspace/unpacked")

SUPER = MERGED / "super.img"


def run_unpack():
    print("[1/3] Checking super.img...")

    if not SUPER.exists():
        print("[ERROR] super.img missing")
        return

    if OUT.exists():
        shutil.rmtree(OUT)

    OUT.mkdir(parents=True)

    print("[2/3] Running BOE super parser (NO external tools)...")

    ok = run_super_parse(SUPER, OUT)

    print("[3/3] Finalizing output...")

    print("\n========== BOE AUTO MODE ==========")
    print("Backend : Native super parser")
    print(f"Status  : {'SUCCESS' if ok else 'PARTIAL'}")
    print("===================================\n")
