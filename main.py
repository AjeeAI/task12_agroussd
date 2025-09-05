from agro_ussd.users.user import User
from agro_ussd.users.farmers import Farmer
from agro_ussd.users.buyers import Buyer
from managers.user_managers import register

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
            pass
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
            
    
    
if __name__ == "__main__":
    main()