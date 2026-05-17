import pytest

from src.laslistan.bookstore import BookStore, Book
from src.laslistan.favorite_books import FavoriteBooks

pytestmark = pytest.mark.integration

def test__favorite_books__add_book_exists_in_bookstore():
    bookstore = BookStore()
    favorite_books = FavoriteBooks()
    book = Book(1, "Roberta Flakyton", "Mocking Me Softly")
    bookstore.addBook(book)
    favorite_books.add(book)

    assert book in bookstore.books
    assert book in favorite_books


