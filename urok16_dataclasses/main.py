from product import Product
from func import add_to_end, print_all

products: list[Product] = []

add_to_end(
    products,
    Product(
        photo="(Кросовка)",
        title="Nike hueta",
        description="Кроссовки из-за которых вас обоссут и обхаркают, а вы ещё не успели выйти из дома.",
        rating="4.8",
        price=6767,
        comments=[   
            "рил, hueta",
            "67676767676767676767676767676767676767",
            "нахуя я их купил...",
        ],
    ),
)

add_to_end(
    products,
    Product(
        photo="(Телефон)",
        title="Lohphone",
        description="Хуетень ебанная для бомжей.",
        rating="-2.3",
        price=4242,
        comments=[   
            "рил, Lohphone",
            "424242424242424242424242424242424242",
            "зач я это купил...?",
        ],
    ),
)

print_all(products)