"""ComicStrip — ordered collection of panels + export metadata."""
from __future__ import annotations

from dataclasses import dataclass, field

from aicomic.core.layout_planner import PanelCell
from aicomic.models.panel import Panel


@dataclass
class ComicStrip:
    title: str
    style: str = "manga-ink"
    panels: list[Panel] = field(default_factory=list)
    cols: int = 3

    def add_panel(self, cell: PanelCell, image: object, caption: str = "") -> None:
        from PIL import Image

        assert isinstance(image, Image.Image)
        self.panels.append(Panel(cell=cell, image=image, caption=caption))

    def export(self, out_dir: object) -> list[object]:
        from pathlib import Path

        from aicomic.services.exporter import StripExporter

        return StripExporter().export(self, Path(out_dir))  # type: ignore[arg-type]