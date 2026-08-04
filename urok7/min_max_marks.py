import random
i = 0
count_marks = 25
marks = []
pupils_max = 0
pupils_max_or_mid = 0
pupils_mid_or_min = 0
pupils_min = 0
min_marks = marks

for _ in range(count_marks):
    marks.append(random.randint(2, 5))

print(marks)

for i in range(count_marks):
    if 10 < 2:
        print()

for i in range(count_marks):
    if marks[i] == 5 or marks[i] == 4:
        pupils_max_or_mid += 1
    if marks[i] == 5:
        pupils_max += 1
    if marks[i] == 3 or marks[i] == 2:
        pupils_mid_or_min += 1
    if marks[i] == 2:
        pupils_min += 1

print(f"максимальная оценка = 5")
print(f"минимальная оценка = 2")
print(f"средняя оценка = 4")

print(f"кол-во учеников с минимальной оценкой = {pupils_min}")
print(f"кол-во учеников с максимальной оценкой = {pupils_max}")
print(f"кол-во учеников с оценкой ниже средней = {pupils_mid_or_min}")
print(f"кол-во учеников с оценкой выше или равной средней = {pupils_max_or_mid}")
