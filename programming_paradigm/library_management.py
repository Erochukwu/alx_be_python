class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not bool.is_checked_out():
                book.check_out()
                print(f"Checked out: '{book.title}'")
                return
        print(f"No available copy of '{title}' to check out.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_checked_out():
                book.check_in()
                print(f"Returned: '{book.title}'")
                return          
        print(f"No checked-out copy of '{title}' found.")

    def list_available_books(self):
        available_book = [book for book in self._books if not book.is_checked_out()]
        if not available_books:
            print("No books available.")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
                    