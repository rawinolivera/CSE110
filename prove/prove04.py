print("* * * * * * * * * * * * * * * * * * * * ")
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
drink_price = float(input("What is the price of the drink? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
num_drinks = float(input("How much of drink are there? (liters): "))
tax_rate = float(input("What is the sales tax rate? "))
subtotal = child_price * num_children + adult_price * num_adults + drink_price * num_drinks
tax = subtotal * (tax_rate / 100)
total = subtotal + tax
print()
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print()
payment = float(input("What is the payment amount? "))
while total > payment:
    print("The payment amount is not enough")
    payment = float(input("Please provide a payment amount greater or equal to the total? "))
change = payment - total
print(f"Change: ${round(change, 2)}")
print("* * * * * * * * * * * * * * * * * * * * ")