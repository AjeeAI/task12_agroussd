
from user import User


class Farmers(User):
    def __init__(self, name, age, state, lga, phone, farm_size, *products):
        super().__init__(name, age, phone, state, lga)
        self.farm_size  = farm_size
        self.products = products
        
    def display_details(self):
        print(f"""Farmer: {self.name}
state: {self.state}
Local government: {self.lga}
Contact info: {self.phone}
Farm size: {self.farm_size} acres
Products: {self.products}
              """)
farmer1 = Farmers("Ajani", 35, "Ogun state", "Abeokuta South", "08059081256", 30, "Rice", "Beans", "Yam")
farmer1.display_details()