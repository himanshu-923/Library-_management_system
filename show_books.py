from utlis import books

def show_books():
    if len(books) == 0:
        print("No books available in the library.")
    else:
        print("Books available in the library:")
        for _ in books:
            print(f"- {_}")