from .user import User
from pathlib import Path
import csv

folder = Path("agro_ussd/data/")
path = folder / "buyers.csv"

class Buyer(User):
    
    def save_buyer(self):
        file_exists = path.exists()
        with open(path, "a", encoding="utf-8", newline="") as file:
            fieldnames = ["name", "password", "contact_info", "state", "lga"]
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            if not file_exists:
                writer.writeheader()
                
            writer.writerow({
                "name": self.name,
                "password": self.password,
                    "contact_info": self.phone,
                    "state": self.state,
                    "lga": self.lga
                    })
    def edit_buyer_details(self):
        while True:
            with open(path, "r+", encoding="utf-8")as file:
                reader = csv.reader(file)
                for num, row in enumerate(reader):
                    
                    print(f"{num}. {row}")
                break
# if __name__ == "__main__":            
    # buyer1 = Buyer()
    # buyer1.register()
    # buyer1.save_buyer()
        