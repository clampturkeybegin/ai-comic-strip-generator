"""Handler for the 'Render Strip' action. Runs on a worker thread."""
from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QObject, Signal, Slot

from aicomic.core.engine import StripEngine


class RenderHandler(QObject):
    progress = Signal(int, int)
    finished = Signal(object)
    failed = Signal(str)

    def __init__(self, engine: StripEngine, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self._engine = engine

    @Slot(str, list)
    def render(self, title: str, panels: list[str]) -> None:
        try:
            strip = self._engine.render(title, panels)
            self.finished.emit(strip)
        except Exception as exc:  # surface to UI, don't kill the app
            self.failed.emit(str(exc))

    @Slot(object, str)
    def export(self, strip: object, out_dir: str) -> None:
        try:
            self._engine.export(strip, Path(out_dir))  # type: ignore[arg-type]
            self.finished.emit(strip)
        except Exception as exc:
            self.failed.emit(str(exc))