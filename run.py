#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(fname,lname,cpw,fpw):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,cpw,fpw)
    return new_user

def create_credential(acc_name,password):
    '''
    function to create a new credential
    '''
    new_credential=Credential(acc_name,password)
    return new_credential

def login_users(user):
    '''
    function to login user 
    '''
    user.login_user()

def save_credentials(credential):
    '''
    function to login user 
    '''
    credential.save_credential()

def del_credentials(Credential):
    '''
    function to delete delete credentials
    '''
    credential.delete_credential()

def find_credential(name):
    '''
    function that finds a credential by name and returns the contact
    '''
    return Credential.find_by-name(name)    
    
