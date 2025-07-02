def deposit(balance,amount):
    return balance+(amount//2)

def withdraw(balance,amount):
    return balance-10000

def check_balance(balance):
    return balance-10000

balance=100000

balance=deposit(balance,50000)
print('yangi balans:',check_balance(balance))