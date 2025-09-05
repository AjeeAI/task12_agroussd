from agro_ussd.users.farmers import Farmer
from agro_ussd.users.buyers import Buyer

def register():
    option1 = """
Welcome to the Agro-Ussd system

1. Register as Buyer
2. Register as Farmer
0. Back
00. Exit
    """
    print(option1)
    while True:
        choice = int(input("Choose from the available options to continue: "))
        if choice == 00:
            print("Ussd is exiting!!!")
            break
        elif choice == 1:
            print("-------------- Buyer Registration -------------")
            buyer = Buyer()
            buyer.register()
            buyer.save_buyer()
        
        elif choice == 2:
            print("-------------- Farmer Registration -------------")
            farmer = Farmer()
            farmer.register()
            farmer.save_farmer()