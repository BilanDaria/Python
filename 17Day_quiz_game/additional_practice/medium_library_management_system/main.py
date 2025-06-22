from Book import Book
from Library import Library
from book_data import books_data

books = []

for i in books_data:
    new_book = Book(**i)
    books.append(new_book)

library = Library(books)

options = {
    '1': library.borrow_book,
    '2': library.return_book,
}

while True:
    option = input("1. Borrow a book.\n"
                   "2. Return a book.\n"
                   "3. List of all books.\n"
                   "4. Shutdown.\n"
                   "What would you like to do: ")
    if option in options:
        book_title = input("Please, input a book title: ")
        options[option](book_title)
    elif option == "3":
        print(library)
    elif option == "4":
        print("Shutdown the system. Thanks for using our program. See you!")
        break
    else:
        print("Unsupported action. Try one more time")
        continue
