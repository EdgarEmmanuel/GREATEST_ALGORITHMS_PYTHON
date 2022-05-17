from collections import namedtuple
# price = "pomme", 5 , 10
#
# def formatTuple(tuple):
#     name, low_price, max_price = tuple
#     print(f"for the product {name} the max price during the year was : {max_price} $")
#
# formatTuple(price)

Product = namedtuple("Product", "name low_price max_price")
pomme = Product("pomme", 5, 10)
orange = Product("orange", 4, 8)

print(orange.low_price)