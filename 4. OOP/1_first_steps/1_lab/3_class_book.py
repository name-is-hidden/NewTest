class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(f"This is {book.name}. It's a very interesting novel, written by {book.author}. It's {book.pages} pages long.")