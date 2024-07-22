import unittest
from utils.uuid_utils import generate_uuid
from models.book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        # Test creating a new book
        book_id = generate_uuid(8)
        book = Book(book_id, "������ ��������", 1925)
        self.assertEqual(book.id, book_id)
        self.assertEqual(book.title, "������������ � ���������")
        self.assertEqual(book.author, "������ ��������")
        self.assertEqual(book.year, 1925)
        self.assertTrue(book.status)

    def test_book_status(self):
        # Test setting the book status
        book_id = generate_uuid(8)
        book = Book(book_id, "������ ��������", "������ � ���������", 1960, False)
        self.assertFalse(book.status)
        book.status = True
        self.assertTrue(book.status)

if __name__ == '__main__':
    unittest.main()