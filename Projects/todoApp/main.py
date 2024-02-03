import os

def display_menu():
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Quit")

def view_todo_list():
    with open("todo.txt", "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("No tasks in the To-Do List.")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task.strip()}")

def add_task():
    task = input("Enter the task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added to the To-Do List.")

def mark_completed():
    view_todo_list()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            with open("todo.txt", "w") as file:
                file.writelines(tasks)
            with open("completed.txt", "a") as completed_file:
                completed_file.write(completed_task)
            print(f"Task '{completed_task.strip()}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Ensure the existence of the todo.txt file
if not os.path.exists("todo.txt"):
    open("todo.txt", "w").close()

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_todo_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        print("Exiting the To-Do List Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
