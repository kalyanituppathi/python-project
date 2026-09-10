from abc import ABC,abstractmethod
from datetime import datetime,timedelta
import json
#data structure
library_books=[]
#abstarction
class libraryitem(ABC):
    @abstractmethod
    def display(self):
        pass
#encapsulation +constructor+inheritance
class Book(libraryitem):#inheritance
   def __init__(self,book_id,title,author,copies,cost):#constructor with parametes
        self.book_id=book_id
        self.title=title
        self.author=author
        self.__copies=copies#encapsulation (private class)
        self.cost=cost
        self.issue_date=None
        self.return_date=None
   def get_copies(self):#methpod
       return self.__copies
   def set_copies(self,copies):
       self.__copies=copies
   def display(self):
        print("******************************")
        print("bookid :",self.book_id)
        print("title :",self.title)
        print("author :",self.author)
        print("book cost :",self.cost)
        print("copies :",self.get_copies())
        print("*****************************")
#parent calss
class Member:
    def __init__(self,name):  #constructor
        self.name=name
    def member_type(self):
        pass
#inheritance
class studentmember(Member):
    def member_type(self):
        return "student member"
class adminmember(Member):
    def member_type(self):
        return "admin member"
#polymorphism
def show_member(Member):
    print("member type:",Member.member_type())
#function:add book+exception handling
def add_book():
    try:
        book_id=int(input("enter book id"))
        title=input("enter book title:")
        author=input("enter author name:")
        copies=int(input("enter no.of copies:"))
        cost=int(input("enter book cost:"))
        book=Book(book_id,title,author,copies,cost)
        library_books.append(book)
        print("\nbook added successfully")
    except ValueError:
        print("Invalid input !please enter correct data")
#function:view books
def view_books():
    if len(library_books)==0:
        print("\n No books available")
    else:
        for book in library_books:
            book.display()
#function :search book
def search_book():
    title=input("enter book title:")
    found=False
    for book in library_books:
        if book.title.lower()==title.lower():
            book.display()
            found=True
    if not found:
        print("book not found")
#function:return book+fine calculation
def issue_book():
    title = input("Enter Book Title To Issue: ")

    for book in library_books:
        if book.title.lower() == title.lower():

            if book.get_copies() > 0:
                book.set_copies(book.get_copies() - 1)
                book.issue_date = datetime.now()

                print("Book Issued Successfully")
            else:
                print("Book Not Available")

            return

    print("Book Not Found")
def return_book():
    title=input("enter book title to return:")
    for book in library_books:
        if book.title.lower()==title.lower():
            if book.issue_date is None:
                print("book was not issued")
                return
            book.return_date=datetime.now()
            days_used=(book.return_date-book.issue_date).days
            fine=0
            if days_used>7:
                fine=book.cost*2
            book.set_copies(book.get_copies()+1)
            print("book returned successfully")
            print("issue date:",book.issue_date.strftime("%d-%m-%y"))
            print("dats used :",days_used)
            print("fine amout:",fine)
            return
    print("book not found")
#file handling:save data to json
def save_data():
    data=[]
    for book in library_books:
        data.append({
            "book_id":book.book_id,
            "title":book.title,
            "author":book.author,
            "copies":book.get_copies(),
            "cost":book.cost,
            "issue_date":str(book.issue_date),
            "return_date":str(book.return_date)
            })
    with open("library_data.json","w") as file:
        json.dump(
            data,
            file,
            indent=4
            )
    print("data saved successfully")
#file handlin:load data from json
def load_data():

    try:

        with open("library_data.json", "r") as file:
            data = json.load(file)

        library_books.clear()

        for item in data:

            book = Book(
                item["book_id"],
                item["title"],
                item["author"],
                item["copies"],
                item["cost"]
            )

            library_books.append(book)

        print("Data Loaded Successfully")

    except FileNotFoundError:

        print("No Saved File Found")


# MAIN FUNCTION
def main():

    student = studentmember("Student")
    admin = adminmember("Library Admin")

    print("\n===== MEMBER DETAILS =====")

    show_member(student)
    show_member(admin)

    while True:

        print("\n******************************")
        print(" SMART LIBRARY MANAGEMENT SYSTEM")
        print("******************************")

        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            save_data()

        elif choice == "7":
            load_data()

        elif choice == "8":
            print("\nThank You For Using Library System")
            break

        else:
            print("Invalid Choice! Please Try Again.")


# PROGRAM ENTRY POINT
if __name__ == "__main__":
    main()


    
    
            

        
    
    
    
