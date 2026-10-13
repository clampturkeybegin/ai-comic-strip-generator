"""Registry mapping style keys to renderer classes.

Lets plugins drop in a new renderer without touching the engine.
"""
from __future__ import annotations

from aicomic.services.renderers.base import BaseRenderer
from aicomic.services.renderers.diffusion import DiffusionRenderer

_REGISTRY: dict[str, type[BaseRenderer]] = {
    "diffusion": DiffusionRenderer,
}


def register(key: str, cls: type[BaseRenderer]) -> None:
    _REGISTRY[key] = cls


def get_renderer(key: str) -> type[BaseRenderer]:
    return _REGISTRY.get(key, DiffusionRenderer)


def available() -> list[str]:
    return sorted(_REGISTRY.keys())