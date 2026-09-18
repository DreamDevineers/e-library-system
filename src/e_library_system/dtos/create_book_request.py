from pydantic import BaseModel

from e_library_system.models.book import BookCategory, BookStatus


class CreateBookRequest(BaseModel):
    title: str
    author: str
    category: BookCategory
    status: BookStatus
    year: int