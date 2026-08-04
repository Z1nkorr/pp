number = int(input("введи число: "))
sum_del = 0
i = 0 
right_side = number // 2
while right_side < number:
    i+=1
    if number % i == 0:
        sum_del += 1

    if number == sum_del:
        print(f"число {number} совершенное")
    else:
        print(f"число {number} несовершенное")