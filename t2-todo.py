# TO-do-list apk....

import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
    return tasks

# Save tasks to a file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

#View tasks ...
def view_tasks(tasks):
    if not tasks:
        print(" tasks not found...")
    else:
        print("\nYour To-Do List :")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()

# Add a task to the list
def add_task(tasks):
    task = input("Add the task : ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added...\n")
    else:
        print("Task not added...\n")

#remove task from the list
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed task : {removed}\n")
        else:
            print("Invalid task number...\n")
    except ValueError:
        print("Please enter a valid number...\n")

def main():
    tasks = load_tasks()
    while True:
        print("---To-Do List Menu---")
        print("1 --> View Tasks")
        print("2 --> Add Task")
        print("3 --> Remove Task")
        print("0 --> Exit")
        choice = input("Choose your option : ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice...\n")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()