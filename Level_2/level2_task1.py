import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter task: ")

    if task_name.strip() == "":
        print("Task cannot be empty.")
        return

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")

   
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n----- To-Do List -----")

    for i, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Task does not exist.")
            return

        deleted_task = tasks.pop(number - 1)
        save_tasks(tasks)

        print(f"Task '{deleted_task['task']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid task number.")


def mark_completed(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark as completed: "))

        if number < 1 or number > len(tasks):
            print("Task does not exist.")
            return

        tasks[number - 1]["completed"] = True
        save_tasks(tasks)

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            mark_completed(tasks)

        elif choice == "5":
            print("Thank you for using To-Do List!")
            break

        else:
            print("Invalid choice. Please try again.")


main()