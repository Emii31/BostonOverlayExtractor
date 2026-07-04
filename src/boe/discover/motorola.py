from __future__ import annotations

import re
from pathlib import Path
from zipfile import ZipFile

from boe.models.firmware import FirmwareInfo


BUILD_RE = re.compile(
    r"ro\.build\.id=(.+)"
)

ANDROID_RE = re.compile(
    r"ro\.build\.version\.release=(.+)"
)

DEVICE_RE = re.compile(
    r"ro\.product\.device=(.+)"
)

FINGERPRINT_RE = re.compile(
    r"ro\.build\.fingerprint=(.+)"
)


def discover(zip_path: Path) -> FirmwareInfo:

    info = FirmwareInfo(
        vendor="Motorola",
        device="Unknown",
        build_id="Unknown",
        android_version="Unknown",
        fingerprint="Unknown",
        path=zip_path,
    )

    with ZipFile(zip_path) as z:

        names = z.namelist()

        for name in names:

            lower = name.lower()

            if "flashfile.xml" in lower:
                info.flashfile = name

            if "servicefile.xml" in lower:
                info.servicefile = name

            if "sparsechunk" in lower:
                info.sparsechunks.append(name)

            if lower.endswith(".img"):
                info.raw_images.append(name)

            if "build.prop" in lower:

                text = z.read(name).decode(
                    "utf-8",
                    errors="ignore",
                )

                if m := BUILD_RE.search(text):
                    info.build_id = m.group(1).strip()

                if m := DEVICE_RE.search(text):
                    info.device = m.group(1).strip()

                if m := ANDROID_RE.search(text):
                    info.android_version = m.group(1).strip()

                if m := FINGERPRINT_RE.search(text):
                    info.fingerprint = m.group(1).strip()

    return info
