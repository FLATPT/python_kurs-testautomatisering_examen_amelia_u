
class Book:
    def __init__(self, book_id, author, title):
        self.id = book_id
        self.author = author
        self.title = title
        self.favorite = False


class BookStore:

    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        return book

    def toggleFavorite(self, book_id):
        for book in self.books:
            if book.id == book_id:
                book.favorite = not book.favorite
