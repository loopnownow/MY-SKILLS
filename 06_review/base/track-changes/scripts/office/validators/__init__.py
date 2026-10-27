"""
Validation modules for Word tracked-change handling.

PPTX validation was removed 2026-10-27: the lab never touches `.pptx`, and the
upstream validator was 275 lines of dead weight.
"""

from .base import BaseSchemaValidator
from .docx import DOCXSchemaValidator
from .redlining import RedliningValidator

__all__ = [
    "BaseSchemaValidator",
    "DOCXSchemaValidator",
    "RedliningValidator",
]
