import argparse
from pathlib import Path
from boe.pipeline.merge import run_merge
from boe.pipeline.unpack import run_unpack
from boe.core.doctor import run_doctor
from boe.pipeline.extract import run_extract


def main():
    parser = argparse.ArgumentParser("BOE")

    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("doctor")

    p_extract = sub.add_parser("extract")
    p_extract.add_argument("firmware")

    sub.add_parser("merge")  # ADD THIS

    sub.add_parser("unpack")

    args = parser.parse_args()

    if args.cmd == "doctor":
        run_doctor()

    elif args.cmd == "extract":
        run_extract(Path(args.firmware))

    elif args.cmd == "merge":
        run_merge()

    elif args.cmd == "unpack":
        run_unpack()

    else:
        parser.print_help()
