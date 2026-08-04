import random

workers = int(input("ввелите кол-во сотрудников: "))

salsa = []

for _ in range(workers):
    salsa.append(random.randint(50000, 150000))

for i in range(workers):
    print(f"Сотрудник №{i+1} зп - {salsa[i]} руб.")

print("==============")

print("сотрудники с зп больше 100000руб.")

for i in range(workers):
    if salsa[i] > 100_000:
        print(f"Сотрудник №{i+1} зп - {salsa[i]} руб.")
