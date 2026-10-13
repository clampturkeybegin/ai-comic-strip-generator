"""Style presets — prompt fragments and post-processing hints per art style."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StylePreset:
    key: str
    prompt_prefix: str
    negative: str
    line_weight: int


STYLES: dict[str, StylePreset] = {
    "manga-ink": StylePreset(
        key="manga-ink",
        prompt_prefix="black and white manga panel, screentone shading, bold ink lines,",
        negative="color, photorealistic, blurry",
        line_weight=3,
    ),
    "euro-clean": StylePreset(
        key="euro-clean",
        prompt_prefix="ligne claire european comic, flat color, clean outlines,",
        negative="gritty, noise, sketch",
        line_weight=2,
    ),
    "pulp-print": StylePreset(
        key="pulp-print",
        prompt_prefix="1960s pulp comic print, halftone dots, limited palette,",
        negative="digital, smooth gradient",
        line_weight=4,
    ),
}


def get_style(key: str) -> StylePreset:
    return STYLES.get(key, STYLES["manga-ink"])