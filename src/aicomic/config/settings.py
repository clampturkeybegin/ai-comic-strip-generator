"""App settings — pydantic model persisted to JSON under app data."""
from __future__ import annotations

import json
from pathlib import Path

from pydantic import BaseModel, Field

from aicomic.utils.paths import app_data_dir


class AppSettings(BaseModel):
    device: str = Field(default="cuda", description="cuda | cpu | mps")
    weights_dir: Path = Field(default_factory=lambda: app_data_dir() / "weights")
    tile_size: int = Field(default=768, ge=256, le=1536)
    default_style: str = "manga-ink"
    panels_per_row: int = Field(default=3, ge=1, le=4)
    seed: int = 6767

    @classmethod
    def load(cls) -> "AppSettings":
        path = app_data_dir() / "settings.json"
        if not path.exists():
            return cls()
        return cls.model_validate(json.loads(path.read_text(encoding="utf-8")))

    def save(self) -> None:
        path = app_data_dir() / "settings.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.model_dump_json(indent=2), encoding="utf-8")