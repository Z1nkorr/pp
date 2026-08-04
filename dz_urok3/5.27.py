a = int(input("введите число от которого начнется сложение: "))
b = int(input("введите число на котором закончится сложение: "))
i = a
total_sum = 0

while i <= b:
    total_sum += i
    i += 1

print(total_sum)