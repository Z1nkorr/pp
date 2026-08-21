from decimal import Decimal
from product import Product

def add_to_end(products:list[Product], product:Product):
    products.append(product)

def print_all(products:list[Product]):
    for product in products:
        print(product)