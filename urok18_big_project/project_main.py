
def print_main_menu():
    pass

def work_with_buyer_menu():
    pass

def auth_is_admin():
    pass

def work_with_admin_menu():
    pass

is_run = True

while is_run == True:
    
    print_main_menu()

    choose_action_main_menu = int(input())

    if choose_action_main_menu == 1:
        work_with_buyer_menu()

    elif choose_action_main_menu == 2:
        if auth_is_admin() == True:
            work_with_admin_menu()
        elif auth_is_admin == False:
            print("Ошибка неверный пароль")

    elif choose_action_main_menu == 3:
        is_run = False
