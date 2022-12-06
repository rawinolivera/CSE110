
loan = float(input("How large is the loan? "))
credit_hist = float(input("How good is your credit history? "))
income = float(input("How high is your income? "))
down_payment = float(input("How large is your down payment? "))

if loan >= 5:
    if credit_hist >= 7 and income >= 7:
            desition = True
    elif (credit_hist >= 7 or income >= 7) and down_payment >= 5:
            desition = True
    else:
        desition = False

elif credit_hist >= 4:
    if  ( income >= 7 or down_payment >= 7) or (income >= 4 and down_payment >= 4):
        desition = True
    else:
        desition = False
else:
    desition = False


if desition:
    print("The loan has been approved")
else:
    print("Loan desition denied")