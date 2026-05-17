import pytest
from src.laslistan.book_store import BookStore

pytestmark = pytest.mark.unit

def test__book_store__add_book():
    book_store = BookStore()
    book_store.add_book("Roberta Flakyton", "Mocking Me Softly")

    assert book_store.books == ["Roberta Flakyton", "Mocking Me Softly"]


def test__book_store__remove_book():

