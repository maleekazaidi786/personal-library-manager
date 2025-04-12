import json
import os

library_file = "library.txt"
library = []

# Load library from file (if exists)
if os.path.exists(library_file):
    with open(library_file, "r") as f:
        library = json.load(f)

def save_library():
    with open(library_file, "w") as f:
        json.dump(library, f)

def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found!")

def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the search keyword: ").lower()
    matches = []

    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or \
           (choice == "2" and keyword in book["author"].lower()):
            matches.append(book)

    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("❌ No matching books found!")

def display_all_books():
    if not library:
        print("Your library is empty!")
        return
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_statistics():
    total = len(library)
    if total == 0:
        print("Library is empty!")
        return
    read_count = sum(1 for book in library if book["read"])
    percent_read = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_all_books()
    elif choice == "5":
        display_statistics()
    elif choice == "6":
        save_library()
        print("Library saved to file. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")