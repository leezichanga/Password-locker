import unittest #import the unittest module
import pyperclip
from password import passwords #importing credentials class

class TestPasswords(unittest.TestCase):
    '''
    defines test cases for the password class behaviours
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_account = passwords("Account","Testname","TestPass")

    def tearDown(self):
        '''
        clean up after each test case has run
        '''
        passwords.password_list = []

    def test_init(self): #first test
        '''
        test if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,"Account")
        self.assertEqual(self.new_account.user_name,"Testname")
        self.assertEqual(self.new_account.password,"TestPass")

    def test_save_account(self): #second test
        '''
        test if the account is saved into the passwords list
        '''
        self.new_account.save_account() #saving the new account
        self.assertEqual(len(passwords.password_list),1)

    def test_save_multiple_accounts(self): #third test
        '''
        test to check if one can save multiple accounts
        '''
        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        self.assertEqual(len(passwords.password_list),2)

    def test_delete_passwords(self): #fourth test
        '''
        test to check if one can delete account passwords
        '''
        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        self.new_account.delete_account() #deleting credentials
        self.assertEqual(len(passwords.password_list),1)

    def test_find_account_by_account_name(self): #fifth test
        '''
        test to search for account details
        '''
        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        found_account = passwords.find_by_account("Account")
        self.assertEqual(found_account.user_name, test_account.user_name)

    def test_account_exists(self): #sixth test
        '''
        test to check if account really exists
        '''
        self.new_account.save_account()
        test_account = passwords("Account","Testname","TestPass")
        test_account.save_account()
        account_exists = passwords.account_exists("Account")
        self.assertTrue(account_exists)

    def test_display_accounts(self): #seventh test
        '''
        test to display accounts
        '''
        self.assertEqual(passwords.display_accounts(),passwords.password_list)

if __name__ == '__main__':
    unittest.main()
