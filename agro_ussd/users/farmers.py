
# from user import User


# class Farmers(User):
#     def __init__(self, name, age, state, lga, phone, farm_size, *products):
#         super().__init__(name, age, phone, state, lga)
#         self.farm_size  = farm_size
#         self.products = products
        
#     def display_details(self):
#         print(f"""Farmer: {self.name}
# state: {self.state}
# Local government: {self.lga}
# Contact info: {self.phone}
# Farm size: {self.farm_size} acres
# Products: {self.products}
#               """)
# farmer1 = Farmers("Ajani", 35, "Ogun state", "Abeokuta South", "08059081256", 30, "Rice", "Beans", "Yam")
# farmer1.display_details()

from pathlib import Path
import csv
import random

#i want to save userid and password in data base probably a csvfile
workspace = Path("agro_ussd/data")
workspace.mkdir(exist_ok=True)
csv_file = Path.cwd()/workspace/"users.csv"
def save_user(path,login_credential):
    participant_header = ["Name","user_id","password"]
    if path.exists()==True:
        with open(csv_file,"r",newline="", encoding="utf-8") as f:
            writer_len= list(csv.reader(f))
            print(writer_len)
        if len(writer_len) <=1 :
            with open(path,"w",newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f,fieldnames=participant_header)
                writer.writeheader()
                writer.writerow(login_credential)
        else:
            with open(path,"a",newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f,fieldnames=participant_header)
                writer.writerow(login_credential)
    else:
        with open(path,"w",newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f,fieldnames=participant_header)
            writer.writeheader()
            writer.writerow(login_credential)
    print(f"You have successfully created an account {login_credential["Name"]}\nYour Username is {login_credential["user_id"]}\nPLEASE DONT FORGET YOUR PASSWORD")
    return "SUCCESS"
def sign_up():
        user_name =input("What is your name")
        random_number = random.randint(1,1000)
        while random_number in randnum_used:
            random_number = random.randint(1,1000)
        else:
            random_number = str(random.randint(1,1000))
            randnum_used.append(random_number)

        user_Id= user_name + random_number
        password_farmer= input("please input your password")

        login_credential = {"Name":user_name,"user_id":user_Id,"password":password_farmer}
        return save_user(csv_file,login_credential)

#list of thing to ask farmer
def register_farm():
        ask= ["Name","Phone number", "location","farm size","primary crops"]
        user_details = {}
        for x in ask:
            if x == "Phone number":
                detail= int(input(f"Please input your {x}"))
                while (len(str(detail))+1) <11 or (len(str(detail))+1) >11:
                    print("Invalid input!! Phone number needs to be 11 digits")
                    detail= int(input(f"Please input your {x} again"))
                else:
                    user_details.update({x:detail})
            elif x == "farm size":
                detail= int(input(f"Please input your {x}"))

            else:
                detail=input(f"Please input your {x}")
                user_details.update({x:detail})
            

        print(user_details)
