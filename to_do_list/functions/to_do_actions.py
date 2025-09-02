from pathlib import Path
import readline

todo_files = Path("todo_files")
todo_files.mkdir(exist_ok=True)
path = todo_files / "todo.txt"

def add_todo(path, todos):
    try:
        with open(path, "a", encoding="utf-8", newline="") as file:
            file.write(todos)
            file.write("\n")
    except FileNotFoundError:
        print("File not found. Please create the file first!!!")

# def remove_todo(path, todo):
#     with open(path , "r+", encoding="utf-8") as file:
#         content = file.readlines()
#         todo_int = int(input("Input the index of the todo you want to remove: "))
#         todo = content[todo_int - 1]
#         del content[todo_int - 1]
#         for todo in content:
#             print(todo)
#         file.write(str(content))

def remove_todo(path):
    with open(path, "r+", encoding="utf-8") as file:
        content = file.readlines()
        todo_int = int(input("Input the index of the todo you want to remove: "))
        if 1 <= todo_int <= len(content):
            del content[todo_int - 1]
            file.seek(0)
            file.truncate()
            file.writelines(content)
            print("Todo removed. Current list:")
            for num, todo in enumerate(content, 1):
                print(f"{num}. {todo}".strip())
        else:
            print("Invalid index.")

# def edit_todo(path):
#     with open(path, "r+", encoding="utf-8") as file:
#         content = file.readlines()
#         for num, todo in enumerate(content, 1):
#             print(f"{num}. {todo}".strip())
#         todo_int = int(input("Input the index of the todo you want to edit: "))
#         if 1 <= todo_int <= len(content):
#             current_todo = content[todo_int - 1].strip()
#             new_todo = input(f"Edit todo [{current_todo}]: ")
#             if new_todo.strip() == "":
#                 print("Todo unchanged.")
#             else:
#                 content[todo_int - 1] = new_todo + "\n"
#                 file.seek(0)
#                 file.truncate()
#                 file.writelines(content)
#                 print("Todo updated. Current list:")
#                 for num, todo in enumerate(content, 1):
#                     print(f"{num}. {todo}".strip())
#         else:
#             print("Invalid index.")

def edit_todo(path):
    with open(path, "r+", encoding="utf-8") as file:
        content = file.readlines()
        for num, todo in enumerate(content, 1):
            print(f"{num}. {todo}".strip())
        todo_int = int(input("Input the index of the todo you want to edit: "))
        if 1 <= todo_int <= len(content):
            current_todo = content[todo_int - 1].strip()
            # Pre-fill input with current todo
            def prefill():
                readline.insert_text(current_todo)
                readline.redisplay()
            readline.set_pre_input_hook(prefill)
            new_todo = input(f"Edit todo [{current_todo}]: ")
            readline.set_pre_input_hook() 
            if new_todo.strip() == "":
                print("Todo unchanged.")
            else:
                content[todo_int - 1] = new_todo + "\n"
                file.seek(0)
                file.truncate()
                file.writelines(content)
                print("Todo updated. Current list:")
                for num, todo in enumerate(content, 1):
                    print(f"{num}. {todo}".strip())
        else:
            print("Invalid index.")
# def mark_as_completed(path):
#     with open(path, "r+", encoding="utf-8") as file:
#         content = 
    
def view_todo(path):
    with open(path, "r", encoding="utf-8", newline="") as file:
        content = file.readlines()
        for num, todo in enumerate(content, 1):
            print(f"{num}. {todo}".strip())
            
        
