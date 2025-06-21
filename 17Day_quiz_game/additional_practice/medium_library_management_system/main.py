from Book import Book
from Library import Library
from book_data import books_data

books = []

for i in books_data:
    new_book = Book(**i)
    books.append(new_book)

library = Library(books)

# print(library)
library.borrow_book("Don Quixote")

# for i in books:
#     print(i)
