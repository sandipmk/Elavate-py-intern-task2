"""
To-Do List CLI Application

A simple command-line task management system that allows users to add, view, 
and remove tasks with persistent file storage.

Author: Elevate Lab Python Internship Program
Version: 1.0
"""

import os

# Configuration constant for the tasks storage file
TASKS_FILE = "tasks.txt"

def load_tasks():
    """
    Load tasks from the persistent storage file.
    
    Reads tasks from the TASKS_FILE (tasks.txt by default) and returns them
    as a list of strings. Each line in the file represents a single task.
    Empty lines are automatically filtered out.
    
    Returns:
        list[str]: A list of task strings. Returns an empty list if the file
                  doesn't exist or is empty.
    
    Example:
        >>> tasks = load_tasks()
        >>> print(tasks)
        ['Buy groceries', 'Complete homework', 'Call dentist']
    
    Note:
        - Creates no file if it doesn't exist (returns empty list)
        - Strips whitespace from each task automatically
        - Ignores empty lines in the file
    """
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
    return tasks

def save_tasks(tasks):
    """
    Save the task list to persistent storage.
    
    Writes all tasks to the TASKS_FILE, with each task on a separate line.
    This function overwrites the existing file content completely.
    
    Args:
        tasks (list[str]): List of task strings to save to file.
    
    Returns:
        None
    
    Example:
        >>> tasks = ["Buy milk", "Study Python", "Exercise"]
        >>> save_tasks(tasks)
        # Creates/updates tasks.txt with the three tasks
    
    Note:
        - Creates the file if it doesn't exist
        - Overwrites existing file content completely
        - Each task is written on a separate line with a newline character
    
    Raises:
        IOError: If there are file permission or disk space issues
    """
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks(tasks):
    """
    Display all tasks in a formatted, numbered list.
    
    Shows tasks with sequential numbering starting from 1. If the task list
    is empty, displays a "tasks not found..." message instead.
    
    Args:
        tasks (list[str]): List of task strings to display.
    
    Returns:
        None
    
    Example:
        >>> tasks = ["Buy groceries", "Complete homework"]
        >>> view_tasks(tasks)
        
        Your To-Do List :
        1. Buy groceries
        2. Complete homework
        
        >>> view_tasks([])
        tasks not found...
    
    Note:
        - Numbering starts from 1 (not 0) for user-friendly display
        - Adds extra newline for better formatting
        - Handles empty list gracefully with informative message
    """
    if not tasks:
        print(" tasks not found...")
    else:
        print("\nYour To-Do List :")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    print()

def add_task(tasks):
    """
    Interactively add a new task to the task list.
    
    Prompts the user to enter a task description, validates the input,
    and adds it to the task list if valid. The updated list is automatically
    saved to persistent storage.
    
    Args:
        tasks (list[str]): Current task list (modified in-place).
    
    Returns:
        None
    
    Example:
        >>> tasks = ["Existing task"]
        >>> add_task(tasks)
        Add the task : Buy coffee
        Task added...
        >>> print(tasks)
        ['Existing task', 'Buy coffee']
    
    Validation:
        - Rejects empty strings (after stripping whitespace)
        - Provides user feedback for both successful and failed additions
        - Automatically saves the updated task list to file
    
    Side Effects:
        - Modifies the tasks list in-place
        - Saves updated tasks to persistent storage
        - Prints feedback messages to console
    """
    task = input("Add the task : ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added...\n")
    else:
        print("Task not added...\n")

def remove_task(tasks):
    """
    Interactively remove a task from the task list by number.
    
    First displays the current task list, then prompts the user to select
    a task number to remove. Validates the input and removes the selected
    task if the input is valid. The updated list is automatically saved.
    
    Args:
        tasks (list[str]): Current task list (modified in-place).
    
    Returns:
        None
    
    Example:
        >>> tasks = ["Task 1", "Task 2", "Task 3"]
        >>> remove_task(tasks)
        
        Your To-Do List :
        1. Task 1
        2. Task 2
        3. Task 3
        
        Enter the task number to remove: 2
        Removed task : Task 2
        >>> print(tasks)
        ['Task 1', 'Task 3']
    
    Validation:
        - Checks if task list is empty and returns early if so
        - Validates input is a valid integer
        - Ensures task number is within valid range (1 to list length)
        - Provides specific error messages for different failure cases
    
    Side Effects:
        - Displays current tasks using view_tasks()
        - Modifies the tasks list in-place
        - Saves updated tasks to persistent storage
        - Prints feedback messages to console
    
    Error Handling:
        - Handles non-integer input with ValueError exception
        - Validates task number range
        - Returns early for empty task lists
    """
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
    """
    Main entry point for the To-Do List CLI application.
    
    Initializes the application by loading existing tasks and presenting
    an interactive menu-driven interface. Runs in a continuous loop until
    the user chooses to exit.
    
    Returns:
        None
    
    Menu Options:
        1 - View Tasks: Display all current tasks
        2 - Add Task: Add a new task to the list
        3 - Remove Task: Remove a task by number
        0 - Exit: Terminate the application
    
    Example:
        >>> main()
        ---To-Do List Menu---
        1 --> View Tasks
        2 --> Add Task
        3 --> Remove Task
        0 --> Exit
        Choose your option : 1
        
        Your To-Do List :
        1. Buy groceries
    
    Features:
        - Persistent task storage across application runs
        - Input validation for menu choices
        - Graceful handling of invalid menu selections
        - Clean exit with confirmation message
    
    Side Effects:
        - Loads tasks from persistent storage on startup
        - All task modifications are automatically saved
        - Prints menu and feedback messages to console
    """
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