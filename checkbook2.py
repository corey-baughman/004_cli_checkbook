## MODULES IMPORTED FOR THIS APP

# import os module to check path against system
import os

# import csv module to transfer data between python usable dictionaries
# and storage as comma separated values in a .txt file
import csv


## FUNCTIONS CREATED FOR THIS APP:

def check_balance():
    with open('transaction_data.txt', 'r') as td:
        trans_data = csv.DictReader(td)
        trans_dict = []
        for transaction in trans_data:
            trans_dict.append(transaction)
    total_balance = 0
    for transaction in trans_dict:
        total_balance += float(transaction['amount'])
    print(f'Your total balance is ${total_balance:,.2f}')

# function to add a debit (withdrawal) from user input
def add_debit():
    while True:
        wd_amt = input("What is the amount of the withdrawal? \n")
        wd_amt = float(wd_amt.strip('$').replace(',', ' ')) * (-1)
        if wd_amt >= 0:
            print('Withdrawal NOT entered.'
                  'Please enter the amount as a positive number')
            continue
        else:
            with open('transaction_data.txt', 'a') as td:
                td.writelines(f'debit,{wd_amt}\n')
            print(f'You entered a debit of ${-1 * wd_amt:,.2f}\n')
            break

# function to add a credit (deposit) from user input
def add_credit():
    while True:
        dep_amt = input("What is the amount of the deposit? \n")
        dep_amt = float(dep_amt.strip('$').replace(',', ' '))
        if dep_amt <= 0:
            print('Deposit NOT entered.\nPlease enter the amount as a positive number')
            continue
        else:
            with open('transaction_data.txt', 'a') as td:
                td.writelines(f'credit,{dep_amt}\n')
            print(f'You entered a deposit of ${dep_amt:,.2f}\n')
            break
                
def close_program():
    print('Thanks, have a great day!')
    exit()   
    
                
## DATA FILE VALIDATE OR CREATE

# check for the file that holds or will hold transaction data
if os.path.exists('/Users/donq/codeup-data-science/cli_checkbook/transaction_data.txt'):
    print('Transaction data file found')
    with open('transaction_data.txt') as td:
        lines = td.readlines()

# if there is no transaction data file found, a new one is created       
else:
    with open('transaction_data.txt', 'a') as td:
        td.writelines('transaction_type,amount\n')
    print('Transaction data file NOT found. New file created.')
    
    
## WELCOME BANNER
        
# print a welcome message to user
print('\n\n\n~~~ Welcome to your terminal checkbook! ~~~\n\n\n')


## CORE APPLICATION LOOP

# user input prompt as while loop
while True:
    
    # show user the menu
    print("What would you like to do?\n\n"
          "1) View current balance\n"
          "2) Record a debit (withdrawal)\n"
          "3) Record a credit (deposit)\n"
          "4) Exit\n")

    # user chooses menu option
    user_input = input('Your choice? \n')

    # user wants to view account balance
    if user_input.startswith('1'):
        check_balance()
        
    # user wants to add a withdrawal
    elif user_input.startswith('2'):
        add_debit()
        
    # user wants to add a deposit
    elif user_input.startswith('3'):
        add_credit()
                
    # user wants to exit the program
    elif user_input.startswith('4'):
        close_program()
        break
         
    else:
        print('Invalid input.'
              'Please type the number of one of the menu items.\n')

