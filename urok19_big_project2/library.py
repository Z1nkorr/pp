from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class Book:
    title: str
    author: str
    genre: str
    total_copies: int
    available_copies: int
    rating: float
    id: int | None = None

@dataclass(slots=True)
class LoanRecord:
    book_id: int
    student_name: str
    issue_date: datetime
    due_date: datetime
    record_id: int | None = None

@dataclass(slots=True)
class Account:
    username: str
    password: str
    loan_records: list 
    count_records: int
    acc_id: int | None = None