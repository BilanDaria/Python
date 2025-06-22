class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def borrow_book(self, book_title):
        book = next((b for b in self.book_list if b.title == book_title.lower()), None)
        if book is None:
            print(f"Unfortunately we don't have {book_title} in our Library")
            return
        if not book.available:
            print(f"{book_title} was taken by another person.")
            return

        print("You may borrow this book. It's available for now")
        answer = input("Do you want to get this book?: ").lower()
        if answer == "yes":
            book.available = False
            print("You can take it on reception.")
            print(f"Your book:\n{book}")
        elif answer == 'no':
            print("Request canceled!")
        else:
            print("Unacceptable answer! Request canceled...")

    def return_book(self, book_title):
        book = next((b for b in self.book_list if b.title == book_title.lower()), None)
        if not book.available:
            book.available = True
            print(f"Thanks for returning the {book_title}. We hope you enjoyed reading.")
        else:
            print("We already have this book in our Library. Please contact our librarian!")

    def __str__(self):
        return '\n'.join(str(i) for i in self.book_list)
