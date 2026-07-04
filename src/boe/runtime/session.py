from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(slots=True, frozen=True)
class Session:
    id: str
    created: datetime


def create_session() -> Session:
    return Session(
        id=uuid4().hex,
        created=datetime.now(UTC),
    )
