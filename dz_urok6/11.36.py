import random

kolvo_chisel = int(input("ввелите кол-во чисел: "))

massive = []

for _ in range(kolvo_chisel):
    massive.append(random.randint(-100, 500))

for i in range(kolvo_chisel):
    print(f"Число №{i+1} - {massive[i]}")

print("==============")

print("числа не превышающие 100")

for i in range(kolvo_chisel):
    if massive[i] < 100:
        print(f"Число №{i+1} - {massive[i]}")