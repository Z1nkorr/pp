year = int(input("какой год: "))

if year % 400 == 0:
    print("это високосный год")
    exit()

elif year % 4 == 0 and year % 100 != 0:
    print("это високосный год")

else:
    print("это не високосный год")