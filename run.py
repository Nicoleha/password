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

def del_credentials(credential):
    '''
    function to delete delete credentials
    '''
    credential.delete_credential()

def find_credential(name):
    '''
    function that finds a credential by name and returns the contact
    '''
    return Credential.find_by_name(name)  

def display_credentials():
    '''function that returns all saved credentials
    '''
    return Credential.display_credentials()


def main():
    print("Welcome to password locker app.What is your name?")
    user_name=input()

    print(f"Hello {user_name}. To continue further you have to create an account")
    print('\n')

    print("first Name ...")
    f_name=input()

    print("Last name ...")
    l_name = input()

    print("Create Password ...")
    cr_pw = input()

    print("Confirm Password ...")
    fi_pw = input()


    if cr_pw == fi_pw:
        print("account successfully created")
    else:
        print("password incorrect")  

    while True:
        print("Use these short codes: cp - create a new new password"," dp - display created password ", " fd - find a password"," ex - exit app")    
        
        short_code=input().lower()

        if short_code == 'cp':  
            print("New Contact")
            print("-"*10)

            print("Account name ...")
            acc_name=input()

            print("password ...")
            password=input()

            save_credentials(create_credential(acc_name,password))
            print('\n')
            print(f"new password {acc_name}  {password} created")
            print('\n')    




if __name__ == '__main__':

    main()


    
