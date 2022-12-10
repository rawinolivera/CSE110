cart = []
print("Welcome to the Shopping Cart Program!")
print()
option = 0

while option != 5:
    if option == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}'  has been added to the cart.")
        option = 0
        print()

    elif option == 2:
        print("The contents of the shopping cart are:")
        for item in cart:
            print(item)
        option = 0
        print()

    elif option == 3:
        print("This option will be available soon")
        print()

    elif option == 4:
        print("This option will be available soon")
        print()

    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    option = int(input("Please enter an action: "))

print("Thank you. Goodbye.")