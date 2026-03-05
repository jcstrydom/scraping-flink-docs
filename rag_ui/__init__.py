"""Standalone UI package for interacting with RAG backends."""

from .app import create_app
from .backend import RAGBackend, BackendQueryResult
from .adapters import NaiveKGRAGBackend
from .main import app

__all__ = ["create_app", "RAGBackend", "BackendQueryResult", "NaiveKGRAGBackend", "app"]
