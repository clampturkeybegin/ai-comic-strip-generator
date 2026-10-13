"""Entry point. Wires config, model runner, and the Qt GUI together."""
from __future__ import annotations

import sys
from pathlib import Path

from aicomic.config.settings import AppSettings
from aicomic.core.engine import StripEngine
from aicomic.services.model_runner import ModelRunner
from aicomic.utils.logging_setup import configure_logging
from aicomic.utils.paths import app_data_dir


def build_engine(settings: AppSettings) -> StripEngine:
    runner = ModelRunner(
        weights_dir=settings.weights_dir,
        device=settings.device,
        tile_size=settings.tile_size,
    )
    return StripEngine(settings=settings, runner=runner)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv if argv is None else argv)
    configure_logging(app_data_dir() / "logs")

    settings = AppSettings.load()
    engine = build_engine(settings)

    if "--headless" in argv:
        from aicomic.cli import run_headless

        return run_headless(engine, argv)

    from aicomic.gui.main_window import launch

    return launch(engine)


if __name__ == "__main__":
    raise SystemExit(main())