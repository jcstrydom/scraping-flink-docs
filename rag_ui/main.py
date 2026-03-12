from __future__ import annotations

from .adapters import DualRAGBackend
from .app import create_app


app = create_app(lambda: DualRAGBackend())
