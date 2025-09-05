from pathlib import Path
folder = Path("agro_ussd/data")
path = folder / "users.csv"
def login(name, password):
    with open(path, "r", encoding="utf-8") as file:
        content = file.readlines()
        
    