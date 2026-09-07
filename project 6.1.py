#TASK 4:MINI PYHTON PROJECT
#TOPIC:Student Management System
#student management system
from datetime import datetime
file_name="student.txt"
#functions to add a student
def add_student():
    try:
        name=input("enter student name:")
        age=int(input("enter student age:"))
        course=input("enter student course:")
        city=input("enter student city:")
        with open(file_name,"a") as file:
            file.write(f"{name},{age},{course},{city}\n")
        print("Student added successfully!")
    except ValueError:
        print("Error:Age must be a number.")
#function to display students
def display_student():
    try:
        with open(file_name,"r") as file:
            data=file.readlines()
            if not data:
                print("No student record found")
                return
            print("\n ---STUDENT RECORDS---")
            for i,record in enumerate(data,start=1):
                fields = record.strip().split(",")
                if len(fields)==4:
                    name, age, course, city = fields
                    print(f"{i}. Name:{name}, Age:{age}, Course:{course}, City:{city}")
    except FileNotFoundError:
        print("No student records found.")
#main menu
while True:
    print("======STUDENT MANAGEMENT SYSTEM ======")
    print("1.Add Student")
    print("2.Display Students")
    print("3.Show Current Date and Time")
    print("4.Exit")
    try:
        choice=int(input("enter your choice: ").strip())
        if choice==1:
            add_student()
        elif choice==2:
            display_student()
        elif choice==3:
            print("Current Date And  Time:",datetime.now())
        elif choice==4:
            print(" Thanks  For Using The System")

        else:
            print("Invalid choice ,please select 1-4")
    except ValueError:
        print("Error:please enter a number.")
            
            
    
        
        
            
