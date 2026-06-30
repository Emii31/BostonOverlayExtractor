from __future__ import annotations

"""
Boston Overlay Extractor

Environment detection and validation.
"""

import platform
import sys
from dataclasses import dataclass

from boe.core.constants import MINIMUM_PYTHON
from boe.core.exceptions import ConfigurationError


@dataclass(slots=True, frozen=True)
class EnvironmentInfo:
    """
    Information about the current runtime environment.
    """

    python_version: str
    python_version_tuple: tuple[int, int, int]
    operating_system: str
    architecture: str
    machine: str


def get_environment() -> EnvironmentInfo:
    """
    Collect information about the current runtime environment.
    """

    return EnvironmentInfo(
        python_version=platform.python_version(),
        python_version_tuple=sys.version_info[:3],
        operating_system=platform.system(),
        architecture=platform.architecture()[0],
        machine=platform.machine(),
    )


def validate_python_version() -> None:
    """
    Ensure the current Python version meets the minimum requirement.
    """

    current = sys.version_info

    if current < MINIMUM_PYTHON:
        required = ".".join(map(str, MINIMUM_PYTHON))
        current_str = ".".join(
            map(str, current[:3])
        )

        raise ConfigurationError(
            f"Python {required}+ is required "
            f"(current: {current_str})"
        )
