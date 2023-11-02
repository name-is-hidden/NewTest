favourite_book = input()
current_book = input()

books_checked = 0
book_found = False

while current_book != "No More Books":
    if current_book == favourite_book:
        book_found = True
        break

    books_checked += 1
    current_book = input()

if book_found:
    print(f"You checked {books_checked} books and found it.")

else:
    print(f"The book you search is not here!")
    print(f"You checked {books_checked} books.")

