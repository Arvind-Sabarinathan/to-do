# To-Do App

This project is a command-line interface (CLI) based to-do application written in Python. The app allows users to manage their to-do list by adding, deleting, viewing, and marking tasks as done. Tasks are stored in a JSON file, ensuring persistence across sessions.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation and Usage](#installation-and-usage)
4. [Code Overview](#code-overview)

## Features

- **Add Tasks**: Add new tasks to your to-do list.
- **Delete Tasks**: Remove tasks from your list by their index.
- **View Tasks**: Display all tasks with their completion status.
- **Mark Tasks as Done**: Mark tasks as completed.
- **Persistent Storage**: Tasks are saved in a JSON file for persistence.

## Requirements

- Python 3
- git

## Installation and Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Arvind-Sabarinathan/to-do.git
   ```

2. **Navigate to the project directory:**

    ```bash
    cd to-do
    ```

3. **Run the application:**

    ```bash
    python todo_app.py
    ```

4. **Follow the on-screen prompts to interact with the to-do app.**

## Code Overview

### TodoApp class

```py
class TodoApp:
    def **init**(self, file_name: str = "tasks.json") -> None:
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()
```

Initializes the `TodoApp` instance:

- `file_name`: The name of the JSON file to store tasks.
- `self.tasks`: A list to hold tasks, loaded from the file if it exists.

### load_tasks

```py
    def load_tasks(self) -> None:
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []
```

Loads tasks from the JSON file if it exists, otherwise initializes an empty list.

### update_json

```py
def update_json(self) -> None:
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)
```

Writes the current list of tasks to the JSON file.

### add_task

```py
def add_task(self, task: str) -> None:
        self.tasks.append({"task": task, "done": False})
        self.update_json()
        print("Task added!")
```

Adds a new task to the list and updates the JSON file.

### delete_task

```py
def delete_task(self, task_index: int) -> None:
        if 1 <= task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
            self.update_json()
            print(f"Task #{task_index} deleted")
        else:
            print(f"Task #{task_index} not found!")
```

Deletes a task by its index and updates the JSON file. Handles invalid indices with a message.

### mark_done

```py
def mark_done(self, task_index: int) -> None:
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            self.update_json()
            print(f"Task #{task_index} marked as done")
        else:
            print(f"Task #{task_index} not found!")
```

Marks a task as done by its index and updates the JSON file. Handles invalid indices with a message.

### view_tasks

```py
def view_tasks(self) -> None:
        print("\n----Your to-do's----")
        if self.tasks_empty():
            print("You have nothing to do, chill!")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task["done"] else "Not done"
                print(f"#{i}. {task['task']} -> {status}")
        print()
```

Prints all tasks with their status. Indicates if there are no tasks to display.

### tasks_empty

```py
def tasks_empty(self) -> bool:
        return len(self.tasks) == 0
```

Returns `True` if the task list is empty, otherwise `False`.

### main

```py
def main() -> None:
    app = TodoApp()
    
    print("\n----To-do-App----")
    print("Choices : 1. Add task | 2. Delete task | 3. View tasks | 4. Mark as done | 5. Exit\n")
    
    while True:
        try:
            choice = int(input("\nEnter your choice# : "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if choice == 1:
            task = input("Task: ")
            app.add_task(task)
            app.view_tasks()
            
        elif choice == 2:
            app.view_tasks()
            if not app.tasks_empty():
                try:
                    task_index = int(input("Enter the task# to remove: "))
                    app.delete_task(task_index)
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
        elif choice == 3:
            app.view_tasks()
            
        elif choice == 4:
            app.view_tasks()
            if not app.tasks_empty():
                try:
                    task_index = int(input("Enter the task# to mark as done: "))
                    app.mark_done(task_index)
                except ValueError:
                    print("Invalid input! Please enter a number.")
            
        elif choice == 5:
            break
        
        else:
            print("Invalid choice! Try again.")
```

The entry point of the application:

- Initializes a `TodoApp` instance.
- Provides a menu for the user to interact with the app.
- Handles user input and calls the appropriate `TodoApp` methods based on the user's choice.
- Continuously prompts for input until the user decides to exit.
