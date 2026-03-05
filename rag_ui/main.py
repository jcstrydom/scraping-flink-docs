from __future__ import annotations

from .adapters import NaiveKGRAGBackend
from .app import create_app


app = create_app(lambda: NaiveKGRAGBackend())
