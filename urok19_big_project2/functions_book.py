from library import *
from console_helper import *
from datetime import timedelta, date

BOOKS_FILE = "books.pkl"

global_book_id = 0

def update_get_next_book_id(id: int) -> int:

    global global_book_id

    global_book_id = id
        
    return global_book_id

def inp_book_data() -> Book:

    title = input_str("Введите название книги: ",1,40)
    author = input_str("Введите автора книги: ",1,25)
    genre = input_str("Введите жанр: ", 1, 20)
    stud_name = None
    available = True
    rating = input_float("Введите рейтинг книги: ",1,5)

    return Book(
        id = 0,
        title = title,
        author = author,
        genre = genre,
        stud_name = stud_name,
        available = available,
        rating = rating,
    )

def get_next_book_id() -> int:

    global global_book_id

    global_book_id += 1

    return(global_book_id)

def get_book_by_id(books: list[Book], search_id: int) -> Book | None:
    for book in books:
        if book.id == search_id:
            return book
    return None

def add_book_to_list(books: list[Book], new_book: Book):
    books.append(new_book)

def update_book_by_id(books: list[Book], book: Book, search_id: int) -> bool:
    find_book = get_book_by_id(books, search_id)
    if find_book is None:
        return False
    find_book.title = book.title
    find_book.author = book.author
    find_book.genre = book.genre
    find_book.available = book.available
    find_book.stud_name = book.stud_name
    find_book.rating = book.rating
    return True

def delete_book_by_id(books: list[Book], search_id: int) -> bool:
    find_book = get_book_by_id(books, search_id)
    if find_book.id != None:
        books.remove(find_book)
        return True
    return False

def issue_registration(books: list[Book], now_acc: str, loan_books: list[Book]):

    search_id = input_int("\nВведите id книги которую хотите оформить: ", 1, 1000)
    book_loan = get_book_by_id(books, search_id)
    td = timedelta(days=14)
    issue_date = date.today() + td

    if book_loan != None:
        print(f"Книга успешно забронирована.\nБронь продлится до {issue_date} После книгу «{book_loan.title}» придеться вернуть через 14 дней.")
        book_loan.stud_name = now_acc
        loan_books.append(book_loan)
        book_loan.available = False
    else:
        print("\nУвы, книги с таким id не оказалось")

def print_single_book(book: Book):
    if book.available == True:
        book_available = "Есть"
    else:
        book_available = "Нет в наличии"

    if book.stud_name == None:
        st_name = "Нет"
    else:
        st_name = book.stud_name
    
    print(
        f"{(book.id):<5}"
        f"{book.title:<40}"
        f"{book.author:<25}"
        f"{book.genre:<20}"
        f"{st_name:<20}"
        f"{book_available:<17}"
        f"{book.rating:<5}"
    )

def print_book_header():
    print("\n"
        f"{'ИД':<5}"
        f"{'Название':<40}"
        f"{'Автор':<25}"
        f"{'Жанр':<20}"
        f"{'Имя студента':<20}"
        f"{'Есть в наличии':<17}"
        f"{'Рейтинг':<5}"
    )

def print_all_books(books: list[Book]):
    if len(books) > 0:
        print_book_header()
        for book in books:
            print_single_book(book)
            print(f"{'-'*140}")
    else:
        print("Книг нет в ассортименте")

def sort_books_by_type_sort(books: list[Book], type_sort: int):
    pass

def find_books_by_type_parameter(
    books: list[Book], type_parameter: int, parameter: str
) -> list[Book]:

    result = []
    param_lower = parameter.lower()

    for book in books:
        title_lower = book.title.lower()
        author_lower = book.author.lower()
        genre_lower = book.genre.lower()

        if type_parameter == 1:
            if param_lower in title_lower:
                result.append(book)

        elif type_parameter == 2:
            if param_lower in author_lower:
                result.append(book)

        elif type_parameter == 3:
            if param_lower in genre_lower:
                result.append(book)

    if result == []:
        return None

    return result

def load_loans_from_list_bk(books: list[Book]) -> list:

    loans = []

    try:
        for book in books:
            if book.available == False:
                loans.append(book)
            else:
                pass
    except:
        print("saslo")

    

    return loans

def delete_loan_book_by_id_st(search_id: int, loan_books: list[Book], now_acc: str):
    book_to_delete = get_book_by_id(loan_books, search_id)

    if book_to_delete.stud_name != None:
        if book_to_delete.stud_name == now_acc:
            loan_books.remove(book_to_delete)
        elif book_to_delete.stud_name != now_acc:
            print("Запись оформлена не на вас.")
        else:
            print("Такой записи нет.")

def delete_loan_book_by_id(search_id: int, loan_books: list[Book]):
    book_to_delete = get_book_by_id(loan_books, search_id)
    if book_to_delete in loan_books:
        loan_books.remove(book_to_delete)
    else:
        print("Такой записи нет.")

def print_loan_books_st(loan_books: list, now_acc):
    if len(loan_books) > 0:
        print_book_header()
        for book in loan_books:
            if book.stud_name == now_acc:
                print_single_book(book)
                print(f"{'-'*140}")
            else:
                pass
    else:
        print("Книг нет в ассортименте")

def print_loan_books(loan_books: list):
    if len(loan_books) > 0:
        print_book_header()
    for book in loan_books:
        print_single_book(book)
        print(f"{'-'*140}")
    else:
        print("Книг нет в ассортименте")

def load_books_from_txt_file(filename: str) -> list[Book]:
    try:
        with open(filename, "r", encoding="utf-8") as file_in:

            books = []
            count_books = int(file_in.readline())
            update_get_next_book_id(int(file_in.readline()))

            for _ in range(count_books):

                books.append(
                    Book(
                        id=int(file_in.readline()),
                        title=file_in.readline().strip(),
                        author=file_in.readline().strip(),
                        genre=file_in.readline().strip(),
                        stud_name=file_in.readline().strip(),
                        available=bool(file_in.readline()),
                        rating=float(file_in.readline()),
                    )
                )

            return books
    except:
        return []

def save_books_to_txt_file(books: list[Book], filename: str) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as file_out:
            file_out.write(f"{len(books)}\n")
            file_out.write(f"{global_book_id}\n")

            for book in books:
                file_out.write(
                    f"{book.id}\n"
                    f"{book.title}\n"
                    f"{book.author}\n"
                    f"{book.genre}\n"
                    f"{book.stud_name}\n"
                    f"{book.available}\n"
                    f"{book.rating}\n"
                )

        return True
    except:
        return False