"""DiffusionRenderer — thin adapter over ModelRunner for the registry."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

from aicomic.services.model_runner import ModelRunner
from aicomic.services.renderers.base import BaseRenderer


class DiffusionRenderer(BaseRenderer):
    def __init__(self, weights_dir: Path, device: str = "cuda") -> None:
        self._runner = ModelRunner(weights_dir=weights_dir, device=device)

    def render(self, prompt: str, width: int, height: int, seed: int) -> Image.Image:
        return self._runner.render_panel(
            prompt=prompt,
            style="manga-ink",
            width=width,
            height=height,
            seed=seed,
        )