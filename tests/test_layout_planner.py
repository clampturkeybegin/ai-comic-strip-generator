"""Tests for LayoutPlanner grid math."""
from __future__ import annotations

from aicomic.core.layout_planner import LayoutPlanner


def test_single_row() -> None:
    layout = LayoutPlanner(panels_per_row=3).plan(["a", "b", "c"])
    assert layout.rows == 1
    assert layout.cols == 3
    assert [c.script_index for c in layout.cells] == [0, 1, 2]


def test_wraps_to_second_row() -> None:
    layout = LayoutPlanner(panels_per_row=3).plan(["a", "b", "c", "d"])
    assert layout.rows == 2
    assert layout.cells[3].row == 1
    assert layout.cells[3].col == 0


def test_all_cells_are_square_panels() -> None:
    layout = LayoutPlanner(panels_per_row=2, panel_px=256).plan(["a", "b", "c"])
    assert all(c.width == 256 and c.height == 256 for c in layout.cells)
</｜｜DSML｜｜ parameter>
</｜｜DSML｜｜ invoke>
</｜｜DSML｜｜ calls>