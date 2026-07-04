from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from boe.models.firmware import FirmwareInfo


class VendorPlugin(ABC):

    name: str

    @abstractmethod
    def detect(
        self,
        firmware: Path,
    ) -> bool:
        ...

    @abstractmethod
    def analyze(
        self,
        firmware: Path,
    ) -> FirmwareInfo:
        ...
