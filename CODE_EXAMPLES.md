# To-Do List CLI Application - Code Examples

## Table of Contents
- [Basic Function Usage](#basic-function-usage)
- [Programmatic Integration](#programmatic-integration)
- [Custom Extensions](#custom-extensions)
- [Automation Scripts](#automation-scripts)
- [Error Handling Examples](#error-handling-examples)
- [Testing Examples](#testing-examples)
- [Performance Optimization](#performance-optimization)

## Basic Function Usage

### Working with Tasks Programmatically

```python
#!/usr/bin/env python3
"""
Basic examples of using the to-do list functions programmatically
"""

# Import the functions (assuming t2-todo.py is in the same directory)
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from t2_todo import load_tasks, save_tasks, view_tasks

# Example 1: Load and display existing tasks
print("=== Example 1: Loading and Displaying Tasks ===")
current_tasks = load_tasks()
print(f"Found {len(current_tasks)} existing tasks")
view_tasks(current_tasks)

# Example 2: Add tasks programmatically
print("=== Example 2: Adding Tasks Programmatically ===")
new_tasks = [
    "Review quarterly budget",
    "Update project documentation", 
    "Schedule team meeting",
    "Backup important files"
]

# Load existing tasks and add new ones
tasks = load_tasks()
for task in new_tasks:
    if task not in tasks:  # Avoid duplicates
        tasks.append(task)
        print(f"Added: {task}")

# Save updated task list
save_tasks(tasks)
print(f"\nTotal tasks after additions: {len(tasks)}")
view_tasks(tasks)

# Example 3: Remove specific tasks by content
print("=== Example 3: Removing Tasks by Content ===")
tasks = load_tasks()
task_to_remove = "Backup important files"

if task_to_remove in tasks:
    tasks.remove(task_to_remove)
    save_tasks(tasks)
    print(f"Removed: {task_to_remove}")
else:
    print(f"Task not found: {task_to_remove}")

view_tasks(tasks)
```

### Individual Function Examples

#### `load_tasks()` Examples

```python
#!/usr/bin/env python3
"""Examples of load_tasks() function usage"""

import os
from t2_todo import load_tasks

# Example 1: Basic loading
print("=== Basic Task Loading ===")
tasks = load_tasks()
print(f"Loaded {len(tasks)} tasks:")
for i, task in enumerate(tasks, 1):
    print(f"  {i}. {task}")

# Example 2: Check if tasks file exists
print("\n=== File Existence Check ===")
if os.path.exists("tasks.txt"):
    print("Tasks file exists")
    tasks = load_tasks()
    print(f"Contains {len(tasks)} tasks")
else:
    print("No tasks file found - starting fresh")
    tasks = []

# Example 3: Handle empty file gracefully
print("\n=== Empty File Handling ===")
# Create empty file for testing
with open("test_tasks.txt", "w") as f:
    f.write("")

# Temporarily change the file name to test
import t2_todo
original_file = t2_todo.TASKS_FILE
t2_todo.TASKS_FILE = "test_tasks.txt"

empty_tasks = load_tasks()
print(f"Tasks from empty file: {empty_tasks}")  # Should be []

# Restore original file name
t2_todo.TASKS_FILE = original_file
os.remove("test_tasks.txt")
```

#### `save_tasks()` Examples

```python
#!/usr/bin/env python3
"""Examples of save_tasks() function usage"""

from t2_todo import save_tasks, load_tasks

# Example 1: Save a new task list
print("=== Saving New Task List ===")
sample_tasks = [
    "Complete Python assignment",
    "Buy groceries for dinner",
    "Call insurance company",
    "Schedule car maintenance"
]

save_tasks(sample_tasks)
print(f"Saved {len(sample_tasks)} tasks to file")

# Verify by loading
loaded_tasks = load_tasks()
print(f"Verification: loaded {len(loaded_tasks)} tasks")

# Example 2: Update existing tasks
print("\n=== Updating Existing Tasks ===")
tasks = load_tasks()
tasks.append("New urgent task")
tasks.insert(0, "PRIORITY: Review important email")  # Add at beginning
save_tasks(tasks)
print("Updated task list saved")

# Example 3: Clear all tasks
print("\n=== Clearing All Tasks ===")
save_tasks([])  # Save empty list
print("All tasks cleared")

# Restore sample tasks for other examples
save_tasks(sample_tasks)
```

#### `view_tasks()` Examples

```python
#!/usr/bin/env python3
"""Examples of view_tasks() function usage"""

from t2_todo import view_tasks, load_tasks

# Example 1: Display current tasks
print("=== Current Tasks Display ===")
tasks = load_tasks()
view_tasks(tasks)

# Example 2: Display empty task list
print("=== Empty Task List Display ===")
empty_tasks = []
view_tasks(empty_tasks)

# Example 3: Display custom task lists
print("=== Custom Task Lists ===")
work_tasks = [
    "Finish quarterly report",
    "Attend team standup",
    "Review pull requests"
]
print("Work Tasks:")
view_tasks(work_tasks)

personal_tasks = [
    "Buy birthday gift for mom",
    "Plan weekend trip",
    "Organize photo collection"
]
print("Personal Tasks:")
view_tasks(personal_tasks)

# Example 4: Capture output for processing
print("=== Capturing Task Display ===")
import io
import sys

# Redirect stdout to capture print output
old_stdout = sys.stdout
sys.stdout = buffer = io.StringIO()

view_tasks(work_tasks)

# Get the output
output = buffer.getvalue()
sys.stdout = old_stdout

print("Captured output:")
print(repr(output))
```

## Programmatic Integration

### Task Management Class

```python
#!/usr/bin/env python3
"""
Enhanced task management with object-oriented approach
"""

import os
from datetime import datetime
from t2_todo import load_tasks, save_tasks

class TaskManager:
    """Enhanced task manager with additional features"""
    
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        # Temporarily change the global filename
        import t2_todo
        self.original_file = t2_todo.TASKS_FILE
        t2_todo.TASKS_FILE = filename
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore original filename
        import t2_todo
        t2_todo.TASKS_FILE = self.original_file
    
    def get_tasks(self):
        """Get all tasks"""
        return load_tasks()
    
    def add_task(self, task, priority=None):
        """Add a task with optional priority"""
        tasks = load_tasks()
        
        if priority:
            task = f"[{priority.upper()}] {task}"
        
        tasks.append(task)
        save_tasks(tasks)
        return len(tasks)
    
    def remove_task_by_content(self, task_content):
        """Remove task by exact content match"""
        tasks = load_tasks()
        
        if task_content in tasks:
            tasks.remove(task_content)
            save_tasks(tasks)
            return True
        return False
    
    def remove_task_by_index(self, index):
        """Remove task by index (0-based)"""
        tasks = load_tasks()
        
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            return removed_task
        return None
    
    def find_tasks(self, keyword):
        """Find tasks containing a keyword"""
        tasks = load_tasks()
        return [task for task in tasks if keyword.lower() in task.lower()]
    
    def count_tasks(self):
        """Get total number of tasks"""
        return len(load_tasks())
    
    def clear_all_tasks(self):
        """Remove all tasks"""
        save_tasks([])
    
    def backup_tasks(self, backup_filename=None):
        """Create a backup of current tasks"""
        if not backup_filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"tasks_backup_{timestamp}.txt"
        
        tasks = load_tasks()
        with open(backup_filename, 'w') as f:
            for task in tasks:
                f.write(task + '\n')
        
        return backup_filename
    
    def import_tasks(self, import_filename):
        """Import tasks from another file"""
        try:
            with open(import_filename, 'r') as f:
                new_tasks = [line.strip() for line in f if line.strip()]
            
            existing_tasks = load_tasks()
            
            # Add only new tasks (avoid duplicates)
            added_count = 0
            for task in new_tasks:
                if task not in existing_tasks:
                    existing_tasks.append(task)
                    added_count += 1
            
            save_tasks(existing_tasks)
            return added_count
        
        except FileNotFoundError:
            return -1

# Usage examples
if __name__ == "__main__":
    print("=== TaskManager Class Examples ===")
    
    with TaskManager("example_tasks.txt") as tm:
        # Add some tasks
        tm.add_task("Complete project proposal", "HIGH")
        tm.add_task("Review team performance")
        tm.add_task("Schedule dentist appointment", "LOW")
        
        print(f"Total tasks: {tm.count_tasks()}")
        
        # Find tasks
        high_priority = tm.find_tasks("HIGH")
        print(f"High priority tasks: {high_priority}")
        
        # Create backup
        backup_file = tm.backup_tasks()
        print(f"Backup created: {backup_file}")
        
        # Remove a task
        removed = tm.remove_task_by_content("Review team performance")
        print(f"Task removed: {removed}")
        
        print(f"Remaining tasks: {tm.count_tasks()}")
    
    # Clean up
    if os.path.exists("example_tasks.txt"):
        os.remove("example_tasks.txt")
    if os.path.exists(backup_file):
        os.remove(backup_file)
```

### Web API Wrapper

```python
#!/usr/bin/env python3
"""
Simple web API wrapper for the todo list using Flask
"""

from flask import Flask, jsonify, request
from t2_todo import load_tasks, save_tasks
import json

app = Flask(__name__)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    try:
        tasks = load_tasks()
        return jsonify({
            'success': True,
            'tasks': tasks,
            'count': len(tasks)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """Add a new task"""
    try:
        data = request.get_json()
        if not data or 'task' not in data:
            return jsonify({
                'success': False,
                'error': 'Task content required'
            }), 400
        
        task_content = data['task'].strip()
        if not task_content:
            return jsonify({
                'success': False,
                'error': 'Task cannot be empty'
            }), 400
        
        tasks = load_tasks()
        tasks.append(task_content)
        save_tasks(tasks)
        
        return jsonify({
            'success': True,
            'message': 'Task added successfully',
            'task': task_content,
            'total_tasks': len(tasks)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task by ID (1-based index)"""
    try:
        tasks = load_tasks()
        
        # Convert to 0-based index
        index = task_id - 1
        
        if index < 0 or index >= len(tasks):
            return jsonify({
                'success': False,
                'error': 'Invalid task ID'
            }), 404
        
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        
        return jsonify({
            'success': True,
            'message': 'Task deleted successfully',
            'deleted_task': removed_task,
            'remaining_tasks': len(tasks)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tasks/search', methods=['GET'])
def search_tasks():
    """Search tasks by keyword"""
    try:
        keyword = request.args.get('q', '').strip()
        if not keyword:
            return jsonify({
                'success': False,
                'error': 'Search keyword required'
            }), 400
        
        tasks = load_tasks()
        matching_tasks = [
            {'id': i + 1, 'task': task}
            for i, task in enumerate(tasks)
            if keyword.lower() in task.lower()
        ]
        
        return jsonify({
            'success': True,
            'keyword': keyword,
            'matches': matching_tasks,
            'count': len(matching_tasks)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("Starting Todo List API server...")
    print("Available endpoints:")
    print("  GET    /api/tasks           - Get all tasks")
    print("  POST   /api/tasks           - Add new task")
    print("  DELETE /api/tasks/<id>      - Delete task by ID")
    print("  GET    /api/tasks/search?q= - Search tasks")
    
    app.run(debug=True, port=5000)
```

## Custom Extensions

### Task Categories and Priorities

```python
#!/usr/bin/env python3
"""
Extended task management with categories and priorities
"""

import re
from datetime import datetime
from t2_todo import load_tasks, save_tasks

class CategorizedTaskManager:
    """Task manager with category and priority support"""
    
    PRIORITIES = ['LOW', 'MEDIUM', 'HIGH', 'URGENT']
    
    def __init__(self):
        self.tasks = load_tasks()
    
    def add_categorized_task(self, task, category=None, priority=None, due_date=None):
        """Add a task with category, priority, and due date"""
        formatted_task = task
        
        # Add priority prefix
        if priority and priority.upper() in self.PRIORITIES:
            formatted_task = f"[{priority.upper()}] {formatted_task}"
        
        # Add category prefix
        if category:
            formatted_task = f"[{category.upper()}] {formatted_task}"
        
        # Add due date suffix
        if due_date:
            formatted_task = f"{formatted_task} (Due: {due_date})"
        
        self.tasks.append(formatted_task)
        save_tasks(self.tasks)
        return formatted_task
    
    def get_tasks_by_category(self, category):
        """Get all tasks in a specific category"""
        pattern = rf'\[{category.upper()}\]'
        return [task for task in self.tasks if re.search(pattern, task)]
    
    def get_tasks_by_priority(self, priority):
        """Get all tasks with a specific priority"""
        pattern = rf'\[{priority.upper()}\]'
        return [task for task in self.tasks if re.search(pattern, task)]
    
    def get_overdue_tasks(self):
        """Get tasks that are overdue (simplified date check)"""
        today = datetime.now().strftime("%Y-%m-%d")
        overdue = []
        
        for task in self.tasks:
            # Simple date pattern matching
            due_match = re.search(r'Due: (\d{4}-\d{2}-\d{2})', task)
            if due_match:
                due_date = due_match.group(1)
                if due_date < today:
                    overdue.append(task)
        
        return overdue
    
    def sort_tasks_by_priority(self):
        """Sort tasks by priority level"""
        priority_order = {'URGENT': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3, None: 4}
        
        def get_priority(task):
            for priority in self.PRIORITIES:
                if f'[{priority}]' in task:
                    return priority_order[priority]
            return priority_order[None]
        
        sorted_tasks = sorted(self.tasks, key=get_priority)
        self.tasks = sorted_tasks
        save_tasks(self.tasks)
        return sorted_tasks
    
    def generate_report(self):
        """Generate a comprehensive task report"""
        report = {
            'total_tasks': len(self.tasks),
            'by_priority': {},
            'by_category': {},
            'overdue': self.get_overdue_tasks()
        }
        
        # Count by priority
        for priority in self.PRIORITIES:
            report['by_priority'][priority] = len(self.get_tasks_by_priority(priority))
        
        # Count by category (extract unique categories)
        categories = set()
        for task in self.tasks:
            matches = re.findall(r'\[([A-Z]+)\]', task)
            for match in matches:
                if match not in self.PRIORITIES:
                    categories.add(match)
        
        for category in categories:
            report['by_category'][category] = len(self.get_tasks_by_category(category))
        
        return report

# Usage examples
if __name__ == "__main__":
    print("=== Categorized Task Manager Examples ===")
    
    # Clear existing tasks for clean demo
    save_tasks([])
    
    ctm = CategorizedTaskManager()
    
    # Add various tasks
    ctm.add_categorized_task("Complete quarterly report", "WORK", "HIGH", "2024-01-15")
    ctm.add_categorized_task("Buy groceries", "PERSONAL", "MEDIUM")
    ctm.add_categorized_task("Submit tax documents", "FINANCE", "URGENT", "2024-01-10")
    ctm.add_categorized_task("Plan vacation", "PERSONAL", "LOW")
    ctm.add_categorized_task("Team meeting preparation", "WORK", "MEDIUM", "2024-01-12")
    
    print(f"Added {len(ctm.tasks)} tasks")
    
    # Get tasks by category
    work_tasks = ctm.get_tasks_by_category("WORK")
    print(f"\nWork tasks: {len(work_tasks)}")
    for task in work_tasks:
        print(f"  - {task}")
    
    # Get high priority tasks
    high_priority = ctm.get_tasks_by_priority("HIGH")
    print(f"\nHigh priority tasks: {len(high_priority)}")
    for task in high_priority:
        print(f"  - {task}")
    
    # Sort by priority
    print("\n=== Sorting by Priority ===")
    sorted_tasks = ctm.sort_tasks_by_priority()
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. {task}")
    
    # Generate report
    print("\n=== Task Report ===")
    report = ctm.generate_report()
    print(f"Total tasks: {report['total_tasks']}")
    print("By priority:")
    for priority, count in report['by_priority'].items():
        print(f"  {priority}: {count}")
    print("By category:")
    for category, count in report['by_category'].items():
        print(f"  {category}: {count}")
    print(f"Overdue tasks: {len(report['overdue'])}")
```

## Automation Scripts

### Daily Task Automation

```python
#!/usr/bin/env python3
"""
Automation scripts for daily task management
"""

import os
import sys
from datetime import datetime, timedelta
from t2_todo import load_tasks, save_tasks

def add_daily_recurring_tasks():
    """Add tasks that should appear every day"""
    daily_tasks = [
        "Check and respond to emails",
        "Review daily schedule",
        "Update project status"
    ]
    
    tasks = load_tasks()
    today = datetime.now().strftime("%Y-%m-%d")
    
    for daily_task in daily_tasks:
        # Check if today's version of this task already exists
        dated_task = f"{daily_task} ({today})"
        if dated_task not in tasks:
            tasks.append(dated_task)
    
    save_tasks(tasks)
    return len(daily_tasks)

def add_weekly_recurring_tasks():
    """Add tasks that should appear weekly"""
    weekly_tasks = {
        0: ["Weekly team meeting", "Plan upcoming week"],  # Monday
        2: ["Mid-week progress review"],                    # Wednesday
        4: ["Weekly report submission", "Plan weekend"]     # Friday
    }
    
    today = datetime.now()
    weekday = today.weekday()  # 0 = Monday, 6 = Sunday
    
    if weekday in weekly_tasks:
        tasks = load_tasks()
        date_str = today.strftime("%Y-%m-%d")
        
        for weekly_task in weekly_tasks[weekday]:
            dated_task = f"{weekly_task} ({date_str})"
            if dated_task not in tasks:
                tasks.append(dated_task)
        
        save_tasks(tasks)
        return len(weekly_tasks[weekday])
    
    return 0

def cleanup_old_tasks():
    """Remove completed or old dated tasks"""
    tasks = load_tasks()
    today = datetime.now()
    cutoff_date = today - timedelta(days=7)  # Remove tasks older than 7 days
    
    cleaned_tasks = []
    removed_count = 0
    
    for task in tasks:
        # Look for date patterns in tasks
        import re
        date_match = re.search(r'\((\d{4}-\d{2}-\d{2})\)', task)
        
        if date_match:
            task_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
            if task_date >= cutoff_date:
                cleaned_tasks.append(task)
            else:
                removed_count += 1
        else:
            # Keep tasks without dates
            cleaned_tasks.append(task)
    
    if removed_count > 0:
        save_tasks(cleaned_tasks)
    
    return removed_count

def generate_daily_summary():
    """Generate a summary of today's tasks"""
    tasks = load_tasks()
    today = datetime.now().strftime("%Y-%m-%d")
    
    today_tasks = [task for task in tasks if today in task]
    other_tasks = [task for task in tasks if today not in task]
    
    summary = {
        'date': today,
        'total_tasks': len(tasks),
        'today_tasks': today_tasks,
        'other_tasks': other_tasks,
        'today_count': len(today_tasks),
        'other_count': len(other_tasks)
    }
    
    return summary

def backup_tasks_daily():
    """Create a daily backup of tasks"""
    tasks = load_tasks()
    if not tasks:
        return None
    
    backup_dir = "task_backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    today = datetime.now().strftime("%Y-%m-%d")
    backup_file = os.path.join(backup_dir, f"tasks_{today}.txt")
    
    # Don't overwrite if backup already exists today
    if not os.path.exists(backup_file):
        with open(backup_file, 'w') as f:
            for task in tasks:
                f.write(task + '\n')
        return backup_file
    
    return None

# Main automation script
def run_daily_automation():
    """Run all daily automation tasks"""
    print("=== Running Daily Task Automation ===")
    
    # Add recurring tasks
    daily_added = add_daily_recurring_tasks()
    weekly_added = add_weekly_recurring_tasks()
    print(f"Added {daily_added} daily tasks, {weekly_added} weekly tasks")
    
    # Clean up old tasks
    removed = cleanup_old_tasks()
    print(f"Removed {removed} old tasks")
    
    # Create backup
    backup_file = backup_tasks_daily()
    if backup_file:
        print(f"Created backup: {backup_file}")
    else:
        print("Backup already exists for today")
    
    # Generate summary
    summary = generate_daily_summary()
    print(f"\n=== Daily Summary ({summary['date']}) ===")
    print(f"Total tasks: {summary['total_tasks']}")
    print(f"Today's tasks: {summary['today_count']}")
    print(f"Other tasks: {summary['other_count']}")
    
    if summary['today_tasks']:
        print("\nToday's tasks:")
        for i, task in enumerate(summary['today_tasks'], 1):
            print(f"  {i}. {task}")

if __name__ == "__main__":
    # Can be run as a standalone script or imported
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        run_daily_automation()
    else:
        print("Daily Task Automation Script")
        print("Usage:")
        print("  python automation.py --auto    # Run automation")
        print("\nFunctions available:")
        print("  - add_daily_recurring_tasks()")
        print("  - add_weekly_recurring_tasks()")
        print("  - cleanup_old_tasks()")
        print("  - generate_daily_summary()")
        print("  - backup_tasks_daily()")
        print("  - run_daily_automation()")
```

### Cron Job Integration

```bash
#!/bin/bash
# cron_todo.sh - Script for cron job integration

# Add to crontab with: crontab -e
# Then add lines like:
# 0 9 * * * /path/to/cron_todo.sh daily
# 0 18 * * 5 /path/to/cron_todo.sh weekly_report

SCRIPT_DIR="/path/to/todo/directory"
PYTHON_CMD="python3"

cd "$SCRIPT_DIR"

case "$1" in
    "daily")
        echo "Running daily automation..."
        $PYTHON_CMD automation.py --auto
        ;;
    "weekly_report")
        echo "Generating weekly report..."
        $PYTHON_CMD -c "
import sys
sys.path.append('$SCRIPT_DIR')
from automation import generate_daily_summary
from t2_todo import load_tasks

tasks = load_tasks()
summary = generate_daily_summary()
print(f'Weekly Report - {summary[\"date\"]}')
print(f'Total active tasks: {len(tasks)}')
for i, task in enumerate(tasks, 1):
    print(f'{i}. {task}')
" > weekly_report.txt
        echo "Weekly report saved to weekly_report.txt"
        ;;
    "backup")
        echo "Creating backup..."
        $PYTHON_CMD -c "
import sys
sys.path.append('$SCRIPT_DIR')
from automation import backup_tasks_daily
backup_file = backup_tasks_daily()
if backup_file:
    print(f'Backup created: {backup_file}')
else:
    print('Backup already exists')
"
        ;;
    *)
        echo "Usage: $0 {daily|weekly_report|backup}"
        exit 1
        ;;
esac
```

## Error Handling Examples

### Robust Task Operations

```python
#!/usr/bin/env python3
"""
Examples of robust error handling for task operations
"""

import os
import sys
from t2_todo import load_tasks, save_tasks

class TaskOperationError(Exception):
    """Custom exception for task operations"""
    pass

def safe_load_tasks(filename=None):
    """Safely load tasks with comprehensive error handling"""
    try:
        if filename:
            # Temporarily change filename
            import t2_todo
            original_file = t2_todo.TASKS_FILE
            t2_todo.TASKS_FILE = filename
        
        tasks = load_tasks()
        
        if filename:
            t2_todo.TASKS_FILE = original_file
        
        return tasks, None
    
    except PermissionError as e:
        return [], f"Permission denied: {e}"
    except FileNotFoundError as e:
        return [], f"File not found: {e}"
    except UnicodeDecodeError as e:
        return [], f"File encoding error: {e}"
    except Exception as e:
        return [], f"Unexpected error loading tasks: {e}"

def safe_save_tasks(tasks, filename=None):
    """Safely save tasks with error handling and validation"""
    try:
        # Validate input
        if not isinstance(tasks, list):
            raise TaskOperationError("Tasks must be a list")
        
        if not all(isinstance(task, str) for task in tasks):
            raise TaskOperationError("All tasks must be strings")
        
        # Check for empty tasks
        clean_tasks = [task.strip() for task in tasks if task.strip()]
        
        if filename:
            import t2_todo
            original_file = t2_todo.TASKS_FILE
            t2_todo.TASKS_FILE = filename
        
        # Create backup before saving
        backup_tasks = load_tasks()
        
        try:
            save_tasks(clean_tasks)
            success = True
            error = None
        except Exception as save_error:
            # Restore from backup on failure
            try:
                save_tasks(backup_tasks)
            except:
                pass  # If restore fails, at least we tried
            raise save_error
        
        if filename:
            t2_todo.TASKS_FILE = original_file
        
        return success, error, len(clean_tasks)
    
    except TaskOperationError as e:
        return False, str(e), 0
    except PermissionError as e:
        return False, f"Permission denied: {e}", 0
    except OSError as e:
        return False, f"File system error: {e}", 0
    except Exception as e:
        return False, f"Unexpected error saving tasks: {e}", 0

def safe_add_task(new_task, validation_func=None):
    """Safely add a task with validation"""
    try:
        # Input validation
        if not isinstance(new_task, str):
            raise TaskOperationError("Task must be a string")
        
        clean_task = new_task.strip()
        if not clean_task:
            raise TaskOperationError("Task cannot be empty")
        
        if len(clean_task) > 500:  # Reasonable length limit
            raise TaskOperationError("Task too long (max 500 characters)")
        
        # Custom validation if provided
        if validation_func and not validation_func(clean_task):
            raise TaskOperationError("Task failed custom validation")
        
        # Load existing tasks
        tasks, load_error = safe_load_tasks()
        if load_error:
            return False, load_error
        
        # Check for duplicates
        if clean_task in tasks:
            return False, "Task already exists"
        
        # Add task
        tasks.append(clean_task)
        
        # Save updated tasks
        success, save_error, count = safe_save_tasks(tasks)
        if not success:
            return False, save_error
        
        return True, f"Task added successfully. Total tasks: {count}"
    
    except TaskOperationError as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {e}"

def safe_remove_task(task_identifier, by_index=True):
    """Safely remove a task by index or content"""
    try:
        tasks, load_error = safe_load_tasks()
        if load_error:
            return False, load_error, None
        
        if not tasks:
            return False, "No tasks to remove", None
        
        removed_task = None
        
        if by_index:
            # Remove by index (1-based for user interface)
            try:
                index = int(task_identifier) - 1
                if index < 0 or index >= len(tasks):
                    return False, f"Invalid task number. Valid range: 1-{len(tasks)}", None
                
                removed_task = tasks.pop(index)
            except ValueError:
                return False, "Task number must be a valid integer", None
        else:
            # Remove by content
            if task_identifier not in tasks:
                return False, "Task not found", None
            
            removed_task = task_identifier
            tasks.remove(task_identifier)
        
        # Save updated tasks
        success, save_error, count = safe_save_tasks(tasks)
        if not success:
            return False, save_error, None
        
        return True, f"Task removed successfully. Remaining tasks: {count}", removed_task
    
    except Exception as e:
        return False, f"Unexpected error: {e}", None

# Usage examples
if __name__ == "__main__":
    print("=== Safe Task Operations Examples ===")
    
    # Test safe loading
    print("\n1. Safe Loading:")
    tasks, error = safe_load_tasks()
    if error:
        print(f"Error: {error}")
    else:
        print(f"Loaded {len(tasks)} tasks successfully")
    
    # Test safe adding with validation
    print("\n2. Safe Adding:")
    
    def validate_task(task):
        """Example validation function"""
        # Don't allow tasks that are too short or contain forbidden words
        if len(task) < 3:
            return False
        forbidden = ['hack', 'illegal', 'spam']
        return not any(word in task.lower() for word in forbidden)
    
    test_tasks = [
        "Buy groceries for the week",
        "",  # Empty task
        "x" * 600,  # Too long
        "Hack the system",  # Contains forbidden word
        "Valid task example"
    ]
    
    for test_task in test_tasks:
        success, message = safe_add_task(test_task, validate_task)
        print(f"  '{test_task[:50]}{'...' if len(test_task) > 50 else ''}': {message}")
    
    # Test safe removal
    print("\n3. Safe Removal:")
    
    # Remove by index
    success, message, removed = safe_remove_task(1, by_index=True)
    print(f"  Remove by index 1: {message}")
    if removed:
        print(f"    Removed: {removed}")
    
    # Remove by content
    success, message, removed = safe_remove_task("Valid task example", by_index=False)
    print(f"  Remove by content: {message}")
    if removed:
        print(f"    Removed: {removed}")
    
    # Test error conditions
    print("\n4. Error Handling:")
    
    # Try to remove from empty list
    save_tasks([])  # Clear tasks
    success, message, removed = safe_remove_task(1, by_index=True)
    print(f"  Remove from empty list: {message}")
    
    # Try invalid index
    save_tasks(["One task"])
    success, message, removed = safe_remove_task(5, by_index=True)
    print(f"  Remove invalid index: {message}")
```

## Testing Examples

### Unit Tests

```python
#!/usr/bin/env python3
"""
Unit tests for the todo list functions
"""

import unittest
import os
import tempfile
import sys

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from t2_todo import load_tasks, save_tasks, view_tasks
import t2_todo

class TestTodoFunctions(unittest.TestCase):
    """Test cases for todo list functions"""
    
    def setUp(self):
        """Set up test environment"""
        # Create temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        self.test_file.close()
        
        # Store original filename and set test filename
        self.original_file = t2_todo.TASKS_FILE
        t2_todo.TASKS_FILE = self.test_file.name
    
    def tearDown(self):
        """Clean up test environment"""
        # Restore original filename
        t2_todo.TASKS_FILE = self.original_file
        
        # Remove test file
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)
    
    def test_load_tasks_empty_file(self):
        """Test loading from empty file"""
        tasks = load_tasks()
        self.assertEqual(tasks, [])
    
    def test_load_tasks_nonexistent_file(self):
        """Test loading from non-existent file"""
        # Remove test file
        os.unlink(self.test_file.name)
        
        tasks = load_tasks()
        self.assertEqual(tasks, [])
    
    def test_save_and_load_tasks(self):
        """Test saving and loading tasks"""
        test_tasks = ["Task 1", "Task 2", "Task 3"]
        
        # Save tasks
        save_tasks(test_tasks)
        
        # Load tasks
        loaded_tasks = load_tasks()
        
        self.assertEqual(loaded_tasks, test_tasks)
    
    def test_save_empty_tasks(self):
        """Test saving empty task list"""
        save_tasks([])
        tasks = load_tasks()
        self.assertEqual(tasks, [])
    
    def test_save_tasks_with_empty_strings(self):
        """Test that empty strings are filtered out on load"""
        # Manually create file with empty lines
        with open(self.test_file.name, 'w') as f:
            f.write("Task 1\n")
            f.write("\n")  # Empty line
            f.write("Task 2\n")
            f.write("   \n")  # Whitespace only
            f.write("Task 3\n")
        
        tasks = load_tasks()
        expected = ["Task 1", "Task 2", "Task 3"]
        self.assertEqual(tasks, expected)
    
    def test_save_tasks_with_unicode(self):
        """Test saving and loading tasks with unicode characters"""
        unicode_tasks = ["Task with émojis 😀", "Tâche en français", "任务中文"]
        
        save_tasks(unicode_tasks)
        loaded_tasks = load_tasks()
        
        self.assertEqual(loaded_tasks, unicode_tasks)
    
    def test_view_tasks_output(self):
        """Test view_tasks output"""
        import io
        import contextlib
        
        # Test with tasks
        test_tasks = ["First task", "Second task"]
        
        # Capture stdout
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            view_tasks(test_tasks)
        
        output = f.getvalue()
        
        # Check that output contains expected elements
        self.assertIn("Your To-Do List :", output)
        self.assertIn("1. First task", output)
        self.assertIn("2. Second task", output)
    
    def test_view_empty_tasks(self):
        """Test view_tasks with empty list"""
        import io
        import contextlib
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            view_tasks([])
        
        output = f.getvalue()
        self.assertIn("tasks not found...", output)
    
    def test_large_task_list(self):
        """Test with large number of tasks"""
        large_task_list = [f"Task {i}" for i in range(1000)]
        
        save_tasks(large_task_list)
        loaded_tasks = load_tasks()
        
        self.assertEqual(len(loaded_tasks), 1000)
        self.assertEqual(loaded_tasks[0], "Task 0")
        self.assertEqual(loaded_tasks[999], "Task 999")
    
    def test_task_persistence(self):
        """Test that tasks persist across multiple operations"""
        # Add some initial tasks
        initial_tasks = ["Initial 1", "Initial 2"]
        save_tasks(initial_tasks)
        
        # Load and add more tasks
        tasks = load_tasks()
        tasks.extend(["Added 1", "Added 2"])
        save_tasks(tasks)
        
        # Load again and verify
        final_tasks = load_tasks()
        expected = ["Initial 1", "Initial 2", "Added 1", "Added 2"]
        self.assertEqual(final_tasks, expected)

class TestTaskOperations(unittest.TestCase):
    """Test higher-level task operations"""
    
    def setUp(self):
        """Set up test environment"""
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
        self.test_file.close()
        
        self.original_file = t2_todo.TASKS_FILE
        t2_todo.TASKS_FILE = self.test_file.name
    
    def tearDown(self):
        """Clean up test environment"""
        t2_todo.TASKS_FILE = self.original_file
        if os.path.exists(self.test_file.name):
            os.unlink(self.test_file.name)
    
    def test_add_remove_cycle(self):
        """Test adding and removing tasks"""
        # Start with empty list
        save_tasks([])
        
        # Add tasks
        tasks = load_tasks()
        tasks.append("Test task 1")
        tasks.append("Test task 2")
        save_tasks(tasks)
        
        # Verify addition
        tasks = load_tasks()
        self.assertEqual(len(tasks), 2)
        
        # Remove one task
        tasks.remove("Test task 1")
        save_tasks(tasks)
        
        # Verify removal
        tasks = load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], "Test task 2")
    
    def test_duplicate_handling(self):
        """Test handling of duplicate tasks"""
        tasks = ["Task 1", "Task 2", "Task 1"]  # Duplicate
        save_tasks(tasks)
        
        loaded_tasks = load_tasks()
        # Should preserve duplicates as saved
        self.assertEqual(loaded_tasks, tasks)

def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestTodoFunctions))
    suite.addTests(loader.loadTestsFromTestCase(TestTaskOperations))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    print("Running Todo List Unit Tests...")
    success = run_tests()
    
    if success:
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)
```

## Performance Optimization

### Optimized Task Manager

```python
#!/usr/bin/env python3
"""
Performance-optimized version of task operations
"""

import os
import json
import pickle
from datetime import datetime
from t2_todo import TASKS_FILE

class OptimizedTaskManager:
    """Performance-optimized task manager with caching and batch operations"""
    
    def __init__(self, cache_file=None, use_json=False):
        self.cache_file = cache_file or f"{TASKS_FILE}.cache"
        self.use_json = use_json  # JSON vs pickle for serialization
        self._cache = None
        self._cache_timestamp = None
        self._dirty = False
    
    def _get_file_timestamp(self, filename):
        """Get file modification timestamp"""
        try:
            return os.path.getmtime(filename)
        except OSError:
            return 0
    
    def _load_from_file(self):
        """Load tasks from the original file"""
        from t2_todo import load_tasks
        return load_tasks()
    
    def _save_to_file(self, tasks):
        """Save tasks to the original file"""
        from t2_todo import save_tasks
        save_tasks(tasks)
    
    def _load_cache(self):
        """Load tasks from cache if available and valid"""
        if not os.path.exists(self.cache_file):
            return None
        
        try:
            cache_timestamp = self._get_file_timestamp(self.cache_file)
            file_timestamp = self._get_file_timestamp(TASKS_FILE)
            
            # Cache is invalid if original file is newer
            if file_timestamp > cache_timestamp:
                return None
            
            if self.use_json:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            else:
                with open(self.cache_file, 'rb') as f:
                    return pickle.load(f)
        
        except (json.JSONDecodeError, pickle.PickleError, OSError):
            return None
    
    def _save_cache(self, tasks):
        """Save tasks to cache"""
        try:
            if self.use_json:
                with open(self.cache_file, 'w') as f:
                    json.dump(tasks, f)
            else:
                with open(self.cache_file, 'wb') as f:
                    pickle.dump(tasks, f)
        except OSError:
            pass  # Cache save failure is not critical
    
    def get_tasks(self, use_cache=True):
        """Get tasks with optional caching"""
        if use_cache and self._cache is not None:
            file_timestamp = self._get_file_timestamp(TASKS_FILE)
            if self._cache_timestamp and file_timestamp <= self._cache_timestamp:
                return self._cache.copy()
        
        # Try to load from cache first
        if use_cache:
            cached_tasks = self._load_cache()
            if cached_tasks is not None:
                self._cache = cached_tasks
                self._cache_timestamp = self._get_file_timestamp(TASKS_FILE)
                return cached_tasks.copy()
        
        # Load from file
        tasks = self._load_from_file()
        
        # Update cache
        if use_cache:
            self._cache = tasks.copy()
            self._cache_timestamp = self._get_file_timestamp(TASKS_FILE)
            self._save_cache(tasks)
        
        return tasks
    
    def save_tasks(self, tasks, update_cache=True):
        """Save tasks with cache update"""
        self._save_to_file(tasks)
        
        if update_cache:
            self._cache = tasks.copy()
            self._cache_timestamp = self._get_file_timestamp(TASKS_FILE)
            self._save_cache(tasks)
    
    def batch_add_tasks(self, new_tasks, avoid_duplicates=True):
        """Add multiple tasks efficiently"""
        current_tasks = self.get_tasks()
        
        if avoid_duplicates:
            current_set = set(current_tasks)
            tasks_to_add = [task for task in new_tasks if task not in current_set]
        else:
            tasks_to_add = new_tasks
        
        if tasks_to_add:
            updated_tasks = current_tasks + tasks_to_add
            self.save_tasks(updated_tasks)
            return len(tasks_to_add)
        
        return 0
    
    def batch_remove_tasks(self, tasks_to_remove):
        """Remove multiple tasks efficiently"""
        current_tasks = self.get_tasks()
        
        if isinstance(tasks_to_remove, str):
            tasks_to_remove = [tasks_to_remove]
        
        removal_set = set(tasks_to_remove)
        updated_tasks = [task for task in current_tasks if task not in removal_set]
        
        removed_count = len(current_tasks) - len(updated_tasks)
        
        if removed_count > 0:
            self.save_tasks(updated_tasks)
        
        return removed_count
    
    def search_tasks(self, query, case_sensitive=False):
        """Efficiently search tasks"""
        tasks = self.get_tasks()
        
        if not case_sensitive:
            query = query.lower()
            return [
                (i, task) for i, task in enumerate(tasks)
                if query in task.lower()
            ]
        else:
            return [
                (i, task) for i, task in enumerate(tasks)
                if query in task
            ]
    
    def get_task_stats(self):
        """Get task statistics efficiently"""
        tasks = self.get_tasks()
        
        stats = {
            'total': len(tasks),
            'avg_length': sum(len(task) for task in tasks) / len(tasks) if tasks else 0,
            'longest': max(tasks, key=len) if tasks else "",
            'shortest': min(tasks, key=len) if tasks else "",
            'word_count': sum(len(task.split()) for task in tasks)
        }
        
        return stats

# Performance comparison
def performance_test():
    """Compare performance of different approaches"""
    import time
    
    # Generate test data
    test_tasks = [f"Performance test task {i}" for i in range(1000)]
    
    print("=== Performance Test ===")
    
    # Test standard operations
    print("\n1. Standard Operations:")
    start_time = time.time()
    
    from t2_todo import save_tasks, load_tasks
    save_tasks(test_tasks)
    
    for _ in range(100):
        tasks = load_tasks()
    
    standard_time = time.time() - start_time
    print(f"   100 loads: {standard_time:.4f} seconds")
    
    # Test optimized operations
    print("\n2. Optimized Operations:")
    start_time = time.time()
    
    otm = OptimizedTaskManager()
    otm.save_tasks(test_tasks)
    
    for _ in range(100):
        tasks = otm.get_tasks()
    
    optimized_time = time.time() - start_time
    print(f"   100 cached loads: {optimized_time:.4f} seconds")
    
    # Test batch operations
    print("\n3. Batch Operations:")
    start_time = time.time()
    
    # Add 100 tasks one by one (standard way)
    tasks = load_tasks()
    for i in range(100):
        tasks.append(f"Individual task {i}")
        save_tasks(tasks)
    
    individual_time = time.time() - start_time
    
    start_time = time.time()
    
    # Add 100 tasks in batch
    batch_tasks = [f"Batch task {i}" for i in range(100)]
    otm.batch_add_tasks(batch_tasks)
    
    batch_time = time.time() - start_time
    
    print(f"   Individual adds: {individual_time:.4f} seconds")
    print(f"   Batch add: {batch_time:.4f} seconds")
    
    # Performance summary
    print(f"\n=== Performance Summary ===")
    print(f"Cache speedup: {standard_time / optimized_time:.2f}x faster")
    print(f"Batch speedup: {individual_time / batch_time:.2f}x faster")
    
    # Cleanup
    otm_cache_file = otm.cache_file
    if os.path.exists(otm_cache_file):
        os.remove(otm_cache_file)

if __name__ == "__main__":
    print("Code Examples for To-Do List CLI Application")
    print("=" * 50)
    
    # Run performance test
    performance_test()
```

---

*This comprehensive code examples document provides practical implementations and usage patterns for the To-Do List CLI Application. Use these examples as starting points for your own extensions and integrations.*