class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def remove(self, book):
        self.books.remove(book)

    def __contains__(self, book):
        return book in self.books
