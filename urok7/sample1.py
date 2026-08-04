import random
count_it = 10
it = []

for _ in range(count_it):
    it.append(random.randint(1,100))

print(it)

index1 = int(input("введите индекс 1-го элемента для замены"))
index2 = int(input("введите индекс 2-го элемента для замены"))

it.insert(index1+2, it[index1])
it.pop(index1)
print(it)

