import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_user=User("nic","hat","term00","term00")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"nic")
        self.assertEqual(self.new_user.last_name,"hat")
        self.assertEqual(self.new_user.create_pw,"term00")
        self.assertEqual(self.new_user.confirm_pw,"term00")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
    
    

if __name__ == '__main__':
    unittest.main()