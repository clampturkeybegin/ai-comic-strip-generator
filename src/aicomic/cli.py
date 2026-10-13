"""Headless mode: render a strip from a script file without the GUI."""
from __future__ import annotations

from pathlib import Path

from aicomic.core.engine import StripEngine


def run_headless(engine: StripEngine, argv: list[str]) -> int:
    try:
        script_path = Path(argv[argv.index("--script") + 1])
    except (ValueError, IndexError):
        print("usage: aicomic --headless --script <path> [--out <dir>]")
        return 2

    out_dir = Path(argv[argv.index("--out") + 1]) if "--out" in argv else Path("output")
    strip = engine.render_from_file(script_path)
    written = strip.export(out_dir)
    print(f"exported {len(written)} panels to {out_dir}")
    return 0