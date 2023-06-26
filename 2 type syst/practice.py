

customer: str = "kev"
cake_base: str = "tin"
size: int = 15
topping: str = "live"
butter: bool = True
price: float = 25.00

print(f"order from {customer}")
print(f"cake base {cake_base}, size {size}cm, topping {topping}")
print(f"add butter: {butter}")
print(f"price {price}")


# Using another string fofrmating
order: str = f""""
  order from {customer}
  cake base {cake_base}, size {size}cm, topping {topping}
  add butter: {butter}
  price {price}
"""
print(order)


# String formating in print
print(f""""
  order from {customer}
  cake base {cake_base}, size {size}cm, topping {topping}
  add butter: {butter}
  price {price}
""")