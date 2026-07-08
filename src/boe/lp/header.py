from dataclasses import dataclass


LP_METADATA_MAGIC = b"\\x03\\x00\\x00\\x00"


@dataclass
class MetadataHeader:
    major_version: int
    minor_version: int
    header_size: int
    tables_size: int


def parse_header(data: bytes):

    if data[:4] != LP_METADATA_MAGIC:
        raise ValueError("Invalid metadata header")

    major = int.from_bytes(data[4:6], "little")
    minor = int.from_bytes(data[6:8], "little")

    header_size = int.from_bytes(
        data[8:12],
        "little"
    )

    tables_size = int.from_bytes(
        data[40:44],
        "little"
    )

    return MetadataHeader(
        major_version=major,
        minor_version=minor,
        header_size=header_size,
        tables_size=tables_size,
    )
