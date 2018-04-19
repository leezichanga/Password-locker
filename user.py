import random

class user:
    """
    creates a class user that acts as a blueprint for all object instances of a user
    """

    user_list = []
    """
    created a list where all new user objects will be stored
    """

    def __init__(self, username, email, password):
        """
        the __init__ method is for defining the properties of the created class User
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        method saves a new user into the user_list
        """
        User.user_list.append(self)

    def generate_password(self, account_password):
        print("How many digits do you want in your generated password?")
        y = input()
        for x in range (y):
            account_password = random.randint(1, 10)
            print(account_password)
