k = int(input("какой день от 1 до 365: "))
1<=k<=365

if k > 365 or k < 1:
    print("введи от 1 до 365")
    exit()

if (k - 1) % 7 < 5:  
    print("рабочий")
else:
    print("выходной")