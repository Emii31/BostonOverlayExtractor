from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ArchiveInfo:
    path: Path
    archive_type: str
    size: int
