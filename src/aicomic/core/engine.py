"""StripEngine — orchestrates script parsing, layout, render, and export."""
from __future__ import annotations

import logging
from pathlib import Path

from aicomic.config.settings import AppSettings
from aicomic.core.layout_planner import LayoutPlanner
from aicomic.core.script_parser import ScriptParser
from aicomic.models.strip import ComicStrip
from aicomic.services.exporter import StripExporter
from aicomic.services.model_runner import ModelRunner

log = logging.getLogger(__name__)


class StripEngine:
    """Top-level facade. One instance per app session.

    Thread-safe for render() calls only if the underlying ModelRunner is.
    Holds no per-render state; safe to reuse.
    """

    def __init__(self, settings: AppSettings, runner: ModelRunner) -> None:
        self._settings = settings
        self._runner = runner
        self._parser = ScriptParser()
        self._planner = LayoutPlanner(panels_per_row=settings.panels_per_row)
        self._exporter = StripExporter()

    def render_from_file(self, script_path: Path) -> ComicStrip:
        script = self._parser.parse(script_path.read_text(encoding="utf-8"))
        return self.render(script.title, script.panels)

    def render(self, title: str, panels: list[str]) -> ComicStrip:
        layout = self._planner.plan(panels)
        strip = ComicStrip(title=title, style=self._settings.default_style)
        for idx, cell in enumerate(layout.cells):
            log.info("rendering panel %d/%d", idx + 1, len(layout.cells))
            image = self._runner.render_panel(
                prompt=panels[cell.script_index],
                style=self._settings.default_style,
                width=cell.width,
                height=cell.height,
                seed=self._settings.seed + idx,
            )
            strip.add_panel(cell, image)
        return strip

    def export(self, strip: ComicStrip, out_dir: Path) -> list[Path]:
        return self._exporter.export(strip, out_dir)