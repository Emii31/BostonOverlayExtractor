from __future__ import annotations

"""
Boston Overlay Extractor

Custom exception hierarchy.

All project-specific exceptions inherit from BOEError.
This allows the application to catch expected failures cleanly
without masking unexpected Python exceptions.
"""


class BOEError(Exception):
    """
    Base exception for all Boston Overlay Extractor errors.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class ConfigurationError(BOEError):
    """
    Raised when configuration files are missing or invalid.
    """


class ArchiveError(BOEError):
    """
    Raised when an archive cannot be opened or recognized.
    """


class WorkspaceError(BOEError):
    """
    Raised when the workspace cannot be created or accessed.
    """


class PluginError(BOEError):
    """
    Raised when plugin loading or execution fails.
    """


class ExtractionError(BOEError):
    """
    Raised when partition extraction fails.
    """


class FilesystemError(BOEError):
    """
    Raised when mounting or extracting a filesystem fails.
    """


class SparseChunkError(BOEError):
    """
    Raised when sparsechunk images are incomplete or corrupted.
    """


class SuperImageError(BOEError):
    """
    Raised when parsing or extracting super.img fails.
    """


class ApkError(BOEError):
    """
    Raised during APK discovery or decompilation.
    """


class ResourceError(BOEError):
    """
    Raised while parsing Android resources.
    """


class OverlayError(BOEError):
    """
    Raised during Runtime Resource Overlay generation.
    """


class DatabaseError(BOEError):
    """
    Raised when interacting with the internal SQLite database.
    """


class BuildError(BOEError):
    """
    Raised during overlay compilation or Magisk module packaging.
    """


class ValidationError(BOEError):
    """
    Raised when validation of user input or generated data fails.
    """
