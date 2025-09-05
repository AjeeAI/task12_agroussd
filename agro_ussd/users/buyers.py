from user import User
from pathlib import Path
import csv

folder = Path("agro_ussd/data/")
path = folder / "buyers.csv"

class Buyer(User):
    
    def save_buyer(self):
        file_exists = path.exists()
        with open(path, "a", encoding="utf-8") as file:
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
buyer1 = Buyer()
buyer1.register()
buyer1.save_buyer()
        