from Book import Book
from book_data import books_data

book_list = []

for i in books_data:
    book_title = i["title"]
    book_author = i["author"]
    book_year = i["year"]
    new_book = Book(book_title, book_author, book_year)
    book_list.append(new_book)

for i in book_list:
    i.display()
