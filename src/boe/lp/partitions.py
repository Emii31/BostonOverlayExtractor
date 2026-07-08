from dataclasses import dataclass


@dataclass
class Partition:
    name: str
    attributes: int
    first_extent: int
    num_extents: int


def parse_partitions(data: bytes, count: int):

    partitions = []

    size = 52

    for i in range(count):

        entry = data[i*size:(i+1)*size]

        name = entry[:36].split(b"\0")[0].decode(
            errors="ignore"
        )

        attributes = int.from_bytes(
            entry[36:40],
            "little"
        )

        first_extent = int.from_bytes(
            entry[40:44],
            "little"
        )

        num_extents = int.from_bytes(
            entry[44:48],
            "little"
        )

        partitions.append(
            Partition(
                name,
                attributes,
                first_extent,
                num_extents
            )
        )

    return partitions
