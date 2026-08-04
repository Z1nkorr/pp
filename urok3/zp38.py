i = 0
N = 10
distance_from_home = 0
total_distance = 0

while i < N:
    i += 1

    current_distance = 1 / i

    if i % 2 != 0:
        distance_from_home += current_distance
    else:
        distance_from_home -= current_distance

    total_distance += current_distance

print(f"дистанция от дома = {distance_from_home:.2f}")
print(f"общая дистанция = {total_distance:.2f}")