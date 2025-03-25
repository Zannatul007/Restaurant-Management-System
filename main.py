from restaurant_management import *

dish1 = Dish("1", "Curry", 2, 1000)
dish2 = Dish("2", "Beef Curry", 2, 2000)

# order = Order()
# order.add_dishes(dish1)
# order.add_dishes(dish2)
# order.details_order()

user1 = User("1", "Zannatul", "Zannatul.fardaush.03@gmail.com", "@123", "Customer")
user2 = User("2", "Zannatul Fardaush", "Zannatul03@gmail.com", "@123", "Customer")
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

user1.book_reservation(restaurant1, reservation1)
