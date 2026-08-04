import random

sal = []
sal_count = 10

for _ in range(sal_count):
    sal.append(random.randint(30, 150))

print(sal)

sum_sal = 0

for i in range(sal_count):
    sum_sal += sal[i]
    avg_sal = sum_sal / sal_count

print(f"sum_sal = {sum_sal}")
print("------------")
print(f"avg_sal = {avg_sal}")

is_sort = False
temp = 0
offset = 0

while is_sort == False:
    is_sort = True

    for i in range(sal_count - offset):
        if sal[i + 1] < sal[i]:
            temp = sal[i]
            sal[i + 1] = sal[i]
            sal[i] = temp
            is_sort = False

print("------------")
print(sal)