from pathlib import Path
import csv
import random

from users import farmers 
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

randnum_used = [] # this need to be replaced with a file so that it doesnt get lost when program rerun 
if acc_status == "2":
    signup_status=farmers.sign_up()
    if signup_status == "SUCCESS":
        farmers.register_farm()
#its either they signin or login
#so i need to create a signin or login form for both user and farmer


