class Book:
    def __init__(self, title, author, year, available):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year of publishing: {self.year}\n"
                f"Available: {self.available}\n"
                f"")
