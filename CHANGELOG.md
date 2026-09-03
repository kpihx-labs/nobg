# Changelog

## v0.1.0 — 2026-09-03

- Initial scaffold: `k-nobg` uv project with `remove_bg()`, `remove_bg_batch()`, CLI.
- Makefile with `install-cpu`, `install-gpu-intel`, `install-gpu-cuda` targets.
- Hardware detection via `get_device()` (CUDA → XPU → CPU fallback).
