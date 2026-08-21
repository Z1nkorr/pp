from library import *
from lib_console_helper import *
from datetime import datetime, time
import pickle

ACCOUNTS_FILE = "accounts.pkl"

global_acc_id = 0

def update_get_next_acc_id(accs:list[Account]) -> int:

    global global_acc_id

    for acc in accs:

        if acc.acc_id > global_acc_id:

            global_acc_id = acc.acc_id
            return(global_acc_id)
        
    return None

def save_accounts_to_pkl_file(accounts: list[Account], filename: str = ACCOUNTS_FILE) -> bool:
    try:
        with open(filename, "wb") as f:
            pickle.dump(accounts, f)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении аккаунтов: {e}")
        return False


def load_accounts_from_pkl_file(filename: str = ACCOUNTS_FILE) -> list[Account]:
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
        if isinstance(data, list):
            return data
        else:
            print("Файл аккаунтов повреждён: ожидался список.")
            return []
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Ошибка при загрузке аккаунтов: {e}")
        return []

def get_next_acc_id() -> int:
    global global_acc_id

    global_acc_id += 1

    return(global_acc_id)

def get_acc_by_id(accounts: list[Account],search_id: int) -> Account | None:
    for acc in accounts:
        if acc.acc_id == search_id:
            return acc
    return None

def delete_acc_by_id(accounts: list[Account], mes:str) -> bool:
    find_acc = get_acc_by_id(accounts,mes)
    if find_acc != None:
        if find_acc.username == "admin":
            print("\nВы не можете удалить аккаунт администратора.")
            return False
        accounts.remove(find_acc)
        print("\nАккаунт успешно удален!")
        return True
    print("\nАккаунт не найден")
    return False

def print_single_account(acc: Account):
    print(
        f"{acc.acc_id:<5}"
        f"{acc.username:<25}"
        f"{acc.password:<20}"
        f"{acc.count_records:<20}"
    )

def print_account_header():
    print(
        f"{'ИД':<5}"
        f"{'Никнейм':<25}"
        f"{'Пароль':<20}"
        f"{'Кол-во выданных книг':20}"
    )

def print_all_accounts(accs: list[Account]):
    if len(accs) > 0:
        print_account_header()
        for acc in accs:
            
                print_single_account(acc)
                print("-"*140)
    else:
        print("Аккаунтов нет")

def sign_in(accounts: list[Account]) -> Account:
        
    username_correct = False
    existing_usernames = {acc.username for acc in accounts}

    while username_correct == False:
        inp_username = input_str("Введите никнейм: ", 1, 20)
        if inp_username in existing_usernames:
            print("Аккаунт с таким именен уже существует")
        else:
            username_correct = True


    is_cor_pass = False
    while not is_cor_pass:
        password = input_str("Введите пароль: ", 1, 100)
        password_confirm = input_str("Подтвердите пароль: ", 1, 100)
        if password == password_confirm:
            is_cor_pass = True
        else:
            print("Пароли не совпадают.")

    acc_id = get_next_acc_id()
    return Account(
        username=inp_username,
        password=password,
        acc_id=get_next_acc_id(),
        loan_records=[],
        count_records=0
    )

def log_in(accounts: list[Account]) -> Account | None:
    username = input_str("Введите никнейм: ", 1, 20)

    account = None
    for acc in accounts:
        if acc.username == username:
            account = acc
            break

    if account is None:
        print("Аккаунт не найден.")
        return None

    is_cor_pass = False
    while not is_cor_pass:
        password = input_str("Введите пароль: ", 1, 100)
        if password == account.password:
            is_cor_pass = True
        else:
            print("Неверный пароль.")

    return account

def add_acc_to_list(accounts:list[Account], new_account:Account):
    accounts.append(new_account)