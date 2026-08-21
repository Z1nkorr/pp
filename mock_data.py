import pickle

if len(accounts) == 0:
    acc1=Account(
        username="admin",
        password="12345",
        acc_id=get_next_acc_id(),
    )
    acc2=Account(
        username="Aleksey_12",
        password="123qwe",
        acc_id=get_next_acc_id(),
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
        available_copies=0,
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