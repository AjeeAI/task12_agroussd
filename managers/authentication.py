from pathlib import Path
import csv
from agro_ussd.users.buyers import Buyer
from agro_ussd.users.farmers import Farmer

# from .user import users #it's not importing users from agro_ussd

#I think this manager file should not be in a separate folder
folder = Path("agro_ussd/data")
buyer_csv = folder / "buyers.csv"
farmer_csv = folder / "farmers.csv"
# path = folder / "users.csv"
# def login(name, password):-
#     with open(path, "r", encoding="utf-8") as file:
#         content = file.readlines()


class UserAuthentication:
    def __init__(self, path):
        self.path = path

    def login(self):
        while True:
            try:
                username = input("Enter your username: ").strip()
                password = input("Enter your password: ").strip()
                found = False
                password_correct = False
                user_row = None
                try:
                    with open(self.path, "r", encoding= "utf-8") as f:
                        reader = csv.reader(f)
                        try:
                            next(reader)
                        except StopIteration:
                            print("No users found yet!!!")
                            return None
                        for row in reader:
                            if not row:
                                continue
                            if row[0].strip() == username:
                                found = True
                                user_row = row
                                if row[1].strip() == password:
                                    password_correct = True
                                    return user_row
                                
                                break
                    
                    if not found:
                        print("Username not found! You are not registered!")
                    elif not password_correct:
                        print("Password entered is not correct!")
                    else:
                        print(f"Login successful! Welcome {user_row[0]}")
                        return user_row
                        
                except FileNotFoundError:
                    print("The file doesn't exist. Try creating it first!!!")
            except Exception as e:
                print(e)
                        

if __name__ == "__main__":
    
    
    authenication = UserAuthentication()

    authenication.login()