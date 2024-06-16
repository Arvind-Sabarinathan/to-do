import json
import os

class TodoApp:
    def __init__(self, file_name: str = "tasks.json") -> None:
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self) -> None:
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []
            
    def update_json(self) -> None:
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)
            
    def add_task(self, task: str) -> None:
        self.tasks.append({"task": task, "done": False})
        self.update_json()
        print("Task added!")
    
    def delete_task(self, task_index: int) -> None:
        if 1 <= task_index <= len(self.tasks):
            self.tasks.pop(task_index - 1)
            self.update_json()
            print(f"Task #{task_index} deleted")
        else:
            print(f"Task #{task_index} not found!")
            
    def mark_done(self, task_index: int) -> None:
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            self.update_json()
            print(f"Task #{task_index} marked as done")
        else:
            print(f"Task #{task_index} not found!")
    
    def view_tasks(self) -> None:
        print("\n----Your to-do's----")
        if self.tasks_empty():
            print("You have nothing to do, chill!")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task["done"] else "Not done"
                print(f"#{i}. {task['task']} -> {status}")
        print()
    
    def tasks_empty(self) -> bool:
        return len(self.tasks) == 0

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
        
main()
