    books = load_books()
    count = int(input("how many books do you want? "))
    for i in range(count):
        book = input("plaese enter a book`s name: ")
        books.append(book)
