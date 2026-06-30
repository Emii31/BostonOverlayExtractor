from __future__ import annotations

"""
Boston Overlay Extractor

Application-wide constants.

This module contains immutable values used throughout the project.
Keeping these values centralized avoids hard-coded strings and
makes future maintenance significantly easier.
"""

from pathlib import Path

# ==============================================================================
# Application Metadata
# ==============================================================================

APP_NAME: str = "Boston Overlay Extractor"
APP_SHORT_NAME: str = "BOE"
APP_VERSION: str = "0.1.0-dev"

# ==============================================================================
# Python Requirements
# ==============================================================================

MINIMUM_PYTHON = (3, 11)

# ==============================================================================
# Default Directories
# ==============================================================================

DEFAULT_WORKSPACE = Path("workspace")
DEFAULT_OUTPUT = Path("output")
DEFAULT_CACHE = Path("cache")
DEFAULT_LOGS = Path("logs")
DEFAULT_REPORTS = Path("reports")

# ==============================================================================
# Supported Archive Types
# ==============================================================================

SUPPORTED_ARCHIVES: tuple[str, ...] = (
    ".zip",
    ".tar",
    ".tar.gz",
    ".tgz",
    ".7z",
)

# ==============================================================================
# Supported Image Types
# ==============================================================================

SUPPORTED_IMAGES: tuple[str, ...] = (
    ".img",
    ".bin",
    ".new.dat",
    ".new.dat.br",
)

# ==============================================================================
# Known Android Partitions
# ==============================================================================

KNOWN_PARTITIONS: tuple[str, ...] = (
    "boot",
    "vendor_boot",
    "vendor",
    "system",
    "system_ext",
    "product",
    "odm",
    "super",
    "dtbo",
    "vbmeta",
    "vbmeta_system",
    "init_boot",
    "recovery",
)

# ==============================================================================
# Motorola Detection Files
# ==============================================================================

MOTOROLA_MARKERS: tuple[str, ...] = (
    "flashfile.xml",
    "servicefile.xml",
    "gpt.bin",
    "boot.img",
    "vendor_boot.img",
)

# ==============================================================================
# Logging
# ==============================================================================

DEFAULT_LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# ==============================================================================
# Exit Codes
# ==============================================================================

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_INVALID_INPUT = 2
EXIT_CONFIGURATION_ERROR = 3
EXIT_EXTRACTION_ERROR = 4
EXIT_PLUGIN_ERROR = 5

# ==============================================================================
# Session
# ==============================================================================

SESSION_PREFIX = "session_"

STATE_FILENAME = "state.json"

CONFIG_FILENAME = "config.yaml"

LOG_FILENAME = "boe.log"
