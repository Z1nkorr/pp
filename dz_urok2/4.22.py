chislo = int(input("Введи любое натуральное число: "))

if chislo <= 0:
    print("это не натуральное число")
    exit()

if chislo % 2 == 0:
    print("это четное число")
else:
    print("это нечетное число")

if chislo % 10 == 7:
    print("это число оканчивается на 7")