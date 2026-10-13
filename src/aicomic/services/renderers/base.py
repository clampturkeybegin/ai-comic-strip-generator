"""BaseRenderer — interface every panel renderer implements."""
from __future__ import annotations

from abc import ABC, abstractmethod

from PIL import Image


class BaseRenderer(ABC):
    @abstractmethod
    def render(
        self,
        prompt: str,
        width: int,
        height: int,
        seed: int,
    ) -> Image.Image:
        """Return a single panel image. Must not raise on empty prompt."""
        raise NotImplementedError