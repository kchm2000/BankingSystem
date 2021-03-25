# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 19:43:31 2021
This Simple Banking system was created by Choo Hongming Kent.
Run through the menus to simulate your banking activities.
@author: kchm2
"""
from Account import Account
        
#create set for account objects and set for NRIC to check for duplicate NRIC
set_of_accounts = set()
set_of_NRIC = set()

import os
import json

# function to check whether the text file containing is present and has data
def is_not_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
#if text file with info is there then execute code block below to load info into set_of_accounts and set_of_NRIC
if is_not_non_zero_file('Acc.txt'):
    with open('Acc.txt', 'r') as file_in:
     
        for line in file_in:
        #strip lines of spaces and retrieves the dictionary files and instantiate them as Account objects
           line_strip = line.strip()
           info = json.loads(line_strip)
           account = Account(info["_nric"],info["_name"],info["_pin"],info["_balance"])
           set_of_accounts.add(account)     
           set_of_NRIC.add(info["_nric"])
    file_in.close

#check that NRIC not repeated 
def check_NRIC_not_repeated():
    is_valid_NRIC = False
    
    while not is_valid_NRIC:
    # asks for input of NRIC number
        ask_NRIC = str(input("Please input NRIC: "))
        #if NRIC is already in system will ask again
        if ask_NRIC in set_of_NRIC:
            print("the NRIC is already in our system use a new one")
        #if NRIC is not set then generate new account
        elif ask_NRIC not in set_of_NRIC:
            is_valid_NRIC = True
            nric = ask_NRIC
    return nric


def check_balance_valid(pop_up_text):
    is_valid_balance = False
    
    while not is_valid_balance:
    # asks for input of balance
        ask_balance = str(input(pop_up_text))
        #if ask_balance is a number with no decimal
        if ask_balance.isnumeric():
            is_valid_balance = True
            return float(ask_balance)
        #if ask_balance is a string with 1 decimal point hence can be a float
        elif ask_balance.count(".")==1 and ask_balance.replace(".","").isnumeric():
            is_valid_balance = True
            return float(ask_balance)
        else:
            print("Error in input please input again.")
  

def create_account():
    print("Choice number 1 is selected by the customer\n")
    
    # creates new accounts with the attributes limit to 9 accounts to keep project small
    if len(set_of_accounts) < 10:
        nric = check_NRIC_not_repeated()
        name = str(input("Input Fullname : "))
        pin = str(input("Please input a pin of your choice : "))
        balance = check_balance_valid("Please input a amount to deposit to start an account: ")

        #create Account object and add the set_of_accounts
        account = Account(nric, name, pin, balance)
        set_of_accounts.add(account)

        print("\n----New account created successfully !----")
        print("Note! Please remember the Name and Pin")
        print("========================================")

    else:
        print("\nCustomer registration exceed reached the no:of spaces left are: " + str((len(set_of_accounts)) - 10))

    # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def withdraw():
    print("Choice number 2 is selected by the customer\n")

    available = False

    nric = input("Please input nric : ")
    pin = input("Please input pin : ")
    # This while loop will prevent the user using the account if the username or pin is wrong.
    for account in set_of_accounts:
        if account.get_nric() == nric and account.get_pin() == pin:
            available = True
            # These few statement would show the balance taken from the list.
            print("Your Current Balance: " + str(account.get_balance()) + "-/Dollars\n")
            balance = (account.get_balance())
            # Statement below would take the amount to withdraw from user.
            withdrawal = check_balance_valid("Input amount to Withdraw : ")
            # The if condition below would look whether the withdraw is greater than the balance.
            if withdrawal > balance:
                # Please deposit more before withdrawing more money.
                print("Please Deposit more money because your Balance is not enough for such a large withdrawal : ")
                break
                
            else:
                # Else condition mentioned above is to do withdrawal if the balance is greater than the
                # withdraw amount.
                balance = balance - withdrawal
                # These few statement would update the values in the list and show it to the customer.
                print("\n----Withdraw Successful!----")
                account.set_balance(balance)
                print("Your New Balance: " + str(balance) + " -/Dollars\n\n")
    if not available:
        # The if condition above would work when the pin or the name is wrong.
        print("Your name and pin does not match!\n")

        # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def deposit():
    print("Choice number 3 is selected by the customer\n")

    available = False

    nric = input("Please input nric : ")
    pin = input("Please input pin : ")
    # The while loop below would work when the pin or the username is wrong.
    for account in set_of_accounts:
        if account.get_nric() == nric and account.get_pin() == pin:
            available = True
            # These statements below would show the customer balance and update list values according to
            # the deposition made.
            print("Your Current Balance: " + str(account.get_balance()) + " -/Dollar")
            balance = account.get_balance()
            # This statement below takes the deposition from the customer.
            deposition =  check_balance_valid("Enter the value you want to deposit : ")
            balance = balance + deposition
            account.set_balance(balance)
            print("\n----Deposition successful!----")
            print("Your New Balance: " + str(balance) + " -/Dollar\n\n")

    if not available:
        print("Your name and pin does not match!\n")
    # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


def print_all_customers():
    print("Choice number 4 is selected by the customer\n")
    
    #password so that only bank employee can view all customers
    password = input("Please input bank password to view all customers: ")
    if password == "password":
        print("\nCustomer name list and balances mentioned below: \n")
        #convert accounts from set to list so that delete them based on the list index and sort them based on name
        list_of_accounts = list(set_of_accounts)
        list_of_accounts.sort(key=lambda x: x._name)
        if len(set_of_accounts) > 0:
            # The while loop below will keeping running until all the customers and balances are shown.
            for index, account in enumerate(list_of_accounts):
                print(str(index+1) + "->. NRIC = " + str(account.get_nric()))
                print("---->. Customer = " + str(account.get_name()))
                print("---->. Balance = " + str(account.get_balance()) + " -/Dollars\n")
        # if there is no accounts        
        elif len(set_of_accounts)==0:
            print("no customers in database")
        # This statement below helps the user to go back to the start of the program (main menu).        
        input("Please press enter key to go back to main menu to perform another function or exit ...")
        
    else:
        print("password incorrect user not allowed to see customer list")
        input("Please press enter key to go back to main menu to perform another function or exit ...")

def choose_valid_del_num(num_customer):
    #initialize as false first for the while loop to keep asking for a valid number
    is_valid_num = False 
    correct_range = [str(x) for x in range(1,num_customer+1)]
    #if in delete choice is within the correct range then serial number will be accepted 
    while not is_valid_num:
        delete_choice = (input("Please choose the serial no. of the account you want deleted: "))
        if delete_choice in correct_range:
            is_valid_num = True 
            return int(delete_choice)
        else:
            print("input invalid choose suitable serial number.")
    
def delete_customer():
    print("Choice number 5 is selected by the customer\n")
    
    #password so that only bank employee can delete customers
    password = input("Please input bank password to delete customers: ")
    if password == "password":
        print("\nCustomer name list and balances mentioned below: \n")
        #convert accounts from set to list so that delete them based on the list index and sort them based on name
        list_of_accounts = list(set_of_accounts)
        list_of_accounts.sort(key=lambda x: x._name)
        if len(set_of_accounts) > 0:
            # The while loop below will keeping running until all the customers and balances are shown.
            for index, account in enumerate(list_of_accounts):
                print(str(index+1) + "->. NRIC = " + str(account.get_nric()))
                print("---->. Customer = " + str(account.get_name()))
                print("---->. Balance = " + str(account.get_balance()) + " -/Dollars\n")
            #choose the serial number you want to delete    
            delete_index = choose_valid_del_num(len(list_of_accounts))
            del(list_of_accounts[delete_index-1])
            
            #recreate the set for accounts and nric
            new_set_of_accounts = set()
            new_set_of_NRIC = set()
            for account in list_of_accounts:
                new_set_of_accounts.add(account)
                new_set_of_NRIC.add(account.get_nric())
                
            print("\nCustomer Serial No." + str(delete_index) + " successfully deleted \n")
            return new_set_of_accounts, new_set_of_NRIC
            
            
        #if no accounts
        elif len(set_of_accounts)==0:
            print("no customers to delete")
                        
        input("Please press enter key to go back to main menu to perform another function or exit ...")
    
    else:
        print("password incorrect user not allowed to see customer list")
        input("Please press enter key to go back to main menu to perform another function or exit ...")

def exit_program():
    # These statements would be just showed to the customer.
    print("Choice number 6 is selected by the customer")
    print("Thank you for using our banking system!\n")
    print("Come again")
    print("Bye bye")
    
    if len(set_of_accounts) > 0:
    # Loop to out class variables into text file for future use
        with open("Acc.txt", 'w') as f:
            for account in set_of_accounts:
                jsonstr = json.dumps(account.__dict__)
                f.write(jsonstr)
                f.write("\n")
            f.close

def invalid_function():
    print("Invalid option selected by the customer")
    print("Please Try again!\n")
    # This statement below helps the user to go back to the start of the program (main menu).
    input("Please press enter key to go back to main menu to perform another function or exit ...")


while True:
    
    print("")
    print("=====================================")
    print(" -------Welcome to Kent Bank-------- ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Delete Customer            >>=")
    print("=<< 6. Exit/Quit                  >>=")
    print("*************************************")
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        # This function will open a new account.
        create_account()
    elif choiceNumber == "2":
        # This function will withdraw money from a specific account.
        withdraw()
    elif choiceNumber == "3":
        # This function will deposit money to a specific account.
        deposit()
    elif choiceNumber == "4":
        # This function will print all the available customers.
        print_all_customers()
    elif choiceNumber == "5":
        # This function is the point of exit from the program.
        set_of_accounts , set_of_NRIC = delete_customer()
    elif choiceNumber == "6":
        # This function is the point of exit from the program.
        exit_program()
        break
    else:
        # This else function above would work when a wrong function is chosen.
        invalid_function()