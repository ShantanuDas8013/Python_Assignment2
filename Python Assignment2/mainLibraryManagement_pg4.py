import LibraryBooks

def main():
    # Display menu options
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Get Book Details")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Add book
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            publisher = input("Enter publisher: ")
            volume = input("Enter volume: ")
            year = int(input("Enter year of publication: "))
            subject = input("Enter subject: ")
            LibraryBooks.add_book(isbn, title, author, publisher, volume, year, subject)
            print("Book added successfully.")

        elif choice == '2':
            # Remove book
            isbn = input("Enter ISBN of the book to remove: ")
            LibraryBooks.remove_book(isbn)
            print("Book removed successfully.")

        elif choice == '3':
            # Get book details
            isbn = input("Enter ISBN: ")
            book_details = LibraryBooks.get_book_details(isbn)
            print("Book Details:", book_details)
            print("Book details have been fetched successfully.")

        elif choice == '4':
            # Exit the program
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
