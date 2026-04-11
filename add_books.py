from utlis import books, normalize_book_name


def add_books():
    book_name = normalize_book_name(input("Enter the name of the book: "))

    if not book_name:
        print("Book name cannot be empty.")
        return

    if book_name in books:
        print(f"Book - {book_name} already exists in the library.")
        return

    books.append(book_name)
    print(f"Book - {book_name} added successfully.")
