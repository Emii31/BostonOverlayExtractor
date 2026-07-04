from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class FirmwareInfo:

    vendor: str

    device: str

    build_id: str

    android_version: str

    fingerprint: str

    path: Path

    flashfile: str | None = None

    servicefile: str | None = None

    sparsechunks: list[str] = field(default_factory=list)

    raw_images: list[str] = field(default_factory=list)

    partitions: list[str] = field(default_factory=list)
