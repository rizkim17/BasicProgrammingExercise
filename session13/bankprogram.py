class Account:
    def __init__(self, account_name, balance):
        self.account_number = len(accounts) + 1
        self.account_name = account_name
        self.balance = balance

accounts = []

def print_account():
    print("\nNum\tAccount Name\n--------------------------")
    for acc in accounts:
        print(f"{acc.account_number}\t{acc.account_name}")

def create_account():
    try:
        account_name = str(input('\nEnter account name\t : '))
        balance = float(input('Enter initial bal1ance\t : '))
        account = Account(account_name, balance)
        accounts.append(account)
        print_account()
        print('\nAccount created successfully.')
    except ValueError:
        print('\nInvalid input.')

def deposit_money():
    try:
        if len(accounts) == 0:
            print_account()
            print('No account found.')
        else:
            print_account()
            account_number = int(input('\nEnter account number\t : '))
            for acc in accounts:
                if acc.account_number == account_number:
                    amount = float(input('Enter amount to deposit\t : '))
                    acc.balance += amount
                    print(f'\nDeposit Rp.{amount:,} to {acc.account_name} successful.')
                    return
            print(f'Account num {account_number} not found.')
    except ValueError:
        print('Invalid input.')

def withdraw_money():
    try:
        if len(accounts) == 0:
            print_account()
            print('No account found.')
        else:
            print_account()
            account_number = int(input('\nEnter account number\t : '))
            for acc in accounts:
                if acc.account_number == account_number:
                    print(f'\n{acc.account_name} balance: Rp. {acc.balance:,}')
                    amount = float(input('\nEnter amount to withdraw\t : '))
                    if acc.balance >= amount:
                        acc.balance -= amount
                        print(f'\nWithdrawal Rp.{amount:,} in account {acc.account_name} successful.')
                    else:
                        print('\nInsufficient balance. Process canceled.')
                    return
            print(f'Account num {account_number} not found.')
    except ValueError:
        print('Invalid input.')

def check_balance():
    try:
        if len(accounts) == 0:
            print_account()
            print('No account found.')
        else:
            print_account()
            account_number = int(input('\nEnter account number\t : '))
            for acc in accounts:
                if acc.account_number == account_number:
                    print(f'\n{acc.account_name} balance: Rp. {acc.balance:,}')
                    return
            print(f'Account num {account_number} not found.')
    except ValueError:
        print('Invalid input.')

def exit():
    print('Exiting banking system.')
    return