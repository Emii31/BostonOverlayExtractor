from pathlib import Path

from .geometry import parse_geometry


class LPParser:

    def __init__(self, image: Path):
        self.image = image


    def locate_geometry(self):

        magic = b"LPG0"

        with self.image.open("rb") as f:

            # scan first 4MB
            chunk = f.read(4 * 1024 * 1024)

            pos = chunk.find(magic)

            if pos != -1:
                return pos


            # check secondary geometry area
            f.seek(-4 * 1024 * 1024, 2)

            chunk = f.read(4 * 1024 * 1024)

            pos = chunk.find(magic)

            if pos != -1:
                return (
                    self.image.stat().st_size
                    - (4 * 1024 * 1024)
                    + pos
                )


        raise RuntimeError(
            "LP geometry not found"
        )


    def parse(self):

        offset = self.locate_geometry()

        print(
            "[LP] Geometry offset:",
            offset
        )

        with self.image.open("rb") as f:

            f.seek(offset)

            geometry = parse_geometry(
                f.read(4096)
            )


        print(
            "[LP] Block size:",
            geometry.logical_block_size
        )

        print(
            "[LP] Metadata size:",
            geometry.metadata_max_size
        )

        return geometry
