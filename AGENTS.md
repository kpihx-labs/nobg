# k-nobg

KπX sovereign background removal project — FeyNobg semantic alpha matting.

## Purpose

Provides a local, sovereign background removal tool using the FeyNobg model (BiRefNet). Three hardware profiles: CPU, Intel Arc (XPU), NVIDIA CUDA.

## Structure

```
src/k_nobg/
├── __init__.py    # version
├── remove.py      # core: remove_bg(), remove_bg_batch(), get_device()
└── cli.py         # k-nobg CLI (typer)
tests/
└── test_import.py
Makefile           # install-cpu, install-gpu-intel, install-gpu-cuda
```

## Rules

- `uv` only — never `pip`.
- Device is selected at runtime via `get_device()` — never assume CUDA/XPU.
- Model is downloaded to `~/.cache/huggingface/` on first run — not vendored.
- See `~/.agents/skills/k-ai/references/remove-bg.md` for the full background removal reference.
