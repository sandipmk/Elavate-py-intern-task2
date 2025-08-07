# To-Do List CLI Application - Usage Guide

## Table of Contents
- [Quick Start](#quick-start)
- [Basic Usage](#basic-usage)
- [Step-by-Step Tutorial](#step-by-step-tutorial)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)
- [Tips and Best Practices](#tips-and-best-practices)
- [Integration Examples](#integration-examples)

## Quick Start

### Prerequisites
- Python 3.6 or higher installed on your system
- Terminal/Command Prompt access
- Write permissions in the directory where you run the application

### Installation
1. Download the `t2-todo.py` file to your desired directory
2. Open terminal/command prompt and navigate to that directory
3. Run the application:
   ```bash
   python t2-todo.py
   ```
   or
   ```bash
   python3 t2-todo.py
   ```

### First Run
When you first run the application, you'll see the main menu:
```
---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 
```

## Basic Usage

### Menu Navigation
The application uses a simple numbered menu system:
- **1**: View all current tasks
- **2**: Add a new task
- **3**: Remove an existing task
- **0**: Exit the application

### Adding Your First Task
1. Run the application
2. Choose option `2` (Add Task)
3. Enter your task description when prompted
4. Press Enter to confirm

**Example:**
```
Choose your option : 2
Add the task : Buy groceries
Task added...
```

### Viewing Tasks
1. Choose option `1` (View Tasks)
2. All tasks will be displayed with numbers

**Example:**
```
Choose your option : 1

Your To-Do List :
1. Buy groceries
2. Complete homework
3. Call dentist
```

### Removing Tasks
1. Choose option `3` (Remove Task)
2. The current task list will be displayed
3. Enter the number of the task you want to remove
4. Press Enter to confirm

**Example:**
```
Choose your option : 3

Your To-Do List :
1. Buy groceries
2. Complete homework
3. Call dentist

Enter the task number to remove: 2
Removed task : Complete homework
```

## Step-by-Step Tutorial

### Tutorial: Managing a Daily Task List

Let's walk through a complete session of managing daily tasks:

#### Step 1: Starting the Application
```bash
$ python t2-todo.py
---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 
```

#### Step 2: Check Existing Tasks
```
Choose your option : 1
 tasks not found...

---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 
```
*No tasks exist yet, so we see "tasks not found..."*

#### Step 3: Add Multiple Tasks
```
Choose your option : 2
Add the task : Buy groceries for the week
Task added...

---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 2
Add the task : Finish Python project
Task added...

---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 2
Add the task : Schedule dentist appointment
Task added...
```

#### Step 4: Review Your Task List
```
Choose your option : 1

Your To-Do List :
1. Buy groceries for the week
2. Finish Python project
3. Schedule dentist appointment

---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 
```

#### Step 5: Complete and Remove a Task
```
Choose your option : 3

Your To-Do List :
1. Buy groceries for the week
2. Finish Python project
3. Schedule dentist appointment

Enter the task number to remove: 1
Removed task : Buy groceries for the week
```

#### Step 6: Final Check and Exit
```
Choose your option : 1

Your To-Do List :
1. Finish Python project
2. Schedule dentist appointment

---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 0
Exiting...
```

### Persistent Storage Verification
When you restart the application, your remaining tasks will still be there:
```bash
$ python t2-todo.py
---To-Do List Menu---
1 --> View Tasks
2 --> Add Task
3 --> Remove Task
0 --> Exit
Choose your option : 1

Your To-Do List :
1. Finish Python project
2. Schedule dentist appointment
```

## Advanced Features

### Task File Location
By default, tasks are stored in `tasks.txt` in the same directory as the script. You can modify this by editing the `TASKS_FILE` constant in the code:

```python
# Change this line in t2-todo.py
TASKS_FILE = "tasks.txt"

# To something like:
TASKS_FILE = "/home/user/my-tasks.txt"
# or
TASKS_FILE = os.path.expanduser("~/Documents/todo-tasks.txt")
```

### Batch Task Management
You can manually edit the `tasks.txt` file with a text editor to:
- Add multiple tasks at once
- Edit existing task descriptions
- Reorder tasks
- Import tasks from other sources

**Example tasks.txt content:**
```
Complete quarterly report
Review team performance
Plan vacation
Update resume
Learn new programming language
```

### Command Line Usage
For advanced users, you can create wrapper scripts:

#### Bash Script Example (`todo.sh`)
```bash
#!/bin/bash
cd /path/to/todo/directory
python3 t2-todo.py
```

#### Quick Add Script (`quick-add.py`)
```python
#!/usr/bin/env python3
import sys
import os

# Add the directory containing t2-todo.py to the path
sys.path.append('/path/to/todo/directory')
from t2_todo import load_tasks, save_tasks

if len(sys.argv) > 1:
    tasks = load_tasks()
    new_task = ' '.join(sys.argv[1:])
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added task: {new_task}")
else:
    print("Usage: quick-add.py <task description>")
```

Usage:
```bash
python quick-add.py "Buy milk on the way home"
```

## Troubleshooting

### Common Issues and Solutions

#### Issue: "Permission denied" error
**Problem**: Cannot write to or read from tasks.txt
**Solution**: 
- Check file permissions: `ls -la tasks.txt`
- Make sure you have write permissions in the directory
- Try running from a different directory where you have write access

#### Issue: Tasks disappear after closing
**Problem**: Tasks are not being saved properly
**Solutions**:
- Ensure the directory is writable
- Check if `tasks.txt` exists and has content after adding tasks
- Verify you're running from the same directory each time

#### Issue: "Invalid choice" appears repeatedly
**Problem**: Entering incorrect menu options
**Solution**: 
- Only enter numbers: 0, 1, 2, or 3
- Make sure to press Enter after typing the number
- Avoid entering letters or special characters

#### Issue: Cannot remove tasks
**Problem**: Error when trying to remove tasks by number
**Solutions**:
- Make sure you enter a valid task number (shown in the list)
- Enter only the number, not the full task description
- Check that tasks exist before trying to remove them

#### Issue: Application won't start
**Problem**: Python errors when starting
**Solutions**:
- Verify Python version: `python --version` (should be 3.6+)
- Try `python3 t2-todo.py` instead of `python t2-todo.py`
- Check that the file is not corrupted by re-downloading it

### Error Messages and Meanings

| Error Message | Meaning | Solution |
|---------------|---------|----------|
| "tasks not found..." | No tasks in the list | Add some tasks using option 2 |
| "Task not added..." | Empty task entered | Enter a non-empty task description |
| "Invalid task number..." | Task number out of range | Enter a number between 1 and the number of tasks |
| "Please enter a valid number..." | Non-numeric input for task removal | Enter only numbers when removing tasks |
| "Invalid choice..." | Invalid menu option | Enter only 0, 1, 2, or 3 |

## Tips and Best Practices

### Task Writing Tips
1. **Be Specific**: Instead of "Study", write "Study Chapter 5 of Python book"
2. **Use Action Words**: Start tasks with verbs like "Call", "Buy", "Complete", "Review"
3. **Include Context**: "Call dentist to schedule cleaning appointment" vs just "Call dentist"
4. **Set Deadlines**: "Submit report by Friday 5 PM"

### Organization Strategies
1. **Prioritize**: Add most important tasks first
2. **Categorize**: Use prefixes like "[WORK]", "[PERSONAL]", "[URGENT]"
3. **Time-based**: Include time estimates: "Review emails (30 min)"
4. **Dependencies**: Note if tasks depend on others: "Buy ingredients (for cooking dinner)"

### Workflow Suggestions
1. **Daily Review**: Check tasks every morning
2. **Weekly Planning**: Add upcoming week's tasks on Sunday
3. **Regular Cleanup**: Remove completed tasks regularly
4. **Backup**: Occasionally backup your `tasks.txt` file

### Example Task Categories
```
[WORK] Complete quarterly report
[PERSONAL] Buy groceries
[URGENT] Submit tax documents
[CALL] Schedule dentist appointment
[BUY] New laptop charger
[LEARN] Python decorators tutorial
```

## Integration Examples

### Integration with System Cron Jobs
Create a cron job to add recurring tasks:

```bash
# Add to crontab (crontab -e)
0 9 * * 1 /usr/bin/python3 /path/to/quick-add.py "Weekly team meeting"
0 8 * * * /usr/bin/python3 /path/to/quick-add.py "Check emails"
```

### Integration with Text Editors
Many text editors can be configured to quickly add tasks:

#### Vim Integration
Add to your `.vimrc`:
```vim
command! TodoAdd :!python3 /path/to/quick-add.py "<args>"
```

Usage in Vim:
```
:TodoAdd Buy coffee before meeting
```

### Integration with Shell Aliases
Add to your `.bashrc` or `.zshrc`:
```bash
alias todo='python3 /path/to/t2-todo.py'
alias todo-add='python3 /path/to/quick-add.py'
alias todo-view='head -20 /path/to/tasks.txt'
```

Usage:
```bash
todo                           # Open the full application
todo-add "New task"           # Quickly add a task
todo-view                     # Quickly view tasks
```

### Integration with Other Applications

#### Export to Calendar
```python
#!/usr/bin/env python3
"""Convert tasks to calendar events"""
from datetime import datetime, timedelta
import sys
sys.path.append('/path/to/todo/directory')
from t2_todo import load_tasks

tasks = load_tasks()
today = datetime.now()

print("Calendar Events:")
for i, task in enumerate(tasks):
    event_date = today + timedelta(days=i)
    print(f"{event_date.strftime('%Y-%m-%d')}: {task}")
```

#### Export to Email
```python
#!/usr/bin/env python3
"""Email daily task list"""
import smtplib
from email.mime.text import MIMEText
import sys
sys.path.append('/path/to/todo/directory')
from t2_todo import load_tasks

tasks = load_tasks()
if tasks:
    task_list = "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
    msg = MIMEText(f"Daily Tasks:\n\n{task_list}")
    msg['Subject'] = 'Daily Task List'
    msg['From'] = 'your-email@example.com'
    msg['To'] = 'your-email@example.com'
    
    # Configure your SMTP settings
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.send_message(msg)
    print("Task list prepared for email")
```

### Mobile Access
For mobile access to your tasks:
1. Store `tasks.txt` in a cloud-synchronized folder (Dropbox, Google Drive)
2. Use a text editor app on your phone to view/edit tasks
3. Changes will sync back to your computer

---

*This usage guide covers comprehensive usage scenarios for the To-Do List CLI Application. For technical details, refer to the API Documentation.*