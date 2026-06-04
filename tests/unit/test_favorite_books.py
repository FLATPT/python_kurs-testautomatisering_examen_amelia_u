import pytest

from src.laslistan.bookstore import Book
from src.laslistan.favorite_books import FavoriteBooks

pytestmark = pytest.mark.unit


def test__favorite_books__add():
    favorite_books = FavoriteBooks()
    book = (1, "Roberta Flakyton", "Mocking Me Softly")
    favorite_books.add(book)

    assert book in favorite_books


def test__favorite_books__remove():
    favorite_books = FavoriteBooks()
    book = Book(1, "Roberta Flakyton", "Mocking Me Softly")
    favorite_books.add(book)
    favorite_books.remove(book)

    assert book not in favorite_books


def test__favorite_books__remove__only_removes_favorite_book():
    favorite_books = FavoriteBooks()
    book1 = Book(1, "Roberta Flakyton", "Mocking Me Softly")
    book2 = Book(2, "Linus Torvalds", "Git Blame and Other Ways to Lose Friends")
    favorite_books.add(book1)
    favorite_books.add(book2)
    favorite_books.remove(book1)

    assert book1 not in favorite_books
    assert book2 in favorite_books
