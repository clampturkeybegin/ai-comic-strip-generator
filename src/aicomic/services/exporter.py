"""StripExporter — writes a ComicStrip to PNG panels + a stitched sheet."""
from __future__ import annotations

import logging
from pathlib import Path

from PIL import Image

from aicomic.models.strip import ComicStrip

log = logging.getLogger(__name__)


class StripExporter:
    def export(self, strip: ComicStrip, out_dir: Path) -> list[Path]:
        out_dir.mkdir(parents=True, exist_ok=True)
        written: list[Path] = []
        for i, panel in enumerate(strip.panels):
            path = out_dir / f"panel_{i:03d}.png"
            panel.image.save(path)
            written.append(path)
        sheet = self._stitch(strip)
        sheet_path = out_dir / "strip.png"
        sheet.save(sheet_path)
        written.append(sheet_path)
        log.info("exported %d files to %s", len(written), out_dir)
        return written

    def _stitch(self, strip: ComicStrip) -> Image.Image:
        if not strip.panels:
            raise ValueError("cannot stitch an empty strip")
        cols = strip.cols
        rows = (len(strip.panels) + cols - 1) // cols
        pw = max(p.image.width for p in strip.panels)
        ph = max(p.image.height for p in strip.panels)
        gutter = 12
        sheet = Image.new(
            "RGB",
            (cols * pw + (cols + 1) * gutter, rows * ph + (rows + 1) * gutter),
            "white",
        )
        for i, panel in enumerate(strip.panels):
            r, c = divmod(i, cols)
            x = gutter + c * (pw + gutter)
            y = gutter + r * (ph + gutter)
            sheet.paste(panel.image, (x, y))
        return sheet