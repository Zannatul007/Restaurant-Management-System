from user_management import *

restaurant_name = input("Please enter a restaurant name:")
restaurant = Restaurant(restaurant_name)
print("Welcome to the {} restaurant".format(restaurant.name))

choices = ["Login", "Register", "Exit"]

for index, choice in enumerate(choices):
    print(f"{index+1}:{choice}")

while True:

    choice = input("Enter your choice :")
    if choice == "1":
        u_id = input("Enter user id: ")
        u_name = input("Enter your name: ")
        u_pass = input("Enter your password: ")
        user = restaurant.members[u_id]
        if restaurant.verify_member(user, u_name, u_pass):
            print("Login successful")
            if user.role == "Customer":
                print("CHOOSE YOUR CHOICE\n")
                print("1: Add reservation")
                print("2: Update reservation")
                print("3: Delete reservation")
                print("4: Place order")
                print("5: Show orders and reservations")

                while True:
                    c_customer = input(">")
                    if(c_customer == '1'):
                        user.

    elif choice == "2":
        u_id = input("Enter user id: ")
        u_email = input("Enter your email: ")
        u_name = input("Enter your name: ")
        u_pass = input("Enter your password: ")
        u_role = input("Enter the role `Customer/Chef/Admin/Staff` ?")
        user = User(u_id, u_name, u_email, u_pass, u_role)
        restaurant.register_member(user)

    else:
        break
