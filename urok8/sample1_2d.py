arr2d = []
rows_count = 5
cols_count = 5

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        if j <= i:
            arr2d[i].append(1)
        else:
            arr2d[i].append(0)

for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()