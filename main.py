from agro_ussd.users.user import User
from agro_ussd.users.farmers import Farmer
from agro_ussd.users.buyers import Buyer
from managers.user_managers import register
from managers.authentication import UserAuthentication
from managers.editor import Editor
from pathlib import Path
import csv
import readline
folder = Path("agro_ussd/data")

buyer_csv = folder / "buyers.csv"
farmer_csv = folder / "farmers.csv"
path = folder / "buyers.csv"

def main():
    while True:
        option1 = """
    Welcome to the Agro-Ussd system
    1. Login
    2. Register
    0. exit
        """
        print(option1)
        choice = int(input("Choose from the available options to continue: "))
        if choice == 0:
            break
        elif choice == 1:
            user_type = input("Are you a buyer or a farmer(b for buyer/ f for farmer): ").strip().upper()
            if user_type != "B" and user_type != "F":
                print("Invalid input! Input can only be B or F")
            elif user_type == "B":
                csv_path = buyer_csv
            else:
                csv_path = farmer_csv
        
            auth = UserAuthentication(csv_path)
            user_data = auth.login()
            if user_type == "B":
                try:
                    buyer = Buyer(*user_data)
                    print(f"Welcome buyer {buyer.name}")
                except Exception as e:
                    print(e)
                view = Editor(csv_path)
                print(view.view(buyer.name))
                view.edit(buyer.name)
                
            else:
                farmer = Farmer(*user_data)
                print(f"Welcome farmer {farmer.name}")
                view = Editor(csv_path)
                # print(view.view(farmer.name))
                print(view.edit(farmer.name))
           
        elif choice == 2:
            option1 = """
    Welcome to the Agro-Ussd system

    1. Register as Buyer
    2. Register as Farmer
    0. Back
    00. Exit
        """
            print(option1)
            register()
        else:
            print("Invalid option. Choose from the available ones!")
        break
            
    
    
if __name__ == "__main__":
    main()