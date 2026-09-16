from datetime import date,datetime,time

def input_int(mes:str,min_val:int,max_val:int) -> int:
    is_cor_inp=False
    input_int=0

    while is_cor_inp==False:
        try:
            input_int = int(input(mes).strip(" "))

            if input_int < min_val or input_int > max_val:
                print(
                    "Ошибка ввода"
                )
            else:
                is_cor_inp=True
        except:
            print("Ошибка ввода")

    return input_int

def input_str(mes:str,min_len:int,max_len:int)->str:
    is_cor_inp=False

    while is_cor_inp==False:
        input_str=input(mes)

        if len(input_str)<min_len or len(input_str)>max_len:
            print(f"Ошибка ввода. Длинна должна быть от {min_len} до {max_len}")

        else:
            is_cor_inp=True

    return input_str

def input_float(mes:str,min_val:int,max_val:int)->float:
    is_cor_inp=False
    input_float=0

    while is_cor_inp==False:
        try:
            input_float = float(input(mes).strip(" "))

            if input_float < min_val or input_float > max_val:
                print(
                    "Ошибка ввода"
                )
            else:
                is_cor_inp=True
        except:
            print("Ошибка ввода")

    return input_float