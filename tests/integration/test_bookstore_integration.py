import pytest

from src.laslistan.bookstore import BookStore, Book
from src.laslistan.favorite_books import FavoriteBooks

pytestmark = pytest.mark.integration


def test__bookstore__toggleFavorite__adds_book_to_favorite_books(mocker):
    bookstore = BookStore()
    favorite_books = FavoriteBooks()
    book = Book(1, "Roberta Flakyton", "Mocking Me Softly")

    add_book_spy = mocker.spy(bookstore, "addBook")
    add_favorite_spy = mocker.spy(favorite_books, "add")

    bookstore.addBook(book)
    add_book_spy.assert_called_once()
    bookstore.toggleFavorite(1)

    if book.favorite:
        favorite_books.add(book)
    add_favorite_spy.assert_called_once_with(book)

    assert book in favorite_books
