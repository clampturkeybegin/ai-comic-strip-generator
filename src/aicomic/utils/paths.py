"""Path helpers — app data dirs, cache, weights."""
from __future__ import annotations

import os
from pathlib import Path


def app_data_dir() -> Path:
    base = os.environ.get("AICOMIC_HOME")
    if base:
        return Path(base)
    return Path.home() / ".aicomic"


def cache_dir() -> Path:
    d = app_data_dir() / "cache"
    d.mkdir(parents=True, exist_ok=True)
    return d


def weights_dir() -> Path:
    d = app_data_dir() / "weights"
    d.mkdir(parents=True, exist_ok=True)
    return d