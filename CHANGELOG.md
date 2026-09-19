# Changelog

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
