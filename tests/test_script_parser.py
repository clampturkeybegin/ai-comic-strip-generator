"""Tests for ScriptParser."""
from __future__ import annotations

import pytest

from aicomic.core.script_parser import ScriptError, ScriptParser


def test_parses_title_and_panels() -> None:
    text = "# The Long Goodbye\npanel: rainy alley\npanel: close-up on eyes\n"
    parsed = ScriptParser().parse(text)
    assert parsed.title == "The Long Goodbye"
    assert parsed.panels == ["rainy alley", "close-up on eyes"]


def test_empty_script_raises() -> None:
    with pytest.raises(ScriptError):
        ScriptParser().parse("# only a title\n")


def test_blank_panel_lines_ignored() -> None:
    text = "panel:\npanel: real beat\n"
    parsed = ScriptParser().parse(text)
    assert parsed.panels == ["real beat"]