from __future__ import annotations

"""
Boston Overlay Extractor

Configuration loading and validation.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from boe.core.constants import (
    DEFAULT_OUTPUT,
    DEFAULT_WORKSPACE,
)
from boe.core.exceptions import ConfigurationError


@dataclass(slots=True)
class AppConfig:
    """
    Application configuration.
    """

    workspace: Path
    output: Path

    profile: str

    parallel_jobs: str

    decode_apks: bool

    keep_workspace: bool

    generate_reports: bool

    verbosity: str


def load_config(path: Path) -> AppConfig:
    """
    Load configuration from a YAML file.

    Parameters
    ----------
    path
        Path to config.yaml.

    Returns
    -------
    AppConfig
    """

    if not path.exists():
        raise ConfigurationError(
            f"Configuration file not found: {path}"
        )

    with path.open("r", encoding="utf-8") as stream:
        data: dict[str, Any] = yaml.safe_load(stream) or {}

    return AppConfig(
        workspace=Path(
            data.get("workspace", DEFAULT_WORKSPACE)
        ),
        output=Path(
            data.get("output", DEFAULT_OUTPUT)
        ),
        profile=data.get("profile", "motorola"),
        parallel_jobs=str(
            data.get("parallel_jobs", "auto")
        ),
        decode_apks=bool(
            data.get("decode_apks", True)
        ),
        keep_workspace=bool(
            data.get("keep_workspace", True)
        ),
        generate_reports=bool(
            data.get("generate_reports", True)
        ),
        verbosity=str(
            data.get("verbosity", "info")
        ),
    )
