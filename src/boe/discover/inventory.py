from __future__ import annotations

from zipfile import ZipFile


def build_inventory(zip_path):

    with ZipFile(zip_path) as z:

        return sorted(z.namelist())
