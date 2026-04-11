from utlis import books, issued_books, normalize_book_name


def return_books():
    if len(issued_books) == 0:
        print("No books are currently issued.")
        return

    book_name = normalize_book_name(input("Enter the name of the book to return: "))

    if not book_name:
        print("Book name cannot be empty.")
        return

    if book_name in issued_books:
        issued_books.remove(book_name)
        books.append(book_name)
        print(f"Book - {book_name} returned successfully.")
    else:
        print(f"Book - {book_name} was not issued from this library.")
