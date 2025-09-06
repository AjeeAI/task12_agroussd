from agro_ussd.users.farmers import Farmer
from agro_ussd.users.buyers import Buyer

def register():
    
    while True:
        option1 = """
    Welcome to the Agro-Ussd system

    1. Register as Buyer
    2. Register as Farmer
    0. Back"""
        print(option1)
        choice = int(input("Choose from the available options to continue: "))
        if choice == 0:
            break
            
        elif choice == 1:
            print("-------------- Buyer Registration -------------")
            buyer = Buyer()
            buyer.register()
            buyer.save_buyer()
            break
        
        elif choice == 2:
            print("-------------- Farmer Registration -------------")
            farmer = Farmer()
            farmer.register()
            farmer.save_farmer()
            break
        else:
            print("Invalid input. Please choose from the available options to continue!")
            
            
# def login():
    

        
