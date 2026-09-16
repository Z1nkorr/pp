from functions_book import *

def work_with_stud_menu(books: list[Book], loan_books: list[Book], now_acc: str):
    
    work_stud = True
    while work_stud == True:

        print("\nМеню студента",
            "1.Каталог книг",
            "2.Поиск книг",
            "3.Оформить выдачу",
            "4.Мои активные выдачи",
            "5.Вернуть книгу",
            "6.Выйти в главное меню",
            "7.Удалить свой аккаунт",
            sep="\n"
        )   
        choose_action = input_int("\nВыберите действие: ", 1, 7)

        if choose_action == 1:
            print_all_books(books)

        elif choose_action == 2:
            print("\nНайти книгу по:",
                "1.Названию",
                "2.Автору",
                "3.Жанру",
                sep="\n"
            )
            choose_action_find = input_int("\nВыберите действие: ",1,3)

            if choose_action_find == 1:
                parameter = input("\nВведите название книги которую хотите найти: ")

            elif choose_action_find == 2:
                parameter = input("\nВведите автора книги которую хотите найти: ")

            elif choose_action_find == 3:
                parameter = input("\nВведите жанр книги которую хотите найти: ")

            found_books_by_type_parameter = find_books_by_type_parameter(books, choose_action_find, parameter)

            if found_books_by_type_parameter != None:

                print_all_books(found_books_by_type_parameter)

            else:
                print("Ничего не нашлось.")

        elif choose_action == 3:
            issue_registration(books, now_acc, loan_books)

        elif choose_action == 4:
            print_loan_books_st(loan_books, now_acc)

        elif choose_action == 5:
            search_id = input_int("Введите id библиотечного абонемента по которому хотите вернуть книгу: ", 1, 1000)
            delete_loan_book_by_id_st(search_id, loan_books, now_acc)

        elif choose_action == 6:
            work_stud = False