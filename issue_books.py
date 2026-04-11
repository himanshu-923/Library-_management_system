from utlis import books, issued_books

def issue_books():
    if len(books) == 0:
        print("No books available in the library to issue.")
    else:
        book_name = input("Enter the name of the book to issue: ").strip().upper()
        if book_name in books:
            books.remove(book_name)
            issued_books.append(book_name)
            print(f"Book - {book_name} issued successfully.")
        else:
            print(f"Book - {book_name} is not available in the library.")