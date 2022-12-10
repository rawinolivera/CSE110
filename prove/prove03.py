print("* * * * * * * * * * * * * * * * * * * * ")
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))
subtotal = child_price * num_children + adult_price * num_adults
tax = subtotal * (tax_rate / 100)
total = subtotal + tax
print()
print(f"Subtotal: ${subtotal}")
print(f"Sales Tax: ${tax}")
print(f"Total: ${total}")
print()
payment = float(input("What is the payment amount? "))
while total > payment:
    print("The payment amount is not enough")
    payment = float(input("Please provide a payment amount greater or equal to the total? "))
change = payment - total
print(f"Change: ${round(change, 2)}")
print("* * * * * * * * * * * * * * * * * * * * ")