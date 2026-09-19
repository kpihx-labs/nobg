"""k-nobg — KπX sovereign background removal via FeyNobg semantic matting."""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

try:
    # Single source of truth: the installed distribution metadata, itself fed by pyproject.toml.
    __version__ = _pkg_version("k-nobg")
except PackageNotFoundError:  # source tree that was never installed
    __version__ = "0.0.0"
