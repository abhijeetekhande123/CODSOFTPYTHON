import json
import os

class TodoList:
    def __init__(self, filename='todo_list.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                status = "✓" if task['completed'] else "✗"
                print(f"{index + 1}. [{status}] {task['task']}")

    def update_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = not self.tasks[task_index]['completed']
            self.save_tasks()
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added!")
        elif choice == '2':
            print("\nCurrent Tasks:")
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to update: ")) - 1
            todo_list.update_task(task_index)
            print("Task updated!")
        elif choice == '4':
            todo_list.view_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_index)
            print("Task deleted!")
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
