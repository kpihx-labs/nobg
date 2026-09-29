PKG_NAME     := k-nobg
PKG_DIR_NAME := k_nobg
PKG_DIR      := src/$(PKG_DIR_NAME)
VERSION      := $(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d= -f2 | xargs)

UV     := $(shell command -v uv 2>/dev/null || echo uv)
PYTHON := $(UV) run python
PYTEST := $(PYTHON) -m pytest

PY_FILES := $(shell $(UV) run python -c 'from pathlib import Path; print(" ".join(map(str, Path("$(PKG_DIR)").rglob("*.py"))))')

.PHONY: help check smoke build publish push release

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ─── Quality ─────────────────────────────────────────────────────────────────

check: smoke ## Lint + format + type-check + tests
	@ruff check --fix $(PKG_DIR)/
	@ruff format $(PKG_DIR)/
	@$(PYTHON) -m py_compile $(PY_FILES)
	@pyright --pythonpath .venv/bin/python $(PKG_DIR)/
	@$(PYTHON) -m pytest tests/ -v

smoke:  ## Smoke test — import + CLI
	@$(PYTHON) -c "from $(PKG_DIR_NAME) import __version__; print('✅ $(PKG_NAME) v' + __version__)"
	@$(PYTHON) -c "from $(PKG_DIR_NAME).cli import app; print('✅ CLI ok')"
	@echo "✅ smoke test passed"

# ─── Build / Publish ─────────────────────────────────────────────────────────

build: ## Build sdist + wheel
	@rm -rf dist
	@echo "🏗️  Building $(PKG_NAME) v$(VERSION)..."
	@$(UV) build --clear

publish: build ## Publish to PyPI (requires UV_PUBLISH_TOKEN)
	@echo "🚀 Publishing v$(VERSION) to PyPI..."
	@$(UV) publish

# ─── Git ─────────────────────────────────────────────────────────────────────

push: ## Push current branch to all remotes
	@branch="$$(git branch --show-current)"; \
	for remote in $$(git remote); do \
		echo "==> pushing $$branch to $$remote"; \
		git push "$$remote" "$$branch"; \
	done

# ─── Release ─────────────────────────────────────────────────────────────────

release: check push publish ## Full release: check → push → publish
	@echo "✅ $(PKG_NAME) v$(VERSION) released"
