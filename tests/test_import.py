"""Basic import + smoke tests."""

from importlib.metadata import version

import pytest


def test_import():
    from k_nobg import __version__

    # `__version__` must mirror the installed distribution metadata (single source of truth),
    # never a second hardcoded copy that drifts on every release.
    assert __version__ == version("k-nobg")


def test_remove_module():
    from k_nobg.remove import remove_bg
    # remove_bg requires torch — skip if not installed
    pytest.importorskip("torch")
    from k_nobg.remove import get_device
    device = get_device()
    assert device in ("cpu", "cuda", "xpu")


def test_cli():
    from k_nobg.cli import app
    assert app is not None
