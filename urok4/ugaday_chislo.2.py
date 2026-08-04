import random

is_repeat = 0

is_repeat = True

while is_repeat == True:

    print("выбери режим: ")
    print("1. угадай число")
    print("2. загадай число")
    mode_choose = int(input("Номер режима: "))



    if mode_choose == 1:



        comp_num = 0
        user_num = 0
        att = 0
        left_side = 0
        right_side = 0
        level = 0

        print("Выберите уровень сложности: ")
        print("1. лёгкий (будешь отгадывать от 1 до 10)")
        print("2. средний (будешь отгадывать от 1 до 100)")
        print("3. сложный (будешь отгадывать от 1 до 1000)")

        level = int(input("введите номер уровня сложности: "))
        if level == 1:
            print("выбран лёгкий уровень сложности")
            left_side = 1
            right_side = 10
        elif level == 2:
            print("выбран средний уровень сложности")
            left_side = 1
            right_side = 100
        elif level == 3:
            print("выбран сложный уровень сложности")
            left_side = 1
            right_side = 1000
        else:
            print("такого уровня сложности нет")
            exit()


        is_correct_rand = False

        while is_correct_rand == False:
            comp_num = random.randint(left_side, right_side)

            if comp_num != 67:
                is_correct_rand = True

        print("Отгадай число")

        while user_num != comp_num:

            input_correct = False

            att += 1

            while input_correct == False:

                if user_num == 67: 
                    input_correct = True
                    print("иди помойся")
                    exit()

                if user_num == 777:
                    print("1200000 НА БАЛЛАНСЕ")
                    input_correct = True

                user_num = int(input(f"попытка:{att}, вводи от {left_side} до {right_side}: "))

                if user_num >= left_side and user_num <= right_side:
                    input_correct = True
                else:
                    ("Число выходит за рамки попробуй ещё раз")
                    
                if user_num > comp_num:
                    print("Введи поменьше")
                    right_side = user_num 
                elif user_num < comp_num:
                    print("Введи побольше")
                    left_side = user_num

        print("угадал")
        print(f"попыток потратил: {att}")
                
        if att == 1:
            print("да ты везучий")
        elif att >= 2 and att <= 4:
            print("хорош")
        elif att >= 5 and att <= 10:
            print("ну норм")
        else:
            print("лох")
            

        

    elif mode_choose == 2:

        comp_num = 0
        user_num = 0
        att = 0
        left_side = 0
        right_side = 0
        level = 0

        print("от скольки до скольки будешь загадывать?")
        left_side = int(input("от: "))
        right_side = int(input("до: "))

        user_num = int(input("загадай число: "))

        if user_num < left_side or user_num > right_side:
                print("загадывай не выходя за грани что ты выставил")

        input_correct = False

        while input_correct == False:

            if left_side > right_side or right_side < left_side:
                print("загадывай так чтобы число ОТ которого можно угадывать, было меньше числа ДО которого можно угадывать")
                input_correct = False
            
            comp_num = random.randint(left_side, right_side)

            
            print(f"вот мое число: {comp_num}")

            answer_2 = int(input("если я угадал нажми 1, если меньше 2, если больше 3: "))

            if answer_2 == 1 and user_num == comp_num: 
                print("Ура!")
                break
            elif answer_2 == 2 and user_num < comp_num:
                print("сейчас введу поменьше")
                right_side = comp_num
            elif answer_2 == 3 and user_num > comp_num:
                print("сейчас введу побольше")
                left_side = comp_num

            if left_side > user_num or right_side < user_num:
                print("да быть такого не может")
                break

            if comp_num == user_num or answer_2 == 1 and user_num != comp_num:
                ("ах ты лжец!")
                break

answer = input("Классно поиграли. Хочешь ещё? (y/n)")

if answer == "y":
    is_repeat = True
elif answer == "n":
    is_repeat = False