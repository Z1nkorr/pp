users_countries = ["Russia", "RUSSIA", "russia", "RuSsiA"]

count_from_Russia = 0

for i in range(len(users_countries)):
    if users_countries[i].upper() == "russia".upper():
        count_from_Russia += 1

    print(f"count from Russia = {count_from_Russia}")