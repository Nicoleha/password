#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_credential(acc_name,password):
    '''
    function to create a new credential
    '''
    new_credential=Credential(acc_name,password)
    return new_credential