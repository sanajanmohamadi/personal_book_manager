from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os

load_dotenv()

name = input("What's your name? ")
print("Welcome", name)

admin_mode = input("do you want to enter admin mode? yes/no")
if admin_mode == "yes":
    admin_password = input("enter admin password: ")
    if admin_password== os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode activated")
    else:
        print("wrong password")


books = load_books()
number = int(input("How many books do you want to add? : "))

for i in range(number):
    book = input("Enter the name of the book: ")
    books.append(book)


show_books(books)
save_books(books)