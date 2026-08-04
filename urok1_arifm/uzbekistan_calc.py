floor = 0

steps_in_floor = 0

SEC_IN_STEP = 10

STAIRS_IN_FLOOR = 2

result_in_sec = 0

mins = 0

secs = 0


floor = int(input("на какой этаж поднялся: "))


steps_in_floor = int(input("введите кол-во ступенек в пролёте: "))


result_in_sec = floor * STAIRS_IN_FLOOR * steps_in_floor * SEC_IN_STEP


mins = result_in_sec // 60

secs = result_in_sec % 60


print(f"ваша жизнь увеличилась на {mins} мин. и {secs} сек.")
