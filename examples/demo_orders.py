from src.shop.orders import Order

for items in ([(10, 2)], [(5, 4), (20, 1)]):
    print(Order(items).total())
