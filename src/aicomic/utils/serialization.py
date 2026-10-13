"""Safe serialization for project files. JSON only — never pickle."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ProjectFileError(ValueError):
    pass


def dump_project(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_project(path: Path) -> dict[str, Any]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise ProjectFileError(f"bad project file: {exc}") from exc
    if not isinstance(raw, dict):
        raise ProjectFileError("project root must be an object")
    return raw