import requests
from dataclasses import dataclass
from datetime import datetime

@dataclass
class RateData:
    date: str
    rate: float

def get_valute_rub(valute: str):
    url = f"https://api.frankfurter.dev/v2/rate/eur/rub"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    return RateData(
        date = datetime.strptime(data["date"], "%Y-%m-%d").strftime("%d-%m-%Y"),
        rate = data.response
    )

valute = "eur"

get_valute_rub(valute)