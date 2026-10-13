"""Handler for loading/saving .aicomic script files."""
from __future__ import annotations

from pathlib import Path

from aicomic.core.script_parser import ParsedScript, ScriptParser


class ScriptHandler:
    def __init__(self, parser: ScriptParser | None = None) -> None:
        self._parser = parser or ScriptParser()

    def load(self, path: Path) -> ParsedScript:
        return self._parser.parse(path.read_text(encoding="utf-8"))

    def save(self, path: Path, script: ParsedScript) -> None:
        lines = [f"# {script.title}", ""]
        lines += [f"panel: {p}" for p in script.panels]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")