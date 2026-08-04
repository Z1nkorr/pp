login = input("Введите логин: ")
login_db = "Z1nkorr"

login = login.strip("- ")

if login == login_db:
    print("auth is correct")
else:
    print("auth err")