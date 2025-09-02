from functions import to_do_actions
from pathlib import Path
todo_files = Path("todo_files")
path = todo_files / "todo.txt"



while True:
    print("""
1. Add todo
2. View todos
3. Remove todos
4. Edit todos
5. Exit program      
      """)
    action = input("Choose from the available options to continue: ")
    if action == "1":
        while True:
            todo = input("Enter your todo: ")
            todo = f"{todo}\n"
            to_do_actions.add_todo(path, todo)
            exit = input("Enter done if you are 'done' entering todos: ").lower()
            if exit == "done":
                break
            continue
    elif action == "2":
        to_do_actions.view_todo(path)
        break
    elif action == "3":
        to_do_actions.view_todo(path)
        to_do_actions.remove_todo(path)
        to_do_actions.view_todo(path)
    elif action == "4":
        to_do_actions.edit_todo(path)
    elif action == "5":
        break
    else:
        print("Invalid choice! Choose from the options available.")
    
