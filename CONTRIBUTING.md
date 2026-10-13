# Contributing to ai-comic-strip-generator

Thanks for wanting to help build the strip engine. This is a hobbyist/educational
project — a Windows desktop tool that turns a script or prompt into a multi-panel
comic strip using local diffusion models and a layout planner.

## Ground rules

- Python 3.11+ on Windows 10/11. Linux/macOS work for engine dev but the GUI targets Windows.
- One feature per PR. Keep diffs reviewable.
- Every new handler under `src/aicomic/handlers/` needs a matching test in `tests/`.
- Don't commit model weights. They live under `models/weights/` and are gitignored.

## Dev setup

```
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
python -m aicomic.bootstrap
```

## Style

- Black + Ruff. `ruff check src tests` must pass.
- Type hints on every public function. `mypy src` clean.
- No bare `except:`. Catch specific exceptions, log, re-raise or degrade.

## Adding a panel renderer

1. Drop a new module in `src/aicomic/services/renderers/`.
2. Subclass `BaseRenderer` from `services/renderers/base.py`.
3. Register it in `services/renderer_registry.py`.
4. Add a golden test in `tests/test_renderers.py`.

## Commit messages

`area: short imperative summary` — e.g. `layout: fix gutter overlap on 3-panel grid`.

## Reporting bugs

Open an issue with: OS build, GPU + VRAM, model checkpoint name, the script input,
and the exported strip. Attach logs from `~/.aicomic/logs/`.