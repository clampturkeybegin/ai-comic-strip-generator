"""Plans a grid of panels from N script beats.

Even split by default; wide/narrow bias for action beats.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PanelCell:
    script_index: int
    row: int
    col: int
    width: int
    height: int


@dataclass(frozen=True)
class Layout:
    cells: list[PanelCell]
    rows: int
    cols: int


class LayoutPlanner:
    def __init__(self, panels_per_row: int = 3, panel_px: int = 512) -> None:
        self._per_row = panels_per_row
        self._panel_px = panel_px

    def plan(self, panels: list[str]) -> Layout:
        rows = (len(panels) + self._per_row - 1) // self._per_row
        cells: list[PanelCell] = []
        for i in range(len(panels)):
            row, col = divmod(i, self._per_row)
            cells.append(
                PanelCell(
                    script_index=i,
                    row=row,
                    col=col,
                    width=self._panel_px,
                    height=self._panel_px,
                )
            )
        return Layout(cells=cells, rows=rows, cols=min(self._per_row, len(panels)))