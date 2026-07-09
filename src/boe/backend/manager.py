from pathlib import Path

from .lpunpack import LPUnpackBackend


def get_backend():

    tool = Path(
        "tools/lpunpack/lpunpack.exe"
    )


    if tool.exists():

        return LPUnpackBackend(
            tool
        )


    raise RuntimeError(
        "No LP backend available"
    )
