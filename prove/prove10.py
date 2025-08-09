cart = []
prices = []
print("Welcome to the Shopping Cart Program!")
print()
option = 0
total_price = 0.00
bound_item = 0

while option != 5:
    if option == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        price = float(input(f"What is the price of {item}? "))
        prices.append(price)
        print(f"'{item}'  has been added to the cart.")
        print()

    elif option == 2:
        bound_item = len(cart)
        if bound_item == 0:
            print("There are not items in the car!")
        else:
            print("The contents of the shopping cart are:")
            for i in range(len(cart)):
                item = cart[i]
                price = prices[i]
                index = i + 1
                print(f"{index}. {item} - ${price:.2f}")
        print()

    elif option == 3:
        if bound_item == 0:
            print("There are not items in the car!")
        else:
            item_i = int(input("Which item would you like to remove? "))
            bound_item = len(cart)
            if item_i > bound_item:
                print("The item is not in the list, try again!")
            elif item_i < 1:
                print("The item is not in the list, try again!")
            else:
                index = item_i - 1
                cart.pop(index)
                prices.pop(index)
                print("Item removed.")
        print()

    elif option == 4:
        for price in prices:
            total_price = total_price + price
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")
        print()

    print("Please select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    option = int(input("Please enter an action: "))

print("Thank you. Goodbye.")