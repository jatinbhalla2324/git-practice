"""In-memory book store. Shared by both routers; owned by the lead (see CONTRACT.md)."""

STATUSES = ("to-read", "reading", "done")

_books: list[dict] = []
_next_id = 1


def add_book(title: str, author: str, status: str) -> dict:
    global _next_id
    book = {"id": _next_id, "title": title, "author": author, "status": status}
    _books.append(book)
    _next_id += 1
    return dict(book)


def list_books(status: str | None = None) -> list[dict]:
    return [dict(b) for b in _books if status is None or b["status"] == status]


def get_book(book_id: int) -> dict | None:
    for b in _books:
        if b["id"] == book_id:
            return dict(b)
    return None


def update_status(book_id: int, status: str) -> dict | None:
    for b in _books:
        if b["id"] == book_id:
            b["status"] = status
            return dict(b)
    return None


def reset() -> None:
    """Clear all books and restart ids at 1. Used by tests."""
    global _next_id
    _books.clear()
    _next_id = 1
