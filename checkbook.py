# import os module to check path against system
import os

# import sys module
import sys

# check for the file that holds or will hold transaction data

if os.path.exists('/Users/donq/codeup-data-science/cli_checkbook/transaction_data.txt'):
    print('Transaction data file found')
    with open('transaction_data.txt') as td:
        lines = td.readlines()

# if there is no transaction data file found, a new one is created       

else:
    with open('transaction_data.txt', 'w') as td:
        td.write('brand new file!')
    print('Transaction data file NOT found. New file created.')
    
    
# print a welcome message to user

print('\n\n\n~~~ Welcome to your terminal checkbook! ~~~\n\n\n')

# print the basic menu question for user

print("What would you like to do?\n")

# print menu

print("1) view current balance\n2) record a debit (withdraw)\n3) record a credit\n4) exit\n")

# print user input prompt

user_input = input('Your choice? ')

if user_input.startswith('1'):
    print('current balance feature coming soon')
elif user_input.startswith('2'):
    print('add a debit (withdrawal) coming soon')
elif user_input.startswith('3'):
    print('add a credit (deposit) coming soon')
elif user_input.startswith('4'):
    print('Thanks, have a great day!')
    exit()
    
else:
    print('Invalid input.\nPlease type the number of one of the menu items.\n')

