# To-Do List CLI App Documentation

## Overview
This is a simple, modular Command-Line To-Do List application written in Python. It allows users to add, view, and remove tasks, with persistent storage using a text file (`tasks.txt`).

---

## Installation & Setup
1. **Clone or Download** this repository to your local machine.
2. Ensure you have **Python 3.x** installed.
3. No external dependencies are required.

---

## Usage Instructions
Run the application from your terminal:
```bash
python t2-todo.py
```
You will see a menu with options to view, add, or remove tasks, or exit the app.

---

## CLI Menu Example Session
```
---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 2
Add the task : Buy groceries
Task added...

---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 1

Your To-Do List :
1. Buy groceries

---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 3

Your To-Do List :
1. Buy groceries
Enter the task number to remove: 1
Removed task : Buy groceries
```

---

## Persistent Storage
- All tasks are saved in a file named `tasks.txt` in the same directory as the script.
- The file is created automatically if it does not exist.
- Each line in the file represents a single task.

---

## Public API Reference

### `load_tasks()`
**Description:**
Loads the list of tasks from `tasks.txt`.

**Returns:**
- `list[str]`: List of task strings.

**Example:**
```python
tasks = load_tasks()
```

---

### `save_tasks(tasks)`
**Description:**
Saves the provided list of tasks to `tasks.txt`.

**Parameters:**
- `tasks` (`list[str]`): List of task strings to save.

**Example:**
```python
save_tasks(["Buy groceries", "Read book"])
```

---

### `view_tasks(tasks)`
**Description:**
Displays the current list of tasks to the user.

**Parameters:**
- `tasks` (`list[str]`): List of task strings to display.

**Example:**
```python
view_tasks(tasks)
```

---

### `add_task(tasks)`
**Description:**
Prompts the user to enter a new task, adds it to the list, and saves the updated list.

**Parameters:**
- `tasks` (`list[str]`): The current list of tasks (will be modified in-place).

**Example:**
```python
add_task(tasks)
```

---

### `remove_task(tasks)`
**Description:**
Displays the current tasks, prompts the user to select a task to remove by number, removes it, and saves the updated list.

**Parameters:**
- `tasks` (`list[str]`): The current list of tasks (will be modified in-place).

**Example:**
```python
remove_task(tasks)
```

---

### `main()`
**Description:**
Entry point for the CLI app. Handles the main menu loop and user interaction.

**Example:**
```python
if __name__ == "__main__":
    main()
```

---

## Notes
- All user input is handled via the terminal.
- The app is robust to invalid input and empty task lists.
- To reset your to-do list, simply delete the `tasks.txt` file.

---

## License
This project is for educational purposes as part of the Elevate Lab Python Internship Program.