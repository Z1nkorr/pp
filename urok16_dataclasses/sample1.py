#photo = ""
#title = ""
#description = ""
#rating = ""
#price = ""
#comments = ["","",""]

# photo = []
# title = []
# description = []
# rating = []
# price = []
# comments = []

# -------------

from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Product:
    photo: str
    title: str
    description: str
    rating: Decimal
    price: int
    comments: list[str]

products: list[Product] = []

products.append(
    Product(
        "(Кросовка)",
        "Nike hueta",
        "Кроссовки из-за которых вас обоссут и обхаркают, а вы ещё не успели выйти из дома.",
        Decimal("4.8"),
        6767,
        [   
            "рил, hueta",
            "67676767676767676767676767676767676767",
            "нахуя я их купил..."
        ]
    )
)
print(products[0].photo)
print(products[0].title)
print(products[0].description)
print(products[0].comments[0])