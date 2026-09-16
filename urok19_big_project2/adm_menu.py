from functions_book import *

def work_with_admin_menu(books: list[Book], loan_books: list[Book]):
        
    work_ad = True

    while work_ad == True:

        global session_active
        session_active = True

        print("\nМеню администратора",
            "1.Каталог книг",
            "2.Добавить книгу",
            "3.Удалить книгу",
            "4.Обновить книгу",
            "5.Все активные выдачи",
            "6.Принудительно вернуть книгу",
            "7.Выйти в главное меню",
            sep="\n"
        )
        choose_action = input_int("\nВыберите действие: ", 1, 9)

        if choose_action == 1:
            print_all_books(books)

        elif choose_action == 2:
            new_book = inp_book_data()
            new_book.id = get_next_book_id()
            add_book_to_list(books, new_book)

        elif choose_action == 3:
            search_id = input_int("\nВведите id книги которую хотите удалить: ", 1, 1000)
            delete_book_by_id(books, search_id)

        elif choose_action == 4:
            book = inp_book_data()
            search_id = input_int("Введите id книги которую хотите обновить: ", 1, 1000)
            update_book_by_id(books, book, search_id)

        elif choose_action == 5:
            print_loan_books(loan_books)

        elif choose_action == 6:
            delete_loan_book_by_id(loan_books)

        elif choose_action == 7:
            work_ad = False