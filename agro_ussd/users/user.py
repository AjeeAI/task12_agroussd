from pathlib import Path
import csv

folder = Path("agro_ussd/data/")
path = folder / "users.csv"

user_dict = {}
class User:
    def __init__(self, name= "", phone = "", state= "", lga = ""):
        self.name = name
        self.phone = phone
        self.state = state
        self.lga = lga
        
    def save_user(self):
        file_exists = path.exists()
        with open(path, "a", encoding="utf-8", newline = "") as file:
            fieldnames = ["name", "contact_info", "state", "lga"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            if not file_exists:
                writer.writeheader()
                
            writer.writerow({
                "name": self.name,
                    "contact_info": self.phone,
                    "state": self.state,
                    "lga": self.lga
                    })
                
            
        
    def register(self):
        while True:
            name = input("Enter your name: ").strip()
            if name != "":
                self.name = name
            else:
                print("This field cannot be left empty!!!")
                continue
                
            phone = input("Enter your phone number: ").strip()
            if phone != "":
                self.phone = phone
            else:
                print("This field cannot be left empty!!!")
                continue
            state = input("Enter the state you reside in: ").strip()
            if state != "":
                self.state = state
            else:
                print("This field cannot be left empty!!!")
                continue
            
            lga = input("Enter the lga of the area you reside: ").strip()
            if lga != "":
                self.lga = lga
            else:
                print("This field cannot be left empty!!!")
                continue
            print(user_dict)
            break

if __name__ == "__main__":
    user1 = User()
    user1.register()
    user1.save_user()                
            

        
    
