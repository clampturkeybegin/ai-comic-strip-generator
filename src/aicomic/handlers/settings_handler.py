"""Handler for persisting and applying settings changes."""
from __future__ import annotations

from aicomic.config.settings import AppSettings


class SettingsHandler:
    def __init__(self, settings: AppSettings) -> None:
        self._settings = settings

    @property
    def settings(self) -> AppSettings:
        return self._settings

    def update(self, **fields: object) -> AppSettings:
        self._settings = self._settings.model_copy(update=fields)
        self._settings.save()
        return self._settings

    def reset(self) -> AppSettings:
        self._settings = AppSettings()
        self._settings.save()
        return self._settings