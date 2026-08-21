from lib_functions_Book import *
from lib_functions_Acc import *
from lib_loans import *
from lib_console_helper import *
from library import *
import pickle
import shutil
from datetime import date, time, datetime

books: list[Book] = load_books_from_pkl_file("books.pkl")
accounts: list[Account] = load_accounts_from_pkl_file("accounts.pkl")
loans: list[LoanRecord] = load_loans_from_pkl_file("loans.pkl")

if len(accounts) == 0:
    acc1=Account(
        username="admin",
        password="12345",
        acc_id=get_next_acc_id(),
        loan_records=[],
        count_records=0
    )
    acc2=Account(
        username="Aleksey_12",
        password="123qwe",
        acc_id=get_next_acc_id(),
        loan_records=[],
        count_records=0
    )
    accounts = [acc1, acc2]
    save_accounts_to_pkl_file(accounts)

if len(books) == 0:

    book1=Book(
        id=get_next_book_id(),
        title="Гарри Поттер и философский камень",
        author="Дж. К. Роулинг",
        genre="Фэнтези",
        total_copies=3,
        available_copies=2,
        rating=4.9
    )
    book2=Book(
        id=get_next_book_id(),
        title="1984",
        author="Джордж Оруэлл",
        genre="Антиутопия",
        total_copies=2,
        available_copies=1,
        rating=4.8
    )
    book3=Book(
        id=get_next_book_id(),
        title="Маленький принц",
        author="Антуан де Сент-Экзюпери",
        genre="Сказка",
        total_copies=4,
        available_copies=4,
        rating=5.0
    )
    book4=Book(
        id=get_next_book_id(),
        title="Преступление и наказание",
        author="Ф. М. Достоевский",
        genre="Классическая проза",
        total_copies=3,
        available_copies=3,
        rating=4.7
    )
    book5=Book(
        id=get_next_book_id(),
        title="Мастер и Маргарита",
        author="М. А. Булгаков",
        genre="Мистика",
        total_copies=5,
        available_copies=3,
        rating=4.9
    )
    book6=Book(
        id=get_next_book_id(),
        title="Властелин колец",
        author="Дж. Р. Р. Толкин",
        genre="Фэнтези",
        total_copies=2,
        available_copies=1,
        rating=5.0
    )
    books = [book1, book2, book3, book4, book5, book6]
    save_books_to_pkl_file(books)

global_book_id = update_get_next_book_id(books)
global_acc_id = update_get_next_acc_id(accounts)
global_loan_id = update_get_next_loan_id(loans)
max_book_id = 0

session_active = False

is_run = True

def issue_registration(books: list[Book]):

    search_id = input_int("\nВведите id книги которую хотите оформить: ", 1, 1000)
    book_loan = get_book_by_id(books, search_id)

    if book_loan != None:
        loan_create = input_LoanRec_data(book_loan.id, now_acc)
        if input_LoanRec_data(book_loan.id, now_acc):
            print(f"Запись успешно создана на ваш аккаунт. Книгу «{book_loan.title}» придеться вернуть через 14 дней.")
            book_loan.available_copies -= 1
            now_acc.loan_records.append(loan_create)
            add_loan_to_list(loans, loan_create)
        else:
            print("Ошибка, запись не создана.")
    else:
        print("\nУвы, книги с таким id не оказалось")



def work_with_stud_menu():
    
    work_stud = True
    while work_stud == True:

        global session_active
        global now_acc

        session_active = True

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
            issue_registration(books)

        elif choose_action == 4:
            print_all_loans_stud(now_acc)

        elif choose_action == 5:
            search_id = input_int("Введите id библиотечного абонемента по которому хотите вернуть книгу: ", 1, 1000)
            delete_loan_by_id_stud(now_acc, search_id, books)

        elif choose_action == 6:
            work_stud = False

        elif choose_action == 7:

            delete_cycle = True

            while delete_cycle == True:

                delete_acc_inp = input_str("Вы уверены? y/n: ", 1, 1)

                if delete_acc_inp == "y":

                    delete_acc_by_id(accounts, now_acc.acc_id)
                    session_active = False
                    work_stud = False
                    delete_cycle = False
                    now_acc = None

                elif delete_acc_inp == "n":

                    delete_cycle = False

                else:
                    print("Введите y/n.")


def work_with_admin_menu():
        
    work_ad = True

    while work_ad == True:

        global session_active
        session_active = True

        print("\nМеню администратора",
            "1.Каталог книг",
            "2.Список аккаунтов",
            "3.Удалить аккаунт из списка",
            "4.Добавить книгу",
            "5.Удалить книгу",
            "6.Обновить книгу",
            "7.Все активные выдачи",
            "8.Принудительно вернуть книгу",
            "9.Выйти в главное меню",
            sep="\n"
        )
        choose_action = input_int("\nВыберите действие: ", 1, 9)

        if choose_action == 1:
            print_all_books(books)

        elif choose_action == 2:
            print_all_accounts(accounts)

        elif choose_action == 3:

            acc_id = input_int("\nВведите id аккаунта который хотите удалить: ", 1, 1000)

            delete_acc_by_id(accounts,acc_id)

        elif choose_action == 4:
            new_book = inp_book_data()
            new_book.id = get_next_book_id()
            add_book_to_list(books, new_book)

        elif choose_action == 5:
            search_id = input_int("\nВведите id книги которую хотите удалить: ", 1, 1000)
            delete_book_by_id(books, search_id)

        elif choose_action == 6:
            book = inp_book_data()
            search_id = input_int("Введите id книги которую хотите обновить: ", 1, 1000)
            update_book_by_id(books, book, search_id)

        elif choose_action == 7:
            print_all_loans(loans)

        elif choose_action == 8:
            delete_loan_by_id(loans)

        elif choose_action == 9:
            work_ad = False

def add_new_book():
    new_book = inp_book_data()
    add_book_to_list(books, new_book)

def add_new_acc_sign_in():
    global now_acc
    now_acc = sign_in(accounts)
    add_acc_to_list(accounts, now_acc)

def add_new_acc_log_in():
    global now_acc
    now_acc = log_in(accounts)

def print_main_menu():

    global session_active

    if session_active == False:
        text = [
            "Добро пожаловать в электронную версию школьной библиотеки!", 
            "1. Зарегистрироваться", 
            "2. Войти",
            "3. Выйти из программы",
        ]
        try:
            width = shutil.get_terminal_size().column
            if width == 0:
                width = 130
        except Exception:
            width = 130

        for i in text:
            print(i.center(width))
    else:
        text = [            
            "Добро пожаловать в электронную версию школьной библиотеки!",  
            "1. Вернуться",
            "2. Выйти из аккаунта",
            "3. Выйти из программы",
        ]
        try:
            width = shutil.get_terminal_size().column
            if width == 0:
                width = 130
        except Exception:
            width = 130

        for i in text:
            print(i.center(width))

is_run = True

while is_run:
    
    print_main_menu()
    if session_active == False:
        choose_action = input_int("\nВыберите действие: ", 1, 3)
    else:
        choose_action = input_int("\nВыберите действие: ", 1, 3)

    if choose_action == 1 and session_active == False:
        add_new_acc_sign_in()
        work_with_stud_menu()

    elif choose_action == 1 and session_active == True:
        if now_acc is not None and now_acc.username == "admin":
            work_with_admin_menu()
        elif now_acc is not None:
            work_with_stud_menu()

    elif choose_action == 2 and session_active == False:
        add_new_acc_log_in()
        if now_acc is not None and now_acc.username == "admin":
            work_with_admin_menu()
        elif now_acc is not None:
            work_with_stud_menu()
        else:
            print("Вход не выполнен.")

    elif choose_action == 2 and session_active == True:
        now_acc = None
        session_active = False
        print("\n"*45)

    elif choose_action == 3 and session_active == False:
        is_run = False

    elif choose_action == 3 and session_active == True:
        is_run = False

if save_books_to_pkl_file(books, "books.pkl"):
    print("Книги сохранены.")
else:
    print("Не удалось сохранить книги.")

if save_accounts_to_pkl_file(accounts, "accounts.pkl"):
    print("Аккаунты сохранены.")
else:
    print("Не удалось сохранить аккаунты.")

if save_loans_to_pkl_file(loans, "loans.pkl"):
    print("Записи сохранены.")
else:
    print("Не удалось сохранить записи.")

print("До свидания!")