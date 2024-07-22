from models.library import Library
from repositories.book_repository import BookRepository
from models.book import Book
from utils.uuid_utils import generate_uuid


class BookService:
    def __init__(self):
        self.book_repository = BookRepository()
        self.library = Library(self.book_repository)

    def add_book(self, title, author, year):
        book_id = generate_uuid(8)
        while self.book_repository.get_book_by_id(book_id)!=None:
            book_id = generate_uuid(8)
        book = Book(book_id,title, author, year)
        self.library.add_book(book)
        print(f"Book '{book.title}' add in library.")

    def remove_book(self, book_id):
        try:
            self.library.remove_book(book_id)
        except ValueError as e:
            print(e)

    def search_books(self, query):
        results = self.library.search_books(query)
        if results:
            for book in results:
                print(f"ID: {book.id}, name: {book.title}, autor: {book.author}, year: {book.year}, status: {book.status}")
        else:
            print("Not found")

    def list_all_books(self):
        for book in self.library.list_all_books():
            print(f"ID: {book.id}, name: {book.title}, autor: {book.author}, year: {book.year}, status: {book.status}")

    def change_book_status(self, book_id):
        try:
            self.library.change_book_status(book_id)
        except ValueError as e:
            print(e)
