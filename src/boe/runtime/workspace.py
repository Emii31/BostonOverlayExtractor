from __future__ import annotations

from pathlib import Path

from boe.core.constants import (
    DEFAULT_CACHE,
    DEFAULT_LOGS,
    DEFAULT_OUTPUT,
    DEFAULT_REPORTS,
    DEFAULT_WORKSPACE,
)


class Workspace:
    def __init__(self, root: Path | None = None):
        self.root = root or DEFAULT_WORKSPACE

        self.output = DEFAULT_OUTPUT
        self.cache = DEFAULT_CACHE
        self.logs = DEFAULT_LOGS
        self.reports = DEFAULT_REPORTS

    def create(self) -> None:
        for directory in (
            self.root,
            self.output,
            self.cache,
            self.logs,
            self.reports,
        ):
            directory.mkdir(
                parents=True,
                exist_ok=True,
            )
