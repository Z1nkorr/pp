import random

ALIVE_SHIP = "K"
DEAD_SHIP = "X"
MISS_CELL = "O"
EMPTY_CELL = "."

USER_PLAYER = "игрок"
COMP_PLAYER = "комп"

answer = "y"

while answer == "y":

    size_field = 0
    user_count_alive_ships = 0
    comp_count_alive_ships = 0

    user_field = []
    comp_field = []

    current_player = ""
    winner_player = ""

    is_correct_input = False

    while is_correct_input == False:
        
        try:
            size_field = int(input("введите размеры игрового поля (от 3 до 10): "))
            print()

            if size_field >= 3 and size_field <= 10:
                is_correct_input = True
            else:
                print("Ошибка. Вы ввели неверные размеры поля.")
        except:
            print("Ошибка. Вы ввели не число.")        

    user_count_alive_ships = comp_count_alive_ships = size_field

    for i in range(size_field):
        user_field.append([])
        for j in range(size_field):
            user_field[i].append(EMPTY_CELL)

    for i in range(size_field):
        comp_field.append([])
        for j in range(size_field):
            comp_field[i].append(EMPTY_CELL)

    for _ in range(user_count_alive_ships):

        i_ship = 0
        j_ship = 0
        is_correct_place = False

        while is_correct_place == False:

            i_ship = random.randint(0, size_field - 1)
            j_ship = random.randint(0, size_field - 1)

            if user_field[i_ship][j_ship] == EMPTY_CELL:
                is_correct_place = True

        user_field[i_ship][j_ship] = ALIVE_SHIP


    for _ in range(comp_count_alive_ships):

        i_ship = 0
        j_ship = 0
        is_correct_place = False

        while is_correct_place == False:

            i_ship = random.randint(0, size_field - 1)
            j_ship = random.randint(0, size_field - 1)

            if comp_field[i_ship][j_ship] == EMPTY_CELL:
                is_correct_place = True

        comp_field[i_ship][j_ship] = ALIVE_SHIP

    if random.randint(1, 1000) <= 500:
        current_player = USER_PLAYER
        print("Первым ходит игрок")

    else:
        current_player = COMP_PLAYER
        print("Первым ходит компьютер")

    is_playing = True

    current_round = 0

    print()
    print("*" * 20)
    print()

    while is_playing == True:

        current_round += 1

        print(f"Раунд №{current_round}")

        print()
        print("=" * 20)
        print()

        print("Поле игрока:")
        for i in range(size_field):
            for j in range(size_field):
                print(f"{user_field[i][j]:2}", end="")
            print()

        print()
        print("-" * 20)
        print()

        print("Поле компьютера:")
        for i in range(size_field):
            for j in range(size_field):
                if comp_field[i][j] == ALIVE_SHIP:
                    print(f"{EMPTY_CELL:2}", end="")
                else:
                    print(f"{comp_field[i][j]:2}", end="")
            print()

        if current_player == USER_PLAYER:
            print("Ход игрока:")
            print()

            cor_inp = False

            while cor_inp == False:

                try:
                    i_shoot = int((input("Введите номер строки для выстрела: "))) - 1
                    j_shoot = int((input("Введите номер столбца для выстрела: "))) - 1

                    if (
                        i_shoot >= 0
                        and i_shoot <= size_field - 1
                        and j_shoot >= 0
                        and j_shoot <= size_field - 1
                    ):
                        if (
                            comp_field[i_shoot][j_shoot] == ALIVE_SHIP
                            or comp_field[i_shoot][j_shoot] == EMPTY_CELL
                        ):
                            cor_inp = True
                        else:
                            print("Ошибка. Вы уже стреляли в эту клетку.")
                    else:
                        print("Ошибка. Вы ввели клетку за пределами поля.")
                except:
                    print("Ошибка. Вы ввели не число.")

            if i_shoot <= size_field or j_shoot <= size_field and i_shoot >= 1 or j_shoot >= 1:
                cor_inp = True

            if comp_field[i_shoot][j_shoot] == ALIVE_SHIP:
                comp_field[i_shoot][j_shoot] = DEAD_SHIP
                comp_count_alive_ships -= 1

            elif comp_field[i_shoot][j_shoot] == EMPTY_CELL:
                comp_field[i_shoot][j_shoot] = MISS_CELL
                current_player = COMP_PLAYER

        elif current_player == COMP_PLAYER:

            print("Ход компьютера:")
            print()

            cor_inp = False

            while cor_inp == False:

                i_shoot = random.randint(0, size_field - 1)
                j_shoot = random.randint(0, size_field - 1)

                if (
                    user_field[i_shoot][j_shoot] == ALIVE_SHIP
                    or user_field[i_shoot][j_shoot] == EMPTY_CELL
                    ):
                    cor_inp = True

            print(f"Комп выстрелил по координатам ({i_shoot + 1}; {j_shoot + 1})")
            print()

            if user_field[i_shoot][j_shoot] == ALIVE_SHIP:
                user_field[i_shoot][j_shoot] = DEAD_SHIP
                user_count_alive_ships -= 1

            elif user_field[i_shoot][j_shoot] == EMPTY_CELL:
                user_field[i_shoot][j_shoot] = MISS_CELL
                current_player = USER_PLAYER

        if user_count_alive_ships == 0:
            winner_player = COMP_PLAYER
            is_playing = False

        elif comp_count_alive_ships == 0:
            winner_player = USER_PLAYER
            is_playing = False

        print()
        print("*" * 20)
        print()

        input("Для продолжения нажмите клавишу <Enter>")
        print()

    print(f"Игра окончена. Победил {winner_player}")

    cor_inp = False

    while cor_inp == False:

        answer = input("Хотите сыграть ещё? (y/n)")

        if answer == "y" or answer == "n":
            cor_inp = True
        else:
            print("Ошибка. Вы ввели неккоректный ответ.")