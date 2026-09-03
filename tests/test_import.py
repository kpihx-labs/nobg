"""Basic import + smoke tests."""

import pytest


def test_import():
    from k_nobg import __version__
    assert __version__ == "0.1.0"


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
