from __future__ import annotations

"""
Boston Overlay Extractor

Application state management.

This module manages the runtime session state and persists it
to disk as JSON.
"""

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from boe.core.constants import STATE_FILENAME
from boe.core.exceptions import WorkspaceError


@dataclass(slots=True)
class AppState:
    """
    Runtime state for a BOE session.
    """

    session_id: str

    created_at: str

    current_stage: str = "initialized"

    plugin: str | None = None

    input_path: str | None = None

    completed_steps: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)


class StateManager:
    """
    Handles loading and saving the application state.
    """

    def __init__(self, workspace: Path) -> None:
        self.workspace = workspace
        self.state_file = workspace / STATE_FILENAME

    def create(self, session_id: str) -> AppState:
        """
        Create a new application state.
        """

        state = AppState(
            session_id=session_id,
            created_at=datetime.utcnow().isoformat(timespec="seconds") + "Z",
        )

        self.save(state)

        return state

    def save(self, state: AppState) -> None:
        """
        Save state to disk.
        """

        self.workspace.mkdir(parents=True, exist_ok=True)

        with self.state_file.open(
            "w",
            encoding="utf-8",
        ) as stream:
            json.dump(
                asdict(state),
                stream,
                indent=4,
                ensure_ascii=False,
            )

    def load(self) -> AppState:
        """
        Load state from disk.
        """

        if not self.state_file.exists():
            raise WorkspaceError(
                f"State file not found: {self.state_file}"
            )

        with self.state_file.open(
            "r",
            encoding="utf-8",
        ) as stream:
            data = json.load(stream)

        return AppState(**data)
