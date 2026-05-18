#project student marks tracker

student = {}

def show_menu():
    print("\nstudent marks tracker")
    print("1. add students")
    print("2. view students")
    print("3. update marks")
    print("4. delete student")
    print("5. Exit")

def add_student ():
    name = input("enter student name")
    marks = float(input("enter marks:"))
    student[name] = marks
    print(f"(name)`$ marks added.")

add_student()
print(student)


add_student()

def view_student():
    if student:
        print("no student yet.")
    else:
        print("\student records:")
        for name, mark in student.item():
            print(f"(name) : (marks)")


#view_student

def update_marks():
    name = input("enter the student name to update:")
    if name in student:
        new_marks = float(input("Enter new marks:"))
        student[name] = new_marks
        print(f"(name)'s marks updated....")
    else:
        print("start not found!")


def delete_student():
    name = input("Enter the student name to delete:")
    if name in student:
        student.pop(name)
        print(f"(name) removed.")
    else:
        print("student not found!")

#main loop
while True:
    show_menu()
    choice = input("choose an option:")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        view_student()
        print("Goodbye")
        break
    else:
        print("invalid choice. try again")
    