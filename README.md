# k-nobg

KπX sovereign background removal — **FeyNobg** semantic alpha matting.

Three hardware profiles: **CPU**, **Intel Arc (XPU)**, **NVIDIA CUDA**.

## Install from Source

```bash
cd ~/KpihX-Labs/AI/nobg
```

### Editable

```bash
# CPU
uv tool install '.[cpu]' -e

# Intel Arc
uv tool install '.[gpu-intel]' -e

# NVIDIA CUDA
uv tool install '.[gpu-cuda]' -e
```

### Non-editable

```bash
# CPU
uv tool install '.[cpu]'

# Intel Arc
uv tool install '.[gpu-intel]'

# NVIDIA CUDA
uv tool install '.[gpu-cuda]'
```

### Purge

```bash
uv tool uninstall k-nobg
```

## Install from PyPI

```bash
# CPU
uv tool install k-nobg[cpu]

# Intel Arc
uv tool install k-nobg[gpu-intel]

# NVIDIA CUDA
uv tool install k-nobg[gpu-cuda]
```

### Purge

```bash
uv tool uninstall k-nobg
```

## Build / Publish

```bash
make build       # sdist + wheel
make publish     # build + publish to PyPI
make release     # check → push → publish
```

## Sources

- FeyNobg: https://github.com/feyninc/nobg
- Model: `feyninc/FeyNobg` (HuggingFace Hub, ~200 MB, auto-downloaded)
- Full reference: `~/.agents/skills/k-ai/references/remove-bg.md`
