from __future__ import annotations

"""
Boston Overlay Extractor

Application context.

This module defines the runtime context shared across the application.
"""

from dataclasses import dataclass, field
from logging import Logger
from pathlib import Path
from typing import Any

from boe.core.config import AppConfig


@dataclass(slots=True)
class BOEContext:
    """
    Runtime application context.

    This object is passed to all major components so they can
    access shared application state without requiring a long
    parameter list.
    """

    config: AppConfig

    logger: Logger

    workspace: Path

    output: Path

    session_id: str

    plugin: Any | None = None

    database: Any | None = None

    state: dict[str, Any] = field(default_factory=dict)
