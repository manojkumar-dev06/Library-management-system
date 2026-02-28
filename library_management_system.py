# Library Management System
# Developed by T Manoj Kumar

# List to store books
books = []

# Function to add book
def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "issued": False
    }

    books.append(book)
    print("Book added successfully.\n")

# Function to view books
def view_books():
    if len(books) == 0:
        print("No books available.\n")
        return

    print("Book List:")
    for book in books:
        status = "Issued" if book["issued"] else "Available"
        print(f'ID: {book["id"]}, Name: {book["name"]}, Author: {book["author"]}, Status: {status}')
    print()

# Function to issue book
def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:
            if book["issued"]:
                print("Book already issued.\n")
            else:
                book["issued"] = True
                print("Book issued successfully.\n")
            return

    print("Book not found.\n")

# Function to return book
def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:
            if not book["issued"]:
                print("Book was not issued.\n")
            else:
                book["issued"] = False
                print("Book returned successfully.\n")
            return

    print("Book not found.\n")

# Main menu
while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you for using Library Management System.")
        break
    else:
        print("Invalid choice. Try again.\n")
