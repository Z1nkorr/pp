def input_int(mes, left_side, right_side):
    is_cor_inp = False
    value = 0



    while is_cor_inp == False:
        try:
            value = int(input(mes))
            if value>=left_side and value<=right_side:
                is_cor_inp = True
            else:
                print("щобла-вобла.")
        except:
            print("ошибка")

    return value

def get_sum(a,b):
    return a + b

def print_sum(summa):
    print(f"summa = {summa}")

a = input_int("a: ",1,100)
b = input_int("b: ",1,100)

summa = get_sum(a,b)

print_sum(summa)