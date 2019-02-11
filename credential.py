class Credential:
    '''
    class that generates new instance for credentials
    '''
    credentail_list=[]
    def __init__(self,account_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New credential account name.
            password : New credential password.
        '''
        self.account_name = account_name
        self.password = password