# Dictionary to store book details
library_books = {}

# Function to add a book
def add_book(isbn, title, author, publisher, volume, year, subject):
    library_books[isbn] = {
        'title': title,
        'author': author,
        'publisher': publisher,
        'volume': volume,
        'year': year,
        'subject': subject
    }

# Function to remove a book
def remove_book(isbn):
    if isbn in library_books:
        del library_books[isbn]
    else:
        print(f"No book found with ISBN: {isbn}")

# Function to get book details
def get_book_details(isbn):
    return library_books.get(isbn, "No book found with that ISBN")

# Example data collection (information for 25 books)
book_data = [
    {"isbn": "9781234567891", "title": "Operating Systems Concepts", "author": "Silberschatz", "publisher": "Wiley", "volume": 10, "year": 2021, "subject": "Operating Systems"},
    {"isbn": "9781234567892", "title": "Modern Operating Systems", "author": "Tanenbaum", "publisher": "Pearson", "volume": 4, "year": 2020, "subject": "Operating Systems"},
    {"isbn": "9781234567893", "title": "Data Structures and Algorithms in Python", "author": "Goodrich", "publisher": "Wiley", "volume": 1, "year": 2021, "subject": "Data Structures"},
    # Add more books here...
]

# Adding the collected book data to the library
for book in book_data:
    add_book(book['isbn'], book['title'], book['author'], book['publisher'], book['volume'], book['year'], book['subject'])
