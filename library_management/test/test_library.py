import unittest
from unittest.mock import MagicMock
from models.book import Book
from models.library import Library
from utils.uuid_utils import generate_uuid

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.book_repository = MagicMock()
        self.library = Library(self.book_repository)

    def test_add_book(self):
        book_id = generate_uuid(8)
        book = Book(book_id,title="Test Book", author="Test Author", year=1960)
        self.library.add_book(book)
        self.book_repository.save_book.assert_called_with(book)

    def test_remove_book(self):
        self.library.remove_book(1)
        self.book_repository.delete_book.assert_called_with(1)

    def test_search_books(self):
        self.book_repository.search_books.return_value = [Book(generate_uuid(8),title="Test Book", author="Test Author", year=1960)]
        result = self.library.search_books("test")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Test Book")
        self.assertEqual(result[0].author, "Test Author")
        self.assertTrue(result[0].status)

    def test_list_all_books(self):
        self.book_repository.get_all_books.return_value = [
            
           Book(generate_uuid(8),title="Book 1", author="Author 1", year=1960),
           Book(generate_uuid(8),title="Book 2", author="Author 2", year=1960)
        ]
        books = self.library.list_all_books()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Book 1")
        self.assertEqual(books[0].author, "Author 1")
        self.assertTrue(books[0].status)
        self.assertEqual(books[1].title, "Book 2")
        self.assertEqual(books[1].author, "Author 2")
        self.assertTrue(books[1].status)

    def test_change_book_status(self):
        book_id = generate_uuid(8)
        book = Book(book_id,title="Test Book", author="Test Author", year=1960)
        self.book_repository.get_book_by_id.return_value = book
        self.library.change_book_status(1)
        self.assertFalse(book.status)

        self.book_repository.get_book_by_id.return_value = None
        with self.assertRaises(ValueError):
            self.library.change_book_status(2)

if __name__ == "__main__":
    unittest.main()
