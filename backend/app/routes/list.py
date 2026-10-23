"""GET /api/books (with ?status=) and GET /api/books/stats. Owned by the List/filter agent (see CONTRACT.md)."""

from fastapi import APIRouter

router = APIRouter()
