from services.book_service import BookService

def main():
    book_service = BookService()

    while True:
        print("\nChoose:")
        print("1. Add book")
        print("2. Delete Book")
        print("3. Search book")
        print("4. List all book")
        print("5. Change status book")
        print("6. Exit")

        choice = input(": ")

        if choice == "1":
            title = input("Enter name book: ")
            author = input("Enter autor: ")
            while True:
                try:
                    year = int(input("Enter year: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid year.")
            book_service.add_book(title, author, year)
        elif choice == "2":
            book_id = input("Enter Id book delet: ")
            book_service.remove_book(book_id)
        elif choice == "3":
            query = input("Enter number, autor or year: ")
            book_service.search_books(query)
        elif choice == "4":
            book_service.list_all_books()
        elif choice == "5":
            book_id = input("Enter ID book, for rename status: ")
            
            book_service.change_book_status(book_id)
        elif choice == "6":
            print("Exit")
            break
        else:
            print("Unccorect")

if __name__ == "__main__":
    main()
