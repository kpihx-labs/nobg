# Changelog

## v0.1.3 - 2026-09-29

- Dev tooling centralized: `ruff` / `pyright` removed from dev-deps (global uv tools now, Makefiles call the binaries with `--pythonpath`).
- Lock converged with the fleet (transformers 5.17.0, numpy 2.5.3, pandas 3.0.6).

## v0.1.2 - 2026-09-29

- Dropped `intel-extension-for-pytorch` from the `gpu-intel` extra (upstream archived March 2026, XPU support is native in `torch`).

## v0.1.1 - 2026-09-19

- Repository paths migrated to the post-reorg layout (`$HOME/Labs/KpihX-Labs/AI/nobg`).
- `batch` annotates its variadic argument as `list[str]`, which is what typer needs to expose
  it as a multi-value CLI argument. `ruff` B008 fired on it because `list` is a mutable
  container, so `typer.Argument` / `typer.Option` are now declared as immutable calls in
  `pyproject.toml` instead of scattering `# noqa: B008`.
- Added `AGENTS.md` project context.

## v0.1.0 — 2026-09-03

- Initial scaffold: `k-nobg` uv project with `remove_bg()`, `remove_bg_batch()`, CLI.
- Makefile with `install-cpu`, `install-gpu-intel`, `install-gpu-cuda` targets.
- Hardware detection via `get_device()` (CUDA → XPU → CPU fallback).
