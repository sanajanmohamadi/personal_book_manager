from books import show_book


name = input("enter your name: ")
print("Welcome", name)

books = []
count = int(input("how many books do you want to add?: "))

for i in range(count):
    book = input("enter a book: ")
    books.append(book)
show_book()