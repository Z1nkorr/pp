from library import *
from lib_console_helper import *
from lib_functions_Acc import *
from lib_functions_Book import *
from datetime import datetime, timedelta, date
import pickle



def input_LoanRec_data(loanid: int, now_acc: Account) -> LoanRecord:

    book_id = loanid
    student_name = now_acc.username
    issue_date = date.today()
    due_date = issue_date + timedelta(days=14)
    record_id = get_next_loan_id()

    return LoanRecord(
        book_id = book_id,
        student_name = student_name,
        issue_date = issue_date,
        due_date = due_date,
        record_id = record_id
    )


LOANS_FILE = "loans.pkl"

global_loan_id = 0

def update_get_next_loan_id(loans:list[LoanRecord]) -> int:

    global global_loan_id

    for loan in loans:

        if loan.record_id > global_loan_id:

            global_loan_id = loan.record_id
            return(global_loan_id)
        
    return None

def save_loans_to_pkl_file(loans: list[LoanRecord], filename: str = LOANS_FILE) -> bool:
    try:
        with open(filename, "wb") as f:
            pickle.dump(loans, f)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении записей: {e}")
        return False


def load_loans_from_pkl_file(filename: str = LOANS_FILE) -> list[LoanRecord]:
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
        if isinstance(data, list):
            return data
        else:
            print("Файл с записями повреждён: ожидался список.")
            return []
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Ошибка при загрузке записей: {e}")
        return []

def get_next_loan_id() -> int:

    global global_loan_id
    global_loan_id += 1
    return(global_loan_id)

def get_loan_by_id(loans: list[LoanRecord], search_id: int) -> LoanRecord | None:
    for loan in loans:
        if loan.record_id == search_id:
            return loan
    return None

def add_loan_to_list(loans: list[LoanRecord], new_loan: LoanRecord):

    loans.append(new_loan)

def delete_loan_by_id(loans: list[LoanRecord]) -> bool:
    find_loan = get_loan_by_id(loans, "Введите id библиотечного абонемента по которому хотите вернуть книгу: ")
    if find_loan.record_id != None:
        loans.remove(find_loan)
        return True
    return False

def delete_loan_by_id_stud(now_acc: Account, search_id: int, books: list[Book]) -> bool:
    recs = now_acc.loan_records
    find_loan = get_loan_by_id(recs, search_id)
    if find_loan != None:
        return_book = get_book_by_id(books, find_loan.book_id)
        return_book.available_copies += 1
        now_acc.loan_records.remove(find_loan)
        return True
    return False

def print_all_loans_stud(now_acc: Account):
    if len(now_acc.loan_records) > 0:
        print_loan_header()
        for loan in now_acc.loan_records:
            print_single_loan(loan)
            print(f"{'-'*140}")
    else:
        print("Активных записей у вас нет.")

def print_single_loan(loan: LoanRecord):
    print(
        f"{loan.book_id:<5}"
        f"{loan.student_name:<40}"
        f"{loan.issue_date.strftime('%d.%m.%Y'):<25}"
        f"{loan.due_date.strftime('%d.%m.%Y'):<20}"
        f"{loan.record_id:<20}"
    )

def print_loan_header():
    print("\n"
        f"{'ИД':<5}"
        f"{'Имя студента':<40}"
        f"{'Дата оформления':<25}"
        f"{'Дата возврата':<20}"
        f"{'ИД выданной книги':<20}"
    )

def print_all_loans(loans: list[LoanRecord]):
    if len(loans) > 0:
        print_loan_header()
        for loan in loans:
            print_single_loan(loan)
            print(f"{'-'*140}")
    else:
        print("Активных записей сейчас нет.")