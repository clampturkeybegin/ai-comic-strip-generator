"""Main window — script editor, panel preview grid, render/export buttons."""
from __future__ import annotations

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from aicomic.core.engine import StripEngine
from aicomic.handlers.render_handler import RenderHandler


class MainWindow(QMainWindow):
    def __init__(self, engine: StripEngine) -> None:
        super().__init__()
        self.setWindowTitle("AI Comic Strip Generator")
        self.resize(1280, 800)
        self._engine = engine
        self._render_handler = RenderHandler(engine, self)
        self._render_handler.finished.connect(self._on_finished)
        self._render_handler.failed.connect(self._on_failed)

        central = QWidget(self)
        layout = QVBoxLayout(central)
        layout.addWidget(self._build_toolbar())
        self.setCentralWidget(central)

    def _build_toolbar(self) -> QWidget:
        from PySide6.QtWidgets import QPushButton

        btn = QPushButton("Render Strip", self)
        btn.clicked.connect(self._on_render_clicked)
        return btn

    def _on_render_clicked(self) -> None:
        self._render_handler.render("Untitled Strip", ["a wide shot", "a close-up"])

    def _on_finished(self, strip: object) -> None:
        self.setWindowTitle(f"AI Comic Strip Generator — {len(strip.panels)} panels")  # type: ignore[attr-defined]

    def _on_failed(self, message: str) -> None:
        self.statusBar().showMessage(f"render failed: {message}", 8000)


def launch(engine: StripEngine) -> int:
    app = QApplication.instance() or QApplication([])
    win = MainWindow(engine)
    win.show()
    return app.exec()