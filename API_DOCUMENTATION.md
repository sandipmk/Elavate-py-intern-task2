# To-Do List CLI Application - API Documentation

## Overview

The To-Do List CLI Application is a command-line based task management system built in Python. It provides persistent storage of tasks using file I/O operations and offers a simple, interactive interface for managing daily tasks.

## Table of Contents

- [Public APIs](#public-apis)
- [Core Functions](#core-functions)
- [Usage Examples](#usage-examples)
- [Error Handling](#error-handling)
- [File Structure](#file-structure)
- [Installation & Setup](#installation--setup)

## Public APIs

### Main Entry Point

#### `main()`

**Description**: The primary entry point for the To-Do List application. Initializes the task list and provides an interactive menu-driven interface.

**Parameters**: None

**Returns**: None

**Functionality**:
- Loads existing tasks from persistent storage
- Displays an interactive menu with options:
  - View Tasks (Option 1)
  - Add Task (Option 2)
  - Remove Task (Option 3)
  - Exit (Option 0)
- Handles user input validation
- Runs in a continuous loop until user exits

**Example**:
```python
if __name__ == "__main__":
    main()  # Starts the interactive To-Do List application
```

## Core Functions

### Task Loading and Saving

#### `load_tasks()`

**Description**: Loads tasks from the persistent storage file (`tasks.txt`).

**Parameters**: None

**Returns**: 
- `list`: A list of strings representing tasks. Returns empty list if file doesn't exist.

**Behavior**:
- Checks if the tasks file exists
- Reads all non-empty lines from the file
- Strips whitespace from each task
- Returns a list of clean task strings

**Example**:
```python
# Load existing tasks
tasks = load_tasks()
print(f"Loaded {len(tasks)} tasks")

# Example output if tasks.txt contains:
# Buy groceries
# Complete project
# Call dentist
# Result: ['Buy groceries', 'Complete project', 'Call dentist']
```

**Error Handling**:
- Safely handles missing file (returns empty list)
- Ignores empty lines in the file

---

#### `save_tasks(tasks)`

**Description**: Saves the current task list to persistent storage.

**Parameters**:
- `tasks` (list): List of task strings to save

**Returns**: None

**Behavior**:
- Overwrites the existing tasks file
- Writes each task on a separate line
- Adds newline character after each task

**Example**:
```python
tasks = ["Buy milk", "Study Python", "Exercise"]
save_tasks(tasks)
# Creates/updates tasks.txt with:
# Buy milk
# Study Python
# Exercise
```

**Error Handling**:
- Creates the file if it doesn't exist
- Overwrites existing content completely

### Task Display

#### `view_tasks(tasks)`

**Description**: Displays all current tasks in a formatted, numbered list.

**Parameters**:
- `tasks` (list): List of task strings to display

**Returns**: None

**Behavior**:
- Shows "tasks not found..." message if list is empty
- Displays tasks with sequential numbering (1, 2, 3...)
- Adds formatting for better readability

**Example**:
```python
tasks = ["Buy groceries", "Complete homework", "Call mom"]
view_tasks(tasks)

# Output:
# Your To-Do List :
# 1. Buy groceries
# 2. Complete homework
# 3. Call mom

# Empty list example:
empty_tasks = []
view_tasks(empty_tasks)
# Output: tasks not found...
```

### Task Management

#### `add_task(tasks)`

**Description**: Prompts user to add a new task to the list and saves it to persistent storage.

**Parameters**:
- `tasks` (list): Current list of tasks (modified in-place)

**Returns**: None

**Behavior**:
- Prompts user for task input
- Validates that task is not empty (after stripping whitespace)
- Adds valid task to the list
- Automatically saves updated list to file
- Provides feedback to user

**Example**:
```python
tasks = ["Existing task"]
add_task(tasks)

# User interaction:
# Add the task : Buy coffee
# Task added...

# Result: tasks now contains ["Existing task", "Buy coffee"]
# tasks.txt is automatically updated
```

**Input Validation**:
- Rejects empty strings
- Strips leading/trailing whitespace
- Provides appropriate feedback for invalid input

---

#### `remove_task(tasks)`

**Description**: Allows user to remove a task by selecting its number from the displayed list.

**Parameters**:
- `tasks` (list): Current list of tasks (modified in-place)

**Returns**: None

**Behavior**:
- First displays current tasks using `view_tasks()`
- Returns early if task list is empty
- Prompts user to enter task number to remove
- Validates input is a valid integer within range
- Removes selected task and saves updated list
- Provides feedback about the removed task

**Example**:
```python
tasks = ["Task 1", "Task 2", "Task 3"]
remove_task(tasks)

# Output shows current tasks, then prompts:
# Your To-Do List :
# 1. Task 1
# 2. Task 2
# 3. Task 3
# 
# Enter the task number to remove: 2
# Removed task : Task 2
# 
# Result: tasks now contains ["Task 1", "Task 3"]
```

**Input Validation**:
- Handles non-integer input gracefully
- Validates number is within valid range (1 to list length)
- Provides specific error messages for different failure cases

## Usage Examples

### Basic Application Flow

```python
# Starting the application
if __name__ == "__main__":
    main()

# Example session:
# ---To-Do List Menu---
# 1 --> View Tasks
# 2 --> Add Task
# 3 --> Remove Task
# 0 --> Exit
# Choose your option : 2
# Add the task : Buy groceries
# Task added...
# 
# ---To-Do List Menu---
# 1 --> View Tasks
# 2 --> Add Task
# 3 --> Remove Task
# 0 --> Exit
# Choose your option : 1
# 
# Your To-Do List :
# 1. Buy groceries
```

### Programmatic Usage

```python
# Using functions programmatically
import os
from t2_todo import load_tasks, save_tasks, view_tasks, add_task, remove_task

# Load existing tasks
my_tasks = load_tasks()

# Add tasks programmatically
my_tasks.append("New programmatic task")
save_tasks(my_tasks)

# Display tasks
view_tasks(my_tasks)

# The functions can also be used in other scripts
def bulk_add_tasks(task_list, new_tasks):
    """Add multiple tasks at once"""
    current_tasks = load_tasks()
    current_tasks.extend(new_tasks)
    save_tasks(current_tasks)
    return current_tasks
```

### Integration Example

```python
# Example of integrating with other systems
def sync_tasks_from_calendar(calendar_events):
    """Sync tasks from calendar events"""
    tasks = load_tasks()
    
    for event in calendar_events:
        task_description = f"Calendar: {event['title']}"
        if task_description not in tasks:
            tasks.append(task_description)
    
    save_tasks(tasks)
    return tasks
```

## Error Handling

### File Operations
- **Missing tasks.txt**: `load_tasks()` returns empty list instead of crashing
- **Permission errors**: File operations may raise `PermissionError` if file is locked
- **Disk space**: `save_tasks()` may fail if insufficient disk space

### User Input
- **Invalid menu choice**: Application shows "Invalid choice..." and continues
- **Empty task input**: `add_task()` rejects empty tasks with feedback
- **Invalid task number**: `remove_task()` validates range and type
- **Non-numeric input**: Graceful handling with "Please enter a valid number..."

### Recommended Error Handling Enhancements

```python
def safe_save_tasks(tasks):
    """Enhanced save function with error handling"""
    try:
        save_tasks(tasks)
        return True
    except PermissionError:
        print("Error: Cannot write to tasks file. Check permissions.")
        return False
    except IOError as e:
        print(f"Error saving tasks: {e}")
        return False

def safe_load_tasks():
    """Enhanced load function with error handling"""
    try:
        return load_tasks()
    except PermissionError:
        print("Error: Cannot read tasks file. Check permissions.")
        return []
    except IOError as e:
        print(f"Error loading tasks: {e}")
        return []
```

## File Structure

```
project/
├── t2-todo.py          # Main application file
├── tasks.txt           # Persistent storage (created automatically)
├── README.md           # Project overview
└── API_DOCUMENTATION.md # This documentation file
```

### tasks.txt Format
- Plain text file
- One task per line
- UTF-8 encoding
- Automatically created if doesn't exist

## Installation & Setup

### Requirements
- Python 3.6 or higher
- No external dependencies required
- Write permissions in the application directory

### Setup Instructions

1. **Download the application**:
   ```bash
   # Clone or download the t2-todo.py file
   ```

2. **Make executable** (Linux/Mac):
   ```bash
   chmod +x t2-todo.py
   ```

3. **Run the application**:
   ```bash
   python t2-todo.py
   # or
   python3 t2-todo.py
   ```

### Configuration

The application uses a constant for the tasks file:
```python
TASKS_FILE = "tasks.txt"
```

To use a different file location, modify this constant:
```python
TASKS_FILE = "/path/to/your/tasks.txt"
# or
TASKS_FILE = os.path.expanduser("~/my-tasks.txt")
```

## Advanced Usage

### Custom Task Formats

```python
# Example: Adding timestamps to tasks
from datetime import datetime

def add_timestamped_task(tasks, task_description):
    """Add a task with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    formatted_task = f"[{timestamp}] {task_description}"
    tasks.append(formatted_task)
    save_tasks(tasks)
    return formatted_task
```

### Task Categories

```python
# Example: Categorized tasks
def add_categorized_task(tasks, category, description):
    """Add a task with category prefix"""
    categorized_task = f"[{category.upper()}] {description}"
    tasks.append(categorized_task)
    save_tasks(tasks)
    return categorized_task

# Usage:
# add_categorized_task(tasks, "work", "Complete project report")
# add_categorized_task(tasks, "personal", "Buy birthday gift")
```

### Batch Operations

```python
# Example: Batch task operations
def clear_all_tasks():
    """Remove all tasks"""
    save_tasks([])
    print("All tasks cleared.")

def import_tasks_from_file(filename):
    """Import tasks from another file"""
    try:
        with open(filename, 'r') as f:
            new_tasks = [line.strip() for line in f if line.strip()]
        
        existing_tasks = load_tasks()
        existing_tasks.extend(new_tasks)
        save_tasks(existing_tasks)
        
        print(f"Imported {len(new_tasks)} tasks from {filename}")
        return len(new_tasks)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0
```

## API Reference Summary

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `main()` | None | None | Main application entry point |
| `load_tasks()` | None | `list[str]` | Load tasks from file |
| `save_tasks(tasks)` | `list[str]` | None | Save tasks to file |
| `view_tasks(tasks)` | `list[str]` | None | Display formatted task list |
| `add_task(tasks)` | `list[str]` | None | Interactive task addition |
| `remove_task(tasks)` | `list[str]` | None | Interactive task removal |

## Constants

| Constant | Value | Description |
|----------|-------|-------------|
| `TASKS_FILE` | `"tasks.txt"` | Default filename for task storage |

---

*This documentation covers version 1.0 of the To-Do List CLI Application. For updates and improvements, please refer to the project repository.*