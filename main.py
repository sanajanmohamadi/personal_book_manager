name = input("enter your name: ")
print("Welcome", name)
book = input("enter a book name: ")
print("the book name is", book)


books = load_books()
count = int(input("how many book do you want to add?: "))

for i in range(count):
    taskbook = input("enter a book name: ")
    books.append(book)
