from __future__ import annotations

import subprocess
from pathlib import Path


class ProcessError(RuntimeError):
    pass


class Process:
    @staticmethod
    def run(cmd: list[str], cwd=None) -> str:
        result = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            shell=False,
        )

        if result.returncode != 0:
            print("\n========== PROCESS ERROR ==========")
            print("CMD:", " ".join(cmd))
            print("\nSTDOUT:\n", result.stdout)
            print("\nSTDERR:\n", result.stderr)
            print("==================================\n")

            raise ProcessError(result.stderr.strip() or "Process failed")

        return result.stdout.strip()
