import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test
        '''
        self.new_credential=Credential("tweeter","tweet00")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"tweeter")
        self.assertEqual(self.new_credential.password,"tweet00")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into credential list
        '''
        self.new_credential.save_credential()   
        self.assertEqual(len(Credential.credential_list),1) 

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''    
        self.new_credential.save_credential()
        test_credential = Credential("tweeter","tweet00")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

if __name__=='__main__':
    unittest.main()        

