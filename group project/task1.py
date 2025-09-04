from pathlib import Path
import csv
import random
#user registration
#welcome message for the ussd service 
print(("============="*6).center(100))
print("WELCOME TO THE AGRO USSD SERVICE".center(100))
print(("============="*6).center(100))
#ask them who they are 
enter_as = input("Press 1 if you are a farmer \nPress 2 if you are a user")
if enter_as == "1":
    acc_status = input("press 1 if you have an account\nPress 2 if you do not have an account")
if acc_status == "1":
    user_Id= input("Please input your Agronumber")
    password_farmer= input("please input your password")

if acc_status == "2":
    user_name =input("What is your name")
    random_number = str(random.randint(1,1000))
    user_Id= user_name + random_number
    password_farmer= input("please input your password")
#i want to save userid and password in data base probably a csvfile

workspace = Path("workspace")
workspace.mkdir(exist_ok=True)
csv_file = Path.cwd()/workspace/"task1.csv"
def save_user(path,user_Id,password_farmer):
    participant_header = ['Name', "user_id" ,'Phone_Number',"password"]
    if path.exists()==True:
        with open(csv_file,"r",newline="", encoding="utf-8") as f:
            writer_len= list(csv.reader(f))
            print(writer_len)
        if len(writer_len) <=1 :
            with open(path,"w",newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f,fieldnames=participant_header)
                writer.writeheader()
                writer.writerow(dictionary)
    #     else:
    #         with open(path,"a",newline="", encoding="utf-8") as f:
    #             writer = csv.DictWriter(f,fieldnames=participant_header)
    #             writer.writeheader()
    #             writer.writerow(dictionary)
    # else:
    #     with open(path,"w",newline="", encoding="utf-8") as f:
    #         writer = csv.DictWriter(f,fieldnames=participant_header)
    #         writer.writeheader()
    #         writer.writerow(dictionary)


#its either they signin or login
#so i need to create a signin or login form for both user and farmer


# #list of thing to ask farmer
# ask= ["Name","Phone number", "location","farm size","primary crops"]
# user_details = {}
# for x in ask:
#     if x == "Phone number":
#         detail= int(input(f"Please input your {x}"))
#         while (len(str(detail))+1) <11 or (len(str(detail))+1) >11:
#             print("Invalid input!! Phone number needs to be 11 digits")
#             detail= int(input(f"Please input your {x} again"))
#         else:
#             user_details.update({x:detail})
#     elif x == "farm size":
#         detail= int(input(f"Please input your {x}"))

#     else:
#         detail=input(f"Please input your {x}")
#         user_details.update({x:detail})
    

# print(user_details)