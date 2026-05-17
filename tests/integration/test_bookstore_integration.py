import pytest

from src.laslistan.bookstore import BookStore, Book
from src.laslistan.favorite_books import FavoriteBooks

pytestmark = pytest.mark.integration

def test__bookstore__toggleFavorite__adds_book_to_favorite_books():
    bookstore = BookStore()
    favorite_books = FavoriteBooks()
    book = Book(1, "Roberta Flakyton", "Mocking Me Softly")
    bookstore.addBook(book)
    bookstore.toggleFavorite(1)

    if book.favorite:
        favorite_books.add(book)

    assert book in favorite_books

