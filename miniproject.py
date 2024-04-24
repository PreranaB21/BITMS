email=["peru@gmail.com","varshini@gmail.com","rishika@gmail.com"]
password=[12345678,12345,98765]
otp=52467
uemail=str(input("Enter email"))
upaw=int(input("Enter password"))
uopt=int(input("Enter otp"))
for i in range(0,len(email)):
    if email[i]==uemail:
        if password[i]==upaw:
            if otp==uopt:
                print("Already registered")
                break
else:
    print("Register first")
def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']

# Create an account dictionary
account = {
    'balance': 1000,
    'transactions': []
}

# Dictionary to map user choices to functions
choices = {
    '1': deposit,
    '2': withdraw,
    '3': get_balance,
    '4': get_transaction_history
}

while  email[i]==uemail and password[i]==upaw:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting program.")
        break

    if choice in choices:
        if choice == '1' or choice == '2':
            amount = float(input("Enter amount: "))
            choices[choice](account, amount)
        else:
            print(choices[choice](account))
        '''if choice == '2':
             amount = float(input("Enter amount: "))
             choices[choice](account, amount)
             withdraw()>5
             print("Limit reached")'''
       
    else:
        print("Invalid choice. Please try again.")