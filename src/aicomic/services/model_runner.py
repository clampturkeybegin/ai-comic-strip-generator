"""ModelRunner — wraps a diffusers pipeline for single-panel generation.

Loads one checkpoint, keeps it warm, renders panels serially.
Not thread-safe: call from a single worker thread.
"""
from __future__ import annotations

import logging
from pathlib import Path

from PIL import Image

log = logging.getLogger(__name__)


class ModelRunner:
    def __init__(self, weights_dir: Path, device: str = "cuda", tile_size: int = 768) -> None:
        self._weights_dir = weights_dir
        self._device = device
        self._tile_size = tile_size
        self._pipeline = None

    def _ensure_pipeline(self) -> None:
        if self._pipeline is not None:
            return
        # Lazy import so headless CI without torch installed can still import.
        from diffusers import StableDiffusionPipeline  # type: ignore

        ckpt = self._weights_dir / "comic-base"
        log.info("loading checkpoint from %s on %s", ckpt, self._device)
        self._pipeline = StableDiffusionPipeline.from_pretrained(str(ckpt))
        self._pipeline = self._pipeline.to(self._device)

    def render_panel(
        self,
        prompt: str,
        style: str,
        width: int,
        height: int,
        seed: int,
    ) -> Image.Image:
        self._ensure_pipeline()
        from aicomic.config.styles import get_style

        preset = get_style(style)
        full_prompt = f"{preset.prompt_prefix} {prompt}"
        generator = None
        try:
            import torch  # type: ignore

            generator = torch.Generator(device=self._device).manual_seed(seed)
        except Exception:  # noqa: BLE001 — torch optional in some dev setups
            pass
        result = self._pipeline(  # type: ignore[misc]
            prompt=full_prompt,
            negative_prompt=preset.negative,
            width=width,
            height=height,
            generator=generator,
        )
        return result.images[0]