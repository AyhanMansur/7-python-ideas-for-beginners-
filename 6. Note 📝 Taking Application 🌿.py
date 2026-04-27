# notes.py
import os
import datetime

NOTES_DIR = "my_notes"

def ensure_notes_dir():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

def add_note(title, content):
    ensure_notes_dir()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{NOTES_DIR}/{title.replace(' ', '_')}_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(f"Title: {title}\n")
        f.write(f"Date: {timestamp}\n")
        f.write("-" * 30 + "\n")
        f.write(content)
    print(f"Note saved as: {filename}")

def list_notes():
    ensure_notes_dir()
    files = os.listdir(NOTES_DIR)
    if not files:
        print("No notes found.")
        return
    print("\n--- Your Notes ---")
    for f in files:
        print(f"- {f}")

def read_note(filename):
    ensure_notes_dir()
    filepath = os.path.join(NOTES_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            print(f.read())
    else:
        print("Note not found.")

def main():
    while True:
        print("\n--- Note-Taking App ---")
        print("1. Add Note")
        print("2. List Notes")
        print("3. Read Note")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            add_note(title, content)
        elif choice == '2':
            list_notes()
        elif choice == '3':
            list_notes()
            filename = input("Enter filename to read: ")
            read_note(filename)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()