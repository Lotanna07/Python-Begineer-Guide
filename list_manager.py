#projects: to-do list manager: to add task, view tasks and remove tasks

todo_list = []

def show_menu():
    print("\nTodo list manage")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Remove Tasks")
    print("4. Exit")


#view task
def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        print("\nyour Tasks:")
        for i , task in enumerate(todo_list, 1 ):
            print(f"(i), task")


#add task
def add_task():
    task =input("Enter a new task:")
    todo_list.append(task)
    print(f'"(task)" added!')


#remove task
def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove"))
        removed = todo_list.pop(task_num - 1)
        print(f'f"(removed)" removed successfully!')
    except (IndexError, ValueError):
        print("invalid task number.")


#main loop

while True:
    show_menu()
    choice = input("choose an option:")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("good bye!")
        break
    else:
        print("invalid choice. try again")
    