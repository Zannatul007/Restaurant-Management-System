from restaurant_management import *

dish1 = Dish("1", "Curry", 2, 1000)
dish2 = Dish("2", "Beef Curry", 2, 2000)

order = Order()
order.add_dishes(dish1)
order.add_dishes(dish2)
order.details_order()
