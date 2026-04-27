#2. To-Do List Application 🧐
import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

def add_todo(todos):
    task = input("Enter task: ")
    todos.append({"task": task, "completed": False})
    save_todos(todos)
    print("Task added!")

def view_todos(todos):
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo["completed"] else "❌"
        print(f"{i}. [{status}] {todo['task']}")

def complete_todo(todos):
    view_todos(todos)
    try:
        index = int(input("Enter task number to complete: ")) - 1
        if 0 <= index < len(todos):
            todos[index]["completed"] = True
            save_todos(todos)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_todo(todos):
    view_todos(todos)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todos):
            todos.pop(index)
            save_todos(todos)
            print("Task deleted!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    todos = load_todos()
    while True:
        print("\n--- To-Do List App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            view_todos(todos)
        elif choice == '3':
            complete_todo(todos)
        elif choice == '4':
            delete_todo(todos)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
