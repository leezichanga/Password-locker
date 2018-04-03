import random
import pyperclip
class user:
    '''
    class that generates new instances of user account
    '''
    user_list = []
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd

    def save_user(self):
        '''
        save user details into user_list
        '''
        user.user_list.append(self)

    def generate_password(self):
        '''
        generate new password
        '''
        chars = '1234567890abcdefghijklmnop?/@-' #characters to choose from
        length = int(input("Enter the length of password you want: "))
        pwd = ''
        for c in range(length):
            pwd += random.choice(chars) #generate random password
        print (pwd)

class passwords:
    '''
    class that generates new instances of passwords
    '''
    password_list = []
    def __init__(self,account_name,user_name,password):
        '''
        init method helps us define properties for our objects
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_account(self):
        '''
        save contact object into password_list
        '''
        passwords.password_list.append(self)

    def delete_account(self):
        '''
        delete account
        '''
        passwords.password_list.remove(self)

    @classmethod
    def find_by_account(cls,account_name):
        '''
        search for account, returns a list containing the account passwords
        args:
             account_name: that will be used to search
        Returns:
            account passwords
        '''
        for account in cls.password_list:
            if account.account_name == account_name:
                return account

    @classmethod
    def account_exists(cls, account_name):
        '''
        check if account really exists.
        args:
             account_name: that will be used to check if account exists
        Returns:
            boolean: depending if the account exists
        '''
        for account in cls.password_list:
            if account.account_name == account_name:
                return True
        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns account details
        '''
        return cls.password_list
