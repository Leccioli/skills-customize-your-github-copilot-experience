"""Starter code for the FastAPI REST APIs assignment.

Run locally:
    pip install fastapi uvicorn
    uvicorn starter-code:app --reload
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    author: str = Field(..., min_length=1, max_length=80)
    year: int = Field(..., ge=1450, le=2100)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=120)
    author: Optional[str] = Field(default=None, min_length=1, max_length=80)
    year: Optional[int] = Field(default=None, ge=1450, le=2100)


class Book(BookBase):
    id: int


books = [
    Book(id=1, title="1984", author="George Orwell", year=1949),
    Book(id=2, title="The Pragmatic Programmer", author="Andrew Hunt", year=1999),
]


def next_id() -> int:
    if not books:
        return 1
    return max(book.id for book in books) + 1


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Books API is running"}


@app.get("/books", response_model=list[Book])
def list_books(author: Optional[str] = None, year: Optional[int] = None) -> list[Book]:
    result = books
    if author:
        result = [book for book in result if book.author.lower() == author.lower()]
    if year is not None:
        result = [book for book in result if book.year == year]
    return result


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book, status_code=201)
def create_book(payload: BookCreate) -> Book:
    book = Book(id=next_id(), **payload.model_dump())
    books.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, payload: BookUpdate) -> Book:
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_data = book.model_dump()
            incoming = payload.model_dump(exclude_none=True)
            updated_data.update(incoming)
            updated = Book(**updated_data)
            books[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int) -> None:
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=404, detail="Book not found")
