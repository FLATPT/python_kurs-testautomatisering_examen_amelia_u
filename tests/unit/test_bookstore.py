import pytest
from src.laslistan.bookstore import BookStore, Book

pytestmark = pytest.mark.unit

# Lägg till boklista Funny_Books i BookStore
FUNNY_BOOKS = [
    {"id": 100, "title": "Ormar på ett plan: En Python-berättelse", "author": "Guido van Rossum"},
    {"id": 102, "title": "The Pragmatic Procrastinator",            "author": "Dave Thomasson"},
    {"id": 103, "title": "Python för folk som hatar ormar",         "author": "Monty Pythonsson"},
    {"id": 104, "title": "Why Your Tests Are Lying to You",         "author": "Kent Backdoor"},
    {"id": 105, "title": "Playwright: Click It Till You Make It",   "author": "Microslop Browserdóttir"},
    {"id": 107, "title": "Git Blame and Other Ways to Lose Friends", "author": "Linus Torvalds"},
    {"id": 108, "title": "Learn Python in 21 Years",                "author": "Sams Teachyourself"},
    {"id": 109, "title": "Agile Is a Feeling",                      "author": "Jeff Sutherland"},
    {"id": 110, "title": "Playwright: Waiting for Selectors",       "author": "Samuel Barclay Beckett"},
    {"id": 111, "title": "Stack Overflow: A Love Story",            "author": "Copy Pasta"},
    {"id": 112, "title": "My First Regex (And Last)",               "author": "Larry Wallström"},
    {"id": 113, "title": "The Developer Who Knew Nothing",          "author": "George R.R. Martin"},
    {"id": 115, "title": "The Bugs are Coming",                     "author": "George R.R. Martin"},
]


def test__bookstore__addBook():
    book = Book(1, "Roberta Flakyton", "Mocking Me Softly")
    bookstore = BookStore()
    bookstore.addBook(book)

    assert len(bookstore.books) == 1


def test__bookstore__addBook__all__books_from_funny__books_list():
    bookstore = BookStore()

    for book in FUNNY_BOOKS:
        bookstore.addBook(Book(book["id"], book["author"], book["title"]))

    assert len(bookstore.books) == len(FUNNY_BOOKS)


def test__bookstore__toggleFavorite__marks_book_as_favorite():
    book = Book(1, "Roberta Flakyton", "Mocking Me Softly")
    bookstore = BookStore()
    bookstore.addBook(book)
    bookstore.toggleFavorite(1)

    assert bookstore.books[0].favorite   # Kontrollera att boken är markerad som favorit


def test__bookstore__toggleFavorite__unmarks_book_as_favorite():
    book = Book(105, "Microslop Browserdóttir", "Playwright: Click It Till You Make It")
    bookstore = BookStore()
    bookstore.addBook(book)
    bookstore.toggleFavorite(105)   # Första gången, markerar som favorit
    bookstore.toggleFavorite(105)   # Andra gången, avmarkerar som favorit

    assert not bookstore.books[0].favorite    # Kontrollera att boken inte längre är favorit
    assert bookstore.books[0].id == 105       # Kontrollera att det är rätt bok som avmarkerats som favorit


def test__bookstore__toggleFavorite__only_marks_selected_book_as_favorite():
    book1 = Book(1, "Roberta Flakyton", "Mocking Me Softly")
    book2 = Book(105, "Microslop Browserdóttir", "Playwright: Click It Till You Make It")
    bookstore = BookStore()
    bookstore.addBook(book1)
    bookstore.addBook(book2)
    bookstore.toggleFavorite(105)

    assert not bookstore.books[0].favorite
    assert bookstore.books[1].favorite
