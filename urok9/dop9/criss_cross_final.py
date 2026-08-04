import random

CRISS_SYMBOL = "X"
CROSS_SYMBOL = "0"
EMPTY_CELL = "."

USER_PLAYER = "user_player"
COMP_PLAYER = "comp_player"
DRAW = "draw"

SIZE_FIELD = 3
filled_cells = 0

player_symbol = "."
comp_symbol = "."

current_player = ""
winner_player = ""

field = []

print("крестики нолики")

for i in range(SIZE_FIELD):
    field.append([])
    for j in range(SIZE_FIELD):
        field[i].append(EMPTY_CELL)

first_player = random.choice(["игрок", "компьютер"])
if first_player == "игрок":
    player_symbol = CRISS_SYMBOL
    comp_symbol = CROSS_SYMBOL
    current_player = USER_PLAYER
else:
    player_symbol = CROSS_SYMBOL
    comp_symbol = CRISS_SYMBOL
    current_player = COMP_PLAYER

game_still_playing = True

while game_still_playing == True:

    for i in range(SIZE_FIELD):
        for j in range(SIZE_FIELD):
            print(f"{field[i][j]:2}", end="")
        print()

    if current_player == USER_PLAYER:
        print("Ход игрока:")

        i_symbol = int((input("введите номер строки для ввода: "))) - 1
        j_symbol = int((input("введите номер столбца для ввода: "))) - 1

        if field[i_symbol][j_symbol] == EMPTY_CELL:
            field[i_symbol][j_symbol] = player_symbol
        filled_cells += 1
        current_player = COMP_PLAYER
        is_correct_inp = True

    elif current_player == COMP_PLAYER:
        print("ход компьютера")
        i_symbol_2 = random.randint(0, SIZE_FIELD-1)
        j_symbol_2 = random.randint(0, SIZE_FIELD-1)

        if field[i_symbol_2][j_symbol_2] == EMPTY_CELL:
            field[i_symbol_2][j_symbol_2] = comp_symbol
            filled_cells += 1
            current_player = USER_PLAYER

    if (
        field[0][0] == player_symbol
        and field[0][1] == player_symbol
        and field[0][2] == player_symbol
        or field[1][0] == player_symbol
        and field[1][1] == player_symbol
        and field[1][2] == player_symbol
        or field[2][0] == player_symbol
        and field[2][1] == player_symbol
        and field[2][2] == player_symbol
        or field[0][0] == player_symbol
        and field[1][0] == player_symbol
        and field[2][0] == player_symbol
        or field[0][1] == player_symbol
        and field[1][1] == player_symbol
        and field[2][1] == player_symbol
        or field[0][2] == player_symbol
        and field[1][2] == player_symbol
        and field[2][2] == player_symbol
        or field[0][0] == player_symbol
        and field[1][1] == player_symbol
        and field[2][2] == player_symbol
        or field[0][2] == player_symbol
        and field[1][1] == player_symbol
        and field[2][0] == player_symbol
    ):
        winner_player = USER_PLAYER
        game_still_playing = False
    elif (
        field[0][0] == comp_symbol
        and field[0][1] == comp_symbol
        and field[0][2] == comp_symbol
        or field[1][0] == comp_symbol
        and field[1][1] == comp_symbol
        and field[1][2] == comp_symbol
        or field[2][0] == comp_symbol
        and field[2][1] == comp_symbol
        and field[2][2] == comp_symbol
        or field[0][0] == comp_symbol
        and field[1][0] == comp_symbol
        and field[2][0] == comp_symbol
        or field[0][1] == comp_symbol
        and field[1][1] == comp_symbol
        and field[2][1] == comp_symbol
        or field[0][2] == comp_symbol
        and field[1][2] == comp_symbol
        and field[2][2] == comp_symbol
        or field[0][0] == comp_symbol
        and field[1][1] == comp_symbol
        and field[2][2] == comp_symbol
        or field[0][2] == comp_symbol
        and field[1][1] == comp_symbol
        and field[2][0] == comp_symbol
    ):
        winner_player = COMP_PLAYER
        game_still_playing = False
    elif filled_cells == 9:
        winner_player = DRAW
        game_still_playing = False

print(f"Game is over. Winner {winner_player}")