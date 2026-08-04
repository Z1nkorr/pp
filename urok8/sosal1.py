import random

arr2d = []
rows_count = 3
cols_count = 3

# for i in range(10):
#     arr2d.append(random.randint(1,100))

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        arr2d[i].append(random.randint(1, 100))

for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()
