from agro_ussd.users.user import User
from agro_ussd.users.farmers import Farmer
from agro_ussd.users.buyers import Buyer
from managers.user_managers import register

def main():
    option1 = """
Welcome to the Agro-Ussd system
1. Login
2. Register
0. exit
    """

    while True:
        choice = int(input("Choose from the available options to continue: "))
        if choice == 0:
            break
        elif choice == 1:
            pass
        elif choice == 2:
            register()
            
    
    
if __name__ == "__main__":
    main()