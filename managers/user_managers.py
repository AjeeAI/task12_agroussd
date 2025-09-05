from pathlib import Path
import csv
from agro_ussd import users #it's not importing users from agro_ussd

#I think this manager file should not be in a separate folder
folder = Path("agro_ussd/data")
path = folder / "users.csv"
# def login(name, password):
#     with open(path, "r", encoding="utf-8") as file:
#         content = file.readlines()
        
class UserAuthentication:
    def __init__(self, path):
        self.path = path

    def login(self):
        with open(self.path, "r+", encoding= "utf-8") as f:
            reader = csv.reader(f)

            while True:
                username = input("Enter your username: ").strip()
                password = input("Enter your password: ").strip()

                for row in reader:
                    if row[1] == username and row[2] == password: #I changed this from row[0] and row[1] to row[1] and row[2] respectively, because hamid csv file contain name before user_id
                        print("Login successful!")
                        print(users.register_farm()) #this should call the function from the users folder

                    else:
                        if row[0] != username:
                            print("User not found, please sign up.")
                        else:    
                            print("Wrong username or password, try again.\n")#this should be wrong password, but to prevent hacking people say username or password
                            break

                            
                        
authenication = UserAuthentication("users.csv")

authenication.login()