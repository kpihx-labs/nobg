"""Core background removal — FeyNobg semantic alpha matting."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path


def get_device() -> str:
    """Select the best available device at runtime. Never assume.

    Torch is imported lazily — this function requires torch to be installed
    (via make install-cpu / install-gpu-intel / install-gpu-cuda).
    """
    import torch  # type: ignore[import-untyped]

    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch, "xpu") and torch.xpu.is_available():
        return "xpu"
    return "cpu"


def remove_bg(
    input_path: str | Path,
    output_path: str | Path | None = None,
    device: str | None = None,
) -> Path:
    """Remove background from a single image.

    Args:
        input_path: Source image (PNG, JPEG, WebP, HEIC).
        output_path: Destination path. Defaults to <input>-nobg.png.
        device: Force a device ("cpu", "cuda", "xpu"). None = auto-detect.

    Returns:
        Path to the output PNG.
    """
    from nobg import AutoModel  # type: ignore[import-untyped]

    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input not found: {input_path}")

    if output_path is None:
        output_path = input_path.with_name(f"{input_path.stem}-nobg.png")
    else:
        output_path = Path(output_path)

    if device is None:
        device = get_device()

    model = AutoModel.from_pretrained("feyninc/FeyNobg").eval().to(device)
    cutout = model.process(str(input_path))
    cutout.save(str(output_path))

    return output_path


def remove_bg_batch(
    input_paths: Sequence[str | Path],
    output_dir: str | Path | None = None,
    device: str | None = None,
    verbose: bool = False,
) -> list[Path]:
    """Remove backgrounds from multiple images.

    Args:
        input_paths: List of source images.
        output_dir: Directory for outputs. Defaults to same dir as input.
        device: Force a device. None = auto-detect.
        verbose: Print per-image progress.

    Returns:
        List of output paths.
    """
    import time

    from nobg import AutoModel  # type: ignore[import-untyped]

    if device is None:
        device = get_device()

    model = AutoModel.from_pretrained("feyninc/FeyNobg").eval().to(device)
    results: list[Path] = []

    for i, input_path in enumerate(input_paths, 1):
        input_path = Path(input_path)
        if not input_path.exists():
            raise FileNotFoundError(f"Input not found: {input_path}")

        if output_dir is not None:
            out = Path(output_dir) / f"{input_path.stem}-nobg.png"
        else:
            out = input_path.with_name(f"{input_path.stem}-nobg.png")

        if verbose:
            print(f"[{i}/{len(input_paths)}] {input_path.name} ...", end=" ", flush=True)

        t0 = time.time()
        cutout = model.process(str(input_path))
        cutout.save(str(out))
        elapsed = time.time() - t0

        if verbose:
            print(f"done in {elapsed:.1f}s")

        results.append(out)

    return results
