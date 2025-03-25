from user_management import *


dish1 = Dish("1", "Curry", 2, 1000)
dish2 = Dish("2", "Beef Curry", 2, 2000)
dish3 = Dish("3", "Beef Rejala", 3, 1000)

order = Order(123)
order.add_dishes(dish1)
order.add_dishes(dish2)
order.add_dishes(dish3)


# order.details_order()

user1 = User(1, "Zannatul", "Zannatul.fardaush.03@gmail.com", "@123", "Customer")
user2 = User(2, "Zannatul Fardaush", "Zannatul03@gmail.com", "@123", "Customer")
reservation1 = Reservation("1", 20, "20 march", "8-9pm")
reservation2 = Reservation("2", 25, "25 march", "8-9.30pm")
restaurant1 = Restaurant()
restaurant1.register_member(user1)
restaurant1.register_member(user2)
restaurant1.verify_member(user1, "Zannatul", "@123")
restaurant1.add_reservations(user1, reservation1)
restaurant1.add_reservations(user2, reservation1)
restaurant1.add_reservations(user2, reservation2)
restaurant1.view_reservations()
user1.place_order(order)

print("**---**")
# user1.view_order(restaurant1)

# restaurant1.add_orders(user1, order)
# restaurant1.
# user1.add_reservations(reservation1)
# user1.add_reservations(reservation2)
# user1.view_reservations()


chef1 = Chef("12", "Sabbir", "Sabbir@gmail.com", "@123")
chef1.view_status(user1, order)
chef1.update_status(user1, order, "Ready")
