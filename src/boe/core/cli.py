from __future__ import annotations

from pathlib import Path

import platform
import typer

from boe.core.constants import APP_NAME, APP_VERSION
from boe.plugins.motorola.detector import MotorolaPlugin
from boe.runtime.environment import (
    get_environment,
    validate_python_version,
)
from boe.runtime.session import create_session
from boe.runtime.workspace import Workspace

app = typer.Typer(add_completion=False)

plugin = MotorolaPlugin()


@app.command()
def version() -> None:
    """Show application version."""

    env = get_environment()

    typer.echo(APP_NAME)
    typer.echo(f"Version : {APP_VERSION}")
    typer.echo(f"Python  : {env.python_version}")
    typer.echo(f"OS      : {platform.system()}")


@app.command()
def analyze(
    firmware: Path,
) -> None:
    """Analyze a firmware package."""

    validate_python_version()

    Workspace().create()

    session = create_session()

    typer.echo(f"Session : {session.id}")
    typer.echo()

    if plugin.detect(firmware):
        typer.echo("Motorola firmware detected.\n")

        info = plugin.analyze(firmware)

        typer.echo("====== Firmware ======")
        typer.echo(f"Vendor       : {info.vendor}")
        typer.echo(f"Device       : {info.device}")
        typer.echo(f"Android      : {info.android_version}")
        typer.echo(f"Build ID     : {info.build_id}")
        typer.echo(f"Fingerprint  : {info.fingerprint}")
        typer.echo()

        typer.echo(f"Raw Images   : {len(info.raw_images)}")
        typer.echo(f"Sparsechunks : {len(info.sparsechunks)}")
        typer.echo(f"Flash XML    : {info.flashfile}")
        typer.echo(f"Service XML  : {info.servicefile}")

    else:
        typer.echo("Unsupported firmware.")


@app.callback(invoke_without_command=True)
def root() -> None:
    """Application entry point."""

    typer.echo(APP_NAME)
