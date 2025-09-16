import csv
import readline
from prompt_toolkit import prompt
class Editor:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        
    def view(self, username):
        with open(self.csv_path, "r", encoding="utf-8") as file:
            content = csv.reader(file)
            next(content)
            for num, row in enumerate(content, 1):
                if row and row[0].strip() == username:
                    return f"{num}. {row}"
            
        print("User not found")
        return None
    
    def edit(self, username):
        with open(self.csv_path, "r", encoding="utf-8") as file:
            content = file.readlines()

        updated = False
        for num, row in enumerate(content):
            if num != 0:  # skip header
                parts = row.strip().split(",")
                if parts and parts[0].strip() == username:
                    prefill_text = ",".join(parts)
                    new_content = prompt("Edit -- ", default=prefill_text)
                    content[num] = new_content + "\n"
                    updated = True
                    break

        if updated:
            with open(self.csv_path, "w", encoding="utf-8") as file:
                file.writelines(content)
            print("User updated!")
        else:
            print("User not found")     
                
            
            
        