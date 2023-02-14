#initialize modules, and variables
import os
import csv
balance = 0
amount = 0
transaction_id = 0
#name colums and rows
cols = ['transaction_id','amount','transaction_type']
transaction = {'transaction_id': 1,'amount':0,'transaction_type':'debit'}

#********function to write csvs********
def write_to_csv(file_name, fieldnames, transaction):
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(transaction)

#function to clear checkbook history
def clear_checkbookpy_history():
    write_to_csv('checkbookpy.csv', cols, transaction)

#function to get balance
def get_balance():
    print('your current balance is: $',balance)

#function to exit
def exit_cb():
    print('Thanks for stopping by, see ya!')

#function to add debit
def add_deposit(amount):
    global balance
    global transaction_id
    transaction_id += 1
    transaction_type = 'credit'
    balance += amount
    with open('checkbookpy.csv', 'a', newline='') as cb:
        writer = csv.writer(cb)
        writer.writerow([transaction_id, amount, transaction_type])

#function to subtrack withdrawal
def add_withdrawal(amount):
    global transaction_id
    global balance
    transaction_id += 1
    transaction_type = 'debit'
    balance -= amount
    with open('checkbookpy.csv', 'a', newline='') as cb:
        writer = csv.writer(cb)
        writer.writerow([transaction_id, amount, transaction_type])

#function to call checkbook csv
def read_checkbookpy():
    with open('checkbookpy.csv', 'r') as cb:
        reader = csv.reader(cb)
        for row in reader:
            print(row)

#this is all the code to run the checkbook program
print('Welcome to Checkbook! Here are your options:\n1) view current balance\n2) record a transaction\n3) exit')
home_input = input('What would you like to do? ')
while True:
    if home_input == '1':
        print('your current balance is: ',balance)
        break
    elif home_input == '2':
        print('what type of transaction? \n1) withdrawal\n2) deposit')
        transaction_type = input('Transaction Type: ')
        if transaction_type == '1':
            amount = input('how much are you withdrawaling today?: ')
            add_withdrawal(float(amount))
            print(f'your new balance is: ', balance)
            done = input('done? y or n: ')
            if done == 'y':
                print('goodbye')
            else:
                continue
        if transaction_type == '2':
            amount = input('how much are you deposting today?: ')
            add_deposit(float(amount))
            print(f'your new balance is: ', balance)
            done = input('done? y or n): ')
            if done == 'y':
                print('goodbye')
            else:
                continue
        break
    elif home_input == '3':
        exit_cb()
        break
    else:
        print('invalid entry, try again')
        break
        continue
        break