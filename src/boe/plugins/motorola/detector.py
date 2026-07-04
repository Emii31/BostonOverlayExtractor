from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile

from boe.discover.motorola import discover
from boe.models.firmware import FirmwareInfo
from boe.plugins.base import VendorPlugin


class MotorolaPlugin(VendorPlugin):
    """Motorola firmware detection plugin."""

    name = "Motorola"

    def detect(
        self,
        firmware: Path,
    ) -> bool:
        """
        Return True if the firmware appears to be a Motorola firmware package.
        """

        if not firmware.exists():
            return False

        if firmware.suffix.lower() != ".zip":
            return False

        try:
            with ZipFile(firmware) as archive:
                names = archive.namelist()

            markers = (
                "flashfile.xml",
                "servicefile.xml",
                "gpt.bin",
            )

            return any(
                any(marker in name.lower() for marker in markers)
                for name in names
            )

        except Exception:
            return False

    def analyze(
        self,
        firmware: Path,
    ) -> FirmwareInfo:
        """
        Analyze a Motorola firmware package.
        """

        return discover(firmware)
