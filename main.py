
from books import show_books, save_books, load_books
import os
from dotenv import load_dotenv

load_dotenv()
name = input("please enter your name: ")
print("welcome", name)

admin_mode = input("do you want to open admin mode? yes/no: ")


if admin_mode.lower() == "yes":
    password = input("enter admin password: ")

    if password == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")
        
books = load_books()
count = int(input("how many books do you want? "))
for i in range(count):
    book = input("plaese enter a book`s name: ")
    books.append(book)

show_books(books)
save_books(books)
