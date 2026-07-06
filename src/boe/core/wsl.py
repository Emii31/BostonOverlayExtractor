from __future__ import annotations

import subprocess
from pathlib import Path


class WSL:
    """
    Silent WSL execution layer for BOE.
    """

    @staticmethod
    def run(command: str) -> str:
        """
        Run Linux command inside WSL and return output.
        """
        result = subprocess.run(
            ["wsl", "-e", "bash", "-lc", command],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print("\n========== WSL ERROR ==========")
            print(result.stderr or result.stdout)
            print("================================\n")
            raise RuntimeError("WSL command failed")

        return result.stdout.strip()
