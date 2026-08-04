import random

right_side = 500

comp_number = random.randint(1, right_side)

print(f"я загадал число от 1 до {right_side}, попрогуй отгадай число")

is_guessed = False

while is_guessed == False:
    user_number = int(input(f"введите своё число от 1 до {right_side}: "))

    if user_number < comp_number:
        print("введи побольше")
    elif user_number > comp_number:
        print("введи поменьше")
    elif user_number == comp_number:
        print("ты угадал")
        is_guessed = True