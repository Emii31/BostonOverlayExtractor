import argparse
from pathlib import Path

from boe.core.doctor import run_doctor
from boe.pipeline.extract import run_extract


def main():
    parser = argparse.ArgumentParser("BOE")

    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("doctor")

    p_extract = sub.add_parser("extract")
    p_extract.add_argument("firmware")

    args = parser.parse_args()

    if args.cmd == "doctor":
        run_doctor()

    elif args.cmd == "extract":
        run_extract(Path(args.firmware))

    else:
        parser.print_help()
