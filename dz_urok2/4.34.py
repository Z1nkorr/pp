a = int(input("введи число: "))
b = int(input("введи ещё одно: "))

if a % b == 0:
    print("b является делителем a")
else:
    print("b не является делителем a")

if b % a == 0:
    print("a является делителем b")
else:
    print("a не является делителем b")