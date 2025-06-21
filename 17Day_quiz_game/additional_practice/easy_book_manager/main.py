from Book import Book
from book_data import books_data

book_list = []

for i in books_data:
    new_book = Book(**i)
    book_list.append(new_book)

for i in book_list:
    print(i)
