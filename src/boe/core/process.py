from subprocess import run
from pathlib import Path


def execute(cmd: list[str]) -> int:
    print(f"[RUN] {' '.join(cmd)}")

    result = run(cmd, shell=True)

    return result.returncode
