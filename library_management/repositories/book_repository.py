import json
from models.book import Book
from utils.file_utils import read_json, write_json

class BookRepository:
    def __init__(self, file_path="books.json"):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self):
        try:
            return [Book(**book_data) for book_data in read_json(self.file_path)]
        except FileNotFoundError:
            return []

    def save_books(self):
        write_json(self.file_path, [book.__dict__ for book in self.books])

    def save_book(self, book):
        self.books.append(book)
        self.save_books()

    def delete_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save_books()
                return
        raise ValueError(f"Book with ID '{book_id}' not found.")

    def search_books(self, query):
        
        return [book for book in self.books if query.lower() in book.title.lower() or
                query.lower() in book.author.lower() or str(book.year) == query]

    def get_all_books(self):
        return self.books

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    

