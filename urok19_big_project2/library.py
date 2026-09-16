from dataclasses import dataclass
from datetime import datetime

@dataclass(slots=True)
class Book:
    title: str
    author: str
    genre: str
    rating: float
    stud_name: str | None = "Нет"
    available: bool = True
    id: int | None = None