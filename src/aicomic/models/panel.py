"""Panel — a single rendered comic panel with its layout metadata."""
from __future__ import annotations

from dataclasses import dataclass

from PIL import Image

from aicomic.core.layout_planner import PanelCell


@dataclass
class Panel:
    cell: PanelCell
    image: Image.Image
    caption: str = ""

    @property
    def width(self) -> int:
        return self.image.width

    @property
    def height(self) -> int:
        return self.image.height