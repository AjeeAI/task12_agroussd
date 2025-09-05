from .user import User

from pathlib import Path
import csv

folder = Path("agro_ussd/data/")
path = folder / "farmers.csv"

user_dict = {}

class Farmer(User):
    def __init__(self, name= "", phone = "", state= "", lga = "", farm_size = 0, products = None):
        super().__init__(name, phone,  state, lga)
        self.farm_size = farm_size
        self.products = products if products is not None else []
    
    def register(self):
        super().register()
        farm_size = input("Enter your farm size: ").strip()
        if farm_size != "":
            self.farm_size = farm_size
        else:
            print("This field cannot be empty!!!")
        while True:
            product = input("Enter the products you have for sale(If you are done enter type 'exit' to exit): ").lower().strip()
            if product == "exit":
                break
            elif product != "":
                self.products.append(product)
                continue
            else:
                print("This field cannot be empty!!!")
                continue
                
            
        
        
    def save_farmer(self):
        file_exists = path.exists()
        with open(path, "a", encoding= "utf-8", newline="") as file:
            fieldnames = ["name", "contact_info", "state", "lga", "farm_size", "products"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            
            writer.writerow({
                "name": self.name,
                "contact_info": self.phone,
                "state": self.state,
                "lga": self.lga,
                "farm_size": self.farm_size,
                "products": self.products
                }
            )
if __name__ == "__main__":
    farmer1 = Farmer()

    farmer1.register()
    farmer1.save_farmer()