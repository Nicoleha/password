#!/usr/bin/env python3.6
from user import User
from credential import Credential
import string
import random

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

def check_existing_credentials(name):
    '''
     Function that check if a credential exists with that account name and return a Boolean
    '''
    return Credential.credential_exist(name)

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))    


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
        print("Use these short codes: cp - create a new new password"," dp - display created password ", " fp - find a password"," ex - exit app", "delp - to delete contact", "gp - generate password")    
        
        short_code=input().lower()

        if short_code == 'cp':  
            print("New Contact")
            print("-"*10)

            print("Account name ...")
            account_name=input()

            print("password ...")
            password=input()

            save_credentials(create_credential(account_name,password))
            print('\n')
            print(f"new password {account_name}  {password} created")
            print('\n') 

        elif short_code=='dp':
            if display_credentials():
                print("here is a list of all your contacts")
                print('\n')

                for credential in display_credentials():
                    print(f"{credential.account_name}  {credential.password}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any password saved yet")
                print('\n')


        elif short_code == 'fp':
            print("enter the name of the accoutn you want to search password for:")
            search_name=input()
            if check_existing_credentials(search_name):
                search_name=find_credential(search_name)
                print(f"{search_name.account_name} {search_name.password}")
                print('-'*20)

                print(f"account name ........ {search_name.account_name}")
                print(f"password ........ {search_name.password}")
            else:
                print("account name does not exist")

        elif short_code == 'delp':
            print("enter name of the account you wish to delete")
            account_name=(input)

            if check_existing_credentials(account_name):
                Credential =find_credential(account_name) 
                del_credentials(Credential)
                print(f"{credential.account_name} deleted")
                print('\n')

                print("credential deleted")
            else:
                print("account name does not exist")  

        elif short_code == 'gp':
            print(pw_gen(int(input('How many characters in your password?'))))   


        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()


    
