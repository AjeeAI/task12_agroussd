import csv
class Editor:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        
    def view(self, username):
        with open(self.csv_path, "r", encoding="utf-8") as file:
            content = csv.reader(file)
            next(content)
            for num, row in enumerate(content, 1):
                if row and row[0].strip() == username:
                    return row
        print("User not found")
        return None