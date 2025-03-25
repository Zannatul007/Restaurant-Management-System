class Dish:
    def __init__(self, d_id, name, quantity: int, price: float):
        self.id = d_id
        self.name = name
        self.quantity = quantity
        self.price = price


class Order:
    def __init__(self):
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


class User:
    def __init__(self, uid, name, email, password, role="Customer"):
        self.id = uid
        self.name = name
        self.email = email
        self.password = password
        self.role = role


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
