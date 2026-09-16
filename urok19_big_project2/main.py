from functions_book import *
from console_helper import *
from library import *
from stud_menu import *
from adm_menu import *
from menu import *

books: list[Book] = load_books_from_txt_file("books.txt")
loan_books: list[Book] = load_loans_from_list_bk(books)

if len(books) == 0:

    book1 = Book(
        id=get_next_book_id(),
        title="Гарри Поттер и философский камень",
        author="Дж. К. Роулинг",
        genre="Фэнтези",
        available=True,
        rating=4.9
    )

    book2 = Book(
        id=get_next_book_id(),
        title="1984",
        author="Джордж Оруэлл",
        genre="Антиутопия",
        available=True,
        rating=4.8
    )

    book3 = Book(
        id=get_next_book_id(),
        title="Маленький принц",
        author="Антуан де Сент-Экзюпери",
        genre="Сказка",
        available=True,
        rating=5.0
    )

    book4 = Book(
        id=get_next_book_id(),
        title="Преступление и наказание",
        author="Ф. М. Достоевский",
        genre="Классическая проза",
        available=True,
        rating=4.7
    )

    book5 = Book(
        id=get_next_book_id(),
        title="Мастер и Маргарита",
        author="М. А. Булгаков",
        genre="Мистика",
        available=True,
        rating=4.9
    )

    book6 = Book(
        id=get_next_book_id(),
        title="Властелин колец",
        author="Дж. Р. Р. Толкин",
        genre="Фэнтези",
        available=True,
        rating=5.0
    )

    books = [book1, book2, book3, book4, book5, book6]
    save_books_to_txt_file(books, "books.txt")

max_book_id = 0

session_active = False

is_run = True

while is_run == True:
    
    print_main_menu(session_active)
    choose_action = input_int("\nВыберите действие: ", 1, 3)

    if choose_action == 1 and session_active == False:
            now_acc = input_str("Введите свое имя: ", 1, 30)
            session_active = True
            work_with_stud_menu(books, loan_books, now_acc)

    elif choose_action == 1 and session_active == True:
        
        if now_acc == "admin":
            work_with_admin_menu(books, loan_books)
        else:
            work_with_stud_menu(books, loan_books, now_acc)

    elif choose_action == 2 and session_active == False:
        passw = input_str("Введите пароль: ", 1, 20)
        if passw == "12345":
            work_with_admin_menu(books, loan_books)
            session_active = True
        else:
            print("Вход не выполнен.")

    elif choose_action == 2 and session_active == True:
        now_acc = None
        session_active = False
        print("\n"*45)

    elif choose_action == 3:
        is_run = False

if save_books_to_txt_file(books, "books.pkl"):
    print("Книги сохранены.")
else:
    print("Не удалось сохранить книги.")

print("До свидания!")