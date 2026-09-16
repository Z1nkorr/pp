from functions_book import *
from menu import *

STANDART = 1
SIMPLIFIED = 2
COMPLICATED = 3

color = "\033[0m"
style = STANDART

def work_with_stud_menu(books: list[Book], loan_books: list[Book], now_acc: str):

    global color
    global style
    stl_fr = style
    color = "\033[0m"
    
    work_stud = True
    while work_stud == True:

        print_stud_menu(style, color)

        choose_action = input_int("\nВыберите действие: ", 1, 7)

        if choose_action == 1:
            print_all_books(books, style)
            input("Нажмите «enter»")

        elif choose_action == 2:
            print("\nНайти книгу по:",
                "1.Названию",
                "2.Автору",
                "3.Жанру",
                "4.Айди",
                sep="\n"
            )
            choose_action_find = input_int("\nВыберите действие: ",1,4)

            if choose_action_find == 1:
                parameter = input_str("\nВведите название книги которую хотите найти: ",1,100)
                found_books_by_type_parameter = find_books_by_type_parameter(books, choose_action_find, parameter)

            elif choose_action_find == 2:
                parameter = input_str("\nВведите автора книги которую хотите найти: ",1,100)
                found_books_by_type_parameter = find_books_by_type_parameter(books, choose_action_find, parameter)

            elif choose_action_find == 3:
                parameter = input_str("\nВведите жанр книги которую хотите найти: ",1,100)
                found_books_by_type_parameter = find_books_by_type_parameter(books, choose_action_find, parameter)

            elif choose_action_find == 4:

                search_id = input_int("Введите айди: ",1,10_000_000)
                print_book_header(style)
                print_single_book(get_book_by_id(books,search_id), stl_fr)
                print(f"{'-'*140}")
                

            if found_books_by_type_parameter != None:
                print_all_books(found_books_by_type_parameter, style)
                
            else:
                print("Ничего не нашлось.")

            input("Нажмите «enter»")
                

        elif choose_action == 3:
            issue_registration(books, now_acc, loan_books)
            input("Нажмите «enter»")

        elif choose_action == 4:
            print_loan_books_st(loan_books, now_acc, style)
            input("Нажмите «enter»")

        elif choose_action == 5:
            search_id = input_int("Введите id библиотечного абонемента по которому хотите вернуть книгу: ", 1, 1000)
            delete_loan_book_by_id_st(search_id, loan_books, now_acc)
            input("Нажмите «enter»")

        elif choose_action == 6:
            work_stud = False

        elif choose_action == 7:

            print_set(style)

            choose_action = input_int("\nВыберите действие: ", 1, 2)

            if choose_action == 1:
                print("1.Красный",
                    "2.Зелёный",
                    "3.Желтый",
                    "4.Вернуть стандартный",
                    sep="\n"  
                    )
        
                choose_act = input_int("\nВыберите действие: ", 1, 4)
                color = switch_color(choose_act)

            elif choose_action == 2:
                print("1.Стандартный",
                    "2.Упрощённый",
                    "3.Усложненный",
                    sep="\n"  
                    )  

                choose_act = input_int("\nВыберите действие: ", 1, 3)

                if choose_act == 1:
                    style = STANDART
                elif choose_act == 2:
                    style = SIMPLIFIED
                elif choose_act == 3:
                    style = COMPLICATED

            input("Нажмите «enter»")
                        