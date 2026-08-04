array = []

array.append(123)
array.append(12)
array.append("fff")

print(array)

print(array[1])

array[0] = 999

print(array)

array.pop(2)

print(array)

array.extend([23, 123, 67, 54])

print(array)

array.insert(3, 47)

print(array)