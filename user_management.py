from restaurant import *


class Dish:
    def __init__(self, d_id, name, quantity: int, price: float):
        self.id = d_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return "Dish name : {}, Quantity : {}, Price : {} ".format(
            self.name, self.quantity, self.price
        )


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.dishes = []
        self.status = "In Progress"

    def add_dishes(self, dish: Dish):
        self.dishes.append(dish)

    def details_order(self):
        price = 0
        for index, dish in enumerate(self.dishes):
            print(
                "{:5} {:20} {:10} {:10} {:10}".format(
                    index + 1,
                    dish.name,
                    dish.quantity,
                    dish.price,
                    dish.price * dish.quantity,
                )
            )
            price += dish.price * dish.quantity
        print("Total Price {}".format(price))

    def __str__(self):
        return "{}'s status is {}".format(self.order_id, self.status)


class Reservation:
    def __init__(self, reservation_id, seats, date, time_slot):
        self.reservation_id = reservation_id
        self.seats = seats
        self.date = date
        self.time_slot = time_slot

    def __str__(self):
        return "Reservation for {} seats on {} at {}".format(
            self.seats, self.date, self.time_slot
        )


class User:
    def __init__(self, u_id, name, email, password, role="Customer"):
        self.id = u_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

        self.orders = []
        self.reservations = []

    def book_reservation(self, restaurant, reservation):
        self.reservations.append(reservation)
        restaurant.add_reservations(self, reservation)

    def update_reservation(self, restaurant, reservation, seat, time_slot, date):
        restaurant.update_reservation(
            self, restaurant, reservation, seat, time_slot, date
        )

    def delete_reservation(self, restaurant):
        restaurant.delete_reservation(self)

    def show_reservation(self):
        for reservation in self.reservations:
            print(reservation)

    def place_order(self, order):
        self.orders.append(order)

    def show_orders(self):
        print("Details of order")

        for order in self.orders:
            print(order.details_order())

    def __str__(self):
        return "{} has a reservation of {} and the orders {}".format(
            self.name, len(self.reservations), len(self.orders)
        )

    # def view_order(self, restaurant):
    #     for i, order in enumerate(restaurant.orders):
    #         print("{} \t {}".format(i, order.details_order()))


class Chef(User):
    def __init__(self, uid, name, email, password):
        super().__init__(uid, name, email, password, role="Chef")

    def view_status(self, customer, order):
        for order in customer.orders:
            print("The status of order is {}".format(order.status))

    def update_status(self, customer, order, status):
        for order in customer.orders:
            order.status = status
            print("Updated order of {} list is {}".format(customer.name, order))


# class Waiter(User):
#     def __init__(self, uid, name, email, password):
#         super().__init__(uid, name, email, password, role="Waiter")

#         def take_order(self, customer, order):


#         def update_order(self, customer_id, order):
#             pass


class Admin(User):
    def __init__(
        self,
        uid,
        name,
        email,
        password,
    ):
        staffs = []
        super().__init__(uid, name, email, password, role="Admin")

    def add_staffs(self, restaurant, user):
        restaurant.register_member(user)

    def update_staff(self, restaurant, user):
        restaurant.update_user(user, user.role, user.email)

    def remove_staff(self, restaurant, user):
        restaurant.delete_user(user)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.members = {}
        self.orders = {}
        self.reservations = {}

    # User management
    def register_member(self, user):
        if user.id in self.members:
            print("User is already exist as a {}".format(user.role))
        else:
            self.members[user.id] = user
            print("{} is successfully registered as {}".format(user.name, user.role))

    def verify_member(self, user, name, password):
        if user.id in self.members:
            if (user.name == name) and (user.password == password):
                # print("good to go")
                return True
            else:
                print("Invalid password or username")
        else:
            print("User doesn't exist")

    def update_user(self, user, role=None, contact_info=None):
        if user.id not in self.members:
            print("User does not exist")
            return
        if role:
            self.members[user.id].role = role
        if contact_info:
            self.members[user.id].email = contact_info

    def delete_user(self, user):
        if user.id not in self.members:
            print("User doesn't exist")
        else:
            print(
                "{} is removed of customer {}".format(self.members[user.id], user.name)
            )
            del self.members[user.id]

    def add_reservations(self, customer, reservation):
        if customer.id in self.members:
            if reservation.reservation_id not in self.reservations:
                self.reservations[customer.id] = reservation
                print(
                    "{} is successfully reserved for {} ".format(
                        reservation, customer.name
                    )
                )
            else:
                print("{} is already reserved".format(reservation))
        else:
            print("User doesn't exist")

    ##Reservation Management
    def update_reservation(
        self,
        customer,
        reservation,
        seat=None,
        time_slot=None,
        date=None,
    ):
        if customer.id not in self.reservations:
            print("Reservation doesn't exist")
            return
        if seat:
            self.reservations[customer.id].seat = seat
        if time_slot:
            self.reservations[customer.id].time_slot = time_slot
        if date:
            self.reservations[customer.id].date = date
        print("Updated reservation is {}".format(reservation))

    def delete_reservation(self, customer):
        if customer.id in self.reservations:
            print(
                "{} is removed of customer {}".format(
                    self.reservations[customer.id], customer.name
                )
            )
            del self.reservations[customer.id]
        else:
            print("Reservation doesn't exist")

    def view_reservations(self):
        print("***All reservations details***")
        for key, reservation in self.reservations.items():
            print("{} is booked for {}".format(reservation, self.members[key].name))

    def add_orders(self, customer, order):
        if customer.id in self.members:
            self.orders[customer.id] = order

    # Order Management
    def add_orders(self, customer, order):
        if customer.id in self.members:
            self.orders[customer.id] = order
        else:
            print("User doesn't exist")

    def show_orders(self):
        for key, order in self.orders():
            print("{} {}".format(self.members[key].name, order))
