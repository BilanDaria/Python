class Library:
    def __init__(self, book_list):
        self.book_list = book_list

    def borrow_book(self, book_title):
        for i in self.book_list:
            if i.title == book_title:
                if i.available:
                    print("You may borrow this book. It's available for now")
                    answer = input("Do you want to get this book?: ").lower()
                    if answer == "yes":
                        self.book_list[book_title].available = False
                        print("Ok. Take it on reception, please.")
                    elif answer == 'no':
                        print("Request canceled!")
                    else:
                        print("Unacceptable answer! Request canceled...")
            else:
                print(f"Unfortunately, we don't have {book_title} in our Library.")

    def __str__(self):
        return '\n'.join(str(i) for i in self.book_list)
