import random


def add_elem_to_end(elem, arr):
    arr.append(elem)


arr = []
count_elems = 5

for _ in range(count_elems):
    arr.append(random.randint(1,100))

print(f"M {arr}")

add_elem_to_end(999, arr)

print(f"M {arr}")
