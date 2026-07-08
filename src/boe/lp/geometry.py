from dataclasses import dataclass
import struct


LP_GEOMETRY_MAGIC = b"LPG0"


@dataclass
class Geometry:
    metadata_max_size: int
    metadata_slot_count: int
    logical_block_size: int


def parse_geometry(data: bytes):
    if data[:4] != LP_GEOMETRY_MAGIC:
        raise ValueError("Invalid LP geometry magic")

    _, struct_size, checksum, metadata_max_size, metadata_slot_count, logical_block_size = struct.unpack(
        "<4sI32sIII",
        data[:52]
    )

    return Geometry(
        metadata_max_size=metadata_max_size,
        metadata_slot_count=metadata_slot_count,
        logical_block_size=logical_block_size,
    )
