"""k-nobg CLI — sovereign background removal."""

from __future__ import annotations

import typer
from rich.console import Console

app = typer.Typer(
    name="k-nobg",
    help="KπX sovereign background removal — FeyNobg semantic matting.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def remove(
    input: str = typer.Argument(..., help="Input image path"),
    output: str | None = typer.Option(None, "-o", "--output", help="Output path (default: <input>-nobg.png)"),
    device: str | None = typer.Option(None, "-d", "--device", help="Force device: cpu, cuda, xpu (default: auto)"),
) -> None:
    """Remove background from a single image."""
    from k_nobg.remove import remove_bg

    out = remove_bg(input, output, device)
    console.print(f"✅ {out}")


@app.command()
def batch(
    inputs: list[str] = typer.Argument(..., help="Input image paths"),
    output_dir: str | None = typer.Option(None, "-o", "--output-dir", help="Output directory"),
    device: str | None = typer.Option(None, "-d", "--device", help="Force device: cpu, cuda, xpu (default: auto)"),
    verbose: bool = typer.Option(False, "-v", "--verbose", help="Show per-image progress"),
) -> None:
    """Remove backgrounds from multiple images."""
    import time

    from k_nobg.remove import remove_bg_batch

    t0 = time.time()
    results = remove_bg_batch(inputs, output_dir, device, verbose=verbose)
    elapsed = time.time() - t0
    for r in results:
        console.print(f"✅ {r}")
    console.print(f"\n{len(results)} images in {elapsed:.1f}s ({elapsed / len(results):.1f}s/image)")


@app.command()
def info() -> None:
    """Show device and model status."""
    import torch  # type: ignore[import-untyped]

    from k_nobg.remove import get_device

    device = get_device()
    console.print(f"[bold]torch[/bold]: {torch.__version__}")
    console.print(f"[bold]CUDA[/bold]: {torch.cuda.is_available()}")
    if hasattr(torch, "xpu"):
        console.print(f"[bold]XPU[/bold]: {torch.xpu.is_available()}")
    console.print(f"[bold]Selected device[/bold]: {device}")

    try:
        from pathlib import Path

        cache = Path.home() / ".cache/huggingface/hub/models--feyninc--FeyNobg"
        if cache.exists():
            console.print(f"[bold]Model[/bold]: ✅ cached at {cache}")
        else:
            console.print("[bold]Model[/bold]: ⚠️ not cached (will download on first run)")
    except (OSError, ValueError):
        console.print("[bold]Model[/bold]: ⚠️ unable to check cache")


if __name__ == "__main__":
    app()
