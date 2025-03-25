class Dish:
    def __init__(self, d_id, name, quantity: int, price: float):
        self.id = d_id
        self.name = name
        self.quantity = quantity
        self.price = price


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
                "{:<5} {:<20} {:<10} {:<10} {:<10}".format(
                    index + 1,
                    dish.name,
                    dish.quantity,
                    dish.price,
                    dish.price * dish.quantity,
                )
            )
            price += dish.price * dish.quantity
        print("Total Price {}".format(price))


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
    def __init__(self, uid, name, email, password, role="Customer"):
        self.id = uid
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.orders = []
        self.reservations = []

    def book_reservation(self, restaurant, reservation: Reservation):
        restaurant.add_reservations(reservation)

    def update_reservation(self, restaurant, reservation: Reservation):
        pass

    def place_order(self, order):
        # self.orders[customer_id].append(order)
        pass


class Chef(User):
    def __init__(self, uid, name, email, password):
        super().__init__(uid, name, email, password, role="Chef")

        def view_status(self, customer_id, order):
            pass

        def update_status(self, customer_id, order):
            pass


class Waiter(User):
    def __init__(self, uid, name, email, password):
        super().__init__(uid, name, email, password, role="Waiter")

        def take_order(self, customer_id, order):
            pass

        def update_order(self, customer_id, order):
            pass


class Admin(User):
    pass


class Restaurant:
    def __init__(self):
        self.members = {}
        self.orders = {}
        self.reservations = {}

    def register_member(self, user: User):
        if user.id in self.members:
            print("User is already exist as a {}".format(user.role))
        else:
            self.members[user.id] = user
            print("{} is successfully registered".format(user.name))

    def verify_member(self, user: User, name, password):
        if user.id in self.members:
            if (user.name == name) and (user.password == password):
                # print("good to go")
                return True
            else:
                print("Invalid password or username")
        else:
            print("User doesn't exist")

    def add_reservations(self, customer: User, reservation: Reservation):
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

    def update_reservation(
        self,
        customer: User,
        reservation: Reservation,
        seat=None,
        time_slot=None,
        date=None,
    ):
        if customer.id not in self.reservations:
            print("Reservation doesn't exist")
            return
        if seat:
            self.reservations[customer.id].seats = seat
        if time_slot:
            self.reservations[customer.id].time_slot = time_slot
        if date:
            self.reservations[customer.id].date = date
        print("Updated reservation is {}".format(reservation))

    def delete_reservation(self, customer: User):
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
