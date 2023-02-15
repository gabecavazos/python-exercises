import os
import csv

# Constants
FILE_NAME = 'transactions.csv'
FIELD_NAMES = ['id', 'amount', 'type']
MENU_OPTIONS = ['1', '2', '3', '4']
BALANCE = 0
#function to view balance
def view_balance():
    balance = get_balance()
    print(f'Current balance: {balance}\n')
#function to add debit
def add_debit():
    amount = get_amount()
    write_transaction(amount, 'debit')
    update_balance(amount)
    print(f'{amount} has been withdrawn from your account.\n')
#function to add credit
def add_credit():
    amount = get_amount()
    write_transaction(amount, 'credit')
    update_balance(amount)
    print(f'{amount} has been added to your account.\n')
#exit function
def exit_program():
    print('Exiting program...')
#update balance function
def get_balance():
    balance = BALANCE
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=FIELD_NAMES)
            for row in reader:
                amount = float(row['amount'])
                if row['type'] == 'credit':
                    balance += amount
                else:
                    balance -= amount
    return balance
#function to accept amount
def get_amount():
    while True:
        amount = input('Enter an amount: ')
        if not is_decimal(amount):
            print('Invalid input. Please enter a valid amount.\n')
            continue
        return float(amount)
#function to check for flotable values
def is_decimal(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
#function to log transactions
def write_transaction(amount, transaction_type):
    transaction_id = get_transaction_id()
    with open(FILE_NAME, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([transaction_id, amount, transaction_type])
#function to get transaction id
def get_transaction_id():
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return str(len(list(reader)) + 1)
    return '1'
#function to update global balance
def update_balance(amount):
    global BALANCE
    if amount is not None:
        BALANCE += amount
#function to intiate menu checkbook
def main():
    print('Welcome to the checkbook\n')
    while True:
        print('Please choose an option:')
        print('1 - View current balance')
        print('2 - Add a debit')
        print('3 - Add a credit')
        print('4 - Exit\n')

        option = input('> ')
        if option not in MENU_OPTIONS:
            print('Invalid input. Please enter a valid option.\n')
            continue

        if option == '1':
            view_balance()
        elif option == '2':
            add_debit()
        elif option == '3':
            add_credit()
        elif option == '4':
            exit_program()
            break
#run checkbook
main()