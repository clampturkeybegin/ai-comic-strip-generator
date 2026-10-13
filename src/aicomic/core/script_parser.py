"""Parse a plain-text comic script into title + panel prompts.

Format:
    # Title
    panel: wide shot of a rain-soaked alley
    panel: close-up on the detective's face
"""
from __future__ import annotations

from dataclasses import dataclass


class ScriptError(ValueError):
    pass


@dataclass(frozen=True)
class ParsedScript:
    title: str
    panels: list[str]


class ScriptParser:
    def parse(self, text: str) -> ParsedScript:
        title = "Untitled Strip"
        panels: list[str] = []
        for raw in text.splitlines():
            line = raw.strip()
            if not line:
                continue
            if line.startswith("#"):
                title = line.lstrip("#").strip() or title
            elif line.lower().startswith("panel:"):
                prompt = line.split(":", 1)[1].strip()
                if prompt:
                    panels.append(prompt)
        if not panels:
            raise ScriptError("script has no panels")
        return ParsedScript(title=title, panels=panels)