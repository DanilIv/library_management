class Library:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def add_book(self, book):
        self.book_repository.save_book(book)

    def remove_book(self, book_id):
        self.book_repository.delete_book(book_id)

    def search_books(self, query):
        return self.book_repository.search_books(query)

    def list_all_books(self):
        return self.book_repository.get_all_books()

    def change_book_status(self, book_id):
        book = self.book_repository.get_book_by_id(book_id)
        if book:
            if book.status:
                book.status = False
            else:
                book.status = True
            
            
        else:
            raise ValueError(f"Book with ID '{book_id}' not found.")
