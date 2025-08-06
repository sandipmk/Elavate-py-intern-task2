# Elevate Lab Python Internship — Task 2 -> Build To-Do List CLI App

## 📋 Task Overview
This repository contains **Task 2 -- To-Do List CLI app** of the **Elevate Lab Python Internship Program**.

**Objective**:
  - Create a Command-Line based To-Do List Manager that allows users to add, view, and remove tasks with persistent storage.

**Key Concepts**:
  - File handling.
  - Lists.
  - String Manipulation.
---

## 📚 Approach

1. **Understanding Requirements**

   The task was to build a **Console-based To-Do List Application** in Python.

   The app needed to support adding tasks, viewing the current list, and removing tasks.

   Additionally, tasks should be stored in a text file for persistence between runs.

2. **Function-Based Design**

   Developed modular functions for core operations:
   - load_tasks(): Load tasks from a file.
   - save_tasks(tasks): Save tasks to a file.
   - view_tasks(tasks): Display all current tasks.
   - add_task(tasks): Add a new task to the list.
   - remove_task(tasks): Remove a task based on user-selected index.

3. **Persistent Storage**

   Used Python's built-in open() function to read from and write to a tasks.txt file.

   This ensures tasks remain saved even after the program terminates.

4. **User Interaction Loop**

   Implemented a continuous while True loop that displays a menu:
   - View Tasks
   - Add Task
   - Remove Task
   - Exit

   Based on user input, appropriate functions are called to perform the desired action.

5. **Input Validation**

   Ensured robustness by:
   - Checking for empty tasks when adding.
   - Validating numerical inputs when removing tasks.
   - Handling cases where the task list might be empty.

6. **Exit Condition**

   When the user selects the 'Exit' option, the loop breaks and the program terminates gracefully with a goodbye message.

7. **Clean Code Practices**

   - Followed PEP8 coding standards for readability.
   - Added comments to explain key parts of the code.
   - Structured the script using if __name__ == "__main__": block for modular execution.

---

## 🛠️ Tools Used
- **Python**
- **VS Code**
