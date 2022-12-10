bank_accounts = []
balances = []
bank_account = ''
balance = 0.00
total_balance = 0.00
average = 0.00
high_balance = 0.00
high_account = ''

while bank_account != 'quit':
    bank_account = input("What is the name of this account? ")
    if bank_account != 'quit':
        balance = float(input("What is the balance: "))
        bank_accounts.append(bank_account)
        balances.append(balance)
        #calculate Total
        total_balance += balance

num_account = len(bank_accounts)
if num_account > 0:
    average = total_balance / num_account

print()
print("Accounts Information:")
for i in range(len(bank_accounts)):
    balance = balances[i]
    bank_account = bank_accounts[i]
    #Determine highest balance
    if balance > high_balance:
        high_balance = balance
        mark = i
        high_account = bank_accounts[mark]
    print(f"{i}. {bank_account} - ${balance:.2f}")

print()
print(f"Total: ${total_balance:.2f}")
print(f"Average: ${average:.2f}")
print(f"Highest balance: {high_account} - ${high_balance:.2f}")

opt = ''
while opt != 'no':
    print()
    opt = input("Do you want to update an account? ")
    opt = opt.lower()
    if opt == 'yes':
        upd_account = int(input("What account index do you want to update? "))
        upd_balance = float(input("What is the new amount? "))
        balances[upd_account] = upd_balance
    print()
    print("Accounts Information:")
    for i in range(len(bank_accounts)):
        balance = balances[i]
        bank_account = bank_accounts[i]
        print(f"{i}. {bank_account} - ${balance:.2f}")




