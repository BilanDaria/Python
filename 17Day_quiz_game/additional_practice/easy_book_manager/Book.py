class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Year of publishing: {self.year}\n"
              f"--------------------------------\n")
