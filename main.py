from add_books import add_books
from show_books import show_books
from issue_books import issue_books
from return_books import return_books


def library():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Books")
        print("2. Show Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if not choice.isdigit():
            print("Invalid choice !!! Please enter a number from 1 to 5.")
            continue

        choice = int(choice)

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank you")
            break
        else:
            print("Invalid choice !!!")


if __name__ == "__main__":
    library()
