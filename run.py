#!/usr/bin/env python3.6
import random
from password import passwords
from password import user
#methods for user
def create_user(name,pwd):
    '''
    function to create new user
    '''
    new_user = user(name,pwd)
    return new_user
def save_user(user):
    '''
    function to save user details
    '''
    user.save_user()
def generate_password(user):
    '''
    function to generate password
    '''
    user.generate_password()

#methods for passwords
def create_account(account_name, user_name, password):
    '''
    function to create new account
    '''
    new_account = passwords(account_name, user_name, password)
    return new_account

def save_account(account):
    '''
    function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    function to delete account
    '''
    account.delete_account()

def find_account(account_name):
    '''
    function to find account by account name
    '''
    return passwords.find_by_account(account_name)

def check_existing_account(account_name):
    '''
    function that checks if account exists
    '''
    return passwords.account_exists(account_name)

def display_accounts():
    '''
    function that returns saved accounts
    '''
    return passwords.display_accounts()


def main():
    print("--------------------Password Locker-------------------")
    print('''Do you ever want to easily access your passwords
without having to memorize??
        Well here is a chance to save all your passwords in a
        single location''')
    print("\n")
    print("Enter your name: ")
    username = input()
    print("*"*78)
    print(f"Hello {username}.\nDo you want to enter a password or we automatically generate for you?")
    print('''
        Press:
                    g- generate new password
                    c- create your own password
          ''')
    pwd_click = input()
    if (pwd_click  == 'g'):
        chars = '1234567890abcdefghijklmnop?/@-' #characters to choose from
        length = int(input("Enter the length of password you want: "))
        pwdinput = ''
        for c in range(length):
            pwdinput += random.choice(chars) #generate random password
        print (pwdinput)
        print(f"{username} your password is {pwdinput}")

    elif (pwd_click == 'c'):
        print("enter your password: ")
        pwdinput = input()
        print(f"{username} your password is {pwdinput}")

        print("\n"*2)

    save_user(create_user(username,pwdinput))
    #create and save user passwords
    print('\n' * 2)
    print (f"New user {username} created.")
    print('\n' * 2)

    print("To continue reenter your details")
    print("*"*78)
    print("Enter your username again: ")
    name = input()
    print("Enter your password: ")
    pwd = input()
    if (name == username and pwd == pwdinput):
        print('\n')
        while True:
            print('''Use the following short codes:
                  c - create new account to save
                  d - display accounts saved
                  f - find saved account
                  ex - exit
                  ''')
            short_code = input().lower()
            if short_code == 'c':
                print("---------------------New account--------------------")
                print("-"*80)
                print("Account Name: ")
                account_name = input()
                print("User Name: ")
                user_name = input()
                print("Password for account: ")
                password = input()

                save_account(create_account(account_name,user_name,password))
                             #create and save account credentials
                print('\n' * 1)
                print (f"New account {account_name} created.")
                print('\n' * 1)

            elif short_code == 'd':
                if display_accounts():
                    print("Here is a list of all your accounts: ")
                    print('\n')
                    for account in display_accounts():
                        print(f"{account.account_name}  {account.user_name}  {account.password}")
                        print('\n')
                else:
                    print('\n')
                    print("You dont have any saved acccounts yet")
                    print('\n')

            elif short_code == 'f':
                print("Enter the name of the account you want to search for: ")
                search_account_name = input()
                if check_existing_account(search_account_name):
                    search_account = find_account(search_account_name)
                    print(f"{search_account.account_name}")
                    print('-' * 20)
                    print(f"User Name...................{search_account.user_name}")
                    print(f"Password...................{search_account.password}")

                else:
                    print("Account does not exist")

            elif short_code == 'ex':
                print("Thanks for your time! Bye!")
                break
            else:
                print("Sorry didnt get that! Please use the short codes")

    else:
        print('''Incorrect Name or Password
Run the application again''')

if __name__ == '__main__':
    main()
