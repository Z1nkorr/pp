from library import *
from lib_console_helper import *
from datetime import datetime, time
import pickle

BOOKS_FILE = "books.pkl"

global_book_id = 0

def update_get_next_book_id(books:list[Book]) -> int:

    global global_book_id

    for book in books:

        if book.id > global_book_id:

            global_book_id = book.id
            return(global_book_id)
        
    return None

def save_books_to_pkl_file(books: list[Book], filename: str = BOOKS_FILE) -> bool:
    try:
        with open(filename, "wb") as f:
            pickle.dump(books, f)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении книг: {e}")
        return False


def load_books_from_pkl_file(filename: str = BOOKS_FILE) -> list[Book]:
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
        if isinstance(data, list):
            return data
        else:
            print("Файл книг повреждён: ожидался список.")
            return []
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Ошибка при загрузке книг: {e}")
        return []

def inp_book_data() -> Book:

    title = input_str("Введите название книги: ",1,40)
    author = input_str("Введите автора книги: ",1,25)
    genre = input_str("Введите жанр: ", 1, 20)
    total_copies = input_int("Введите кол-во экземпляров(от 1 до 100): ",1,100)
    available_copies = total_copies
    rating = input_int("Введите рейтинг книги: ",1,5)

    return Book(
        id = 0,
        title = title,
        author = author,
        genre = genre,
        total_copies = total_copies,
        available_copies = available_copies,
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
    find_book.available_copies = book.available_copies
    find_book.total_copies = book.total_copies
    find_book.rating = book.rating
    return True

def delete_book_by_id(books: list[Book], search_id: int) -> bool:
    find_book = get_book_by_id(books, search_id)
    if find_book.id != None:
        books.remove(find_book)
        return True
    return False

def print_single_book(book: Book):
    print(
        f"{(book.id):<5}"
        f"{book.title:<40}"
        f"{book.author:<25}"
        f"{book.genre:<20}"
        f"{book.total_copies:<15}"
        f"{book.available_copies:<20}"
        f"{book.rating:<10}"
    )

def print_book_header():
    print("\n"
        f"{'ИД':<5}"
        f"{'Название':<40}"
        f"{'Автор':<25}"
        f"{'Жанр':<20}"
        f"{'Всего копий':<15}"
        f"{'Осталось копий':<20}"
        f"{'Рейтинг':<10}"
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

    result: list[Book] = []
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


def buy_book(books: list[Book], search_id: int, request_amount: int) -> bool:
    pass