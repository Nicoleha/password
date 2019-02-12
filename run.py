#!/usr/bin/env python3.6
from user import User
from credential import Credential
import string
import random
import sys 


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
    function that finds a credential by name and returns the password
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
    print("Welcome to password locker app.Enter your first and last name please?")
    print('\n')
   
    print("first Name ...")
    f_name=input()

    print("Last name ...")
    l_name = input()

    print(f"Hello {f_name}  {l_name}. To continue further you have to create a password and confirm it!")
    print('\n')


    print("Create Password ...")
    cr_pw = input()

    print("Confirm Password ...")
    fi_pw = input()

    login_users(create_user(f_name,l_name,cr_pw,fi_pw)) 

    if cr_pw == fi_pw:
        print(f"account for {f_name}  {l_name}  successfully created ")
        print('\n')
    else:
        print(f"password {cr_pw} or {fi_pw} incorrect. Next time , Please confirm the password correctly.")  
        sys.exit()
        
    print("now let procceed to login to our account")
    print('\n')
    print("enter your first name (the name must the same to the as the first name you entered previously ):")
    print('\n')
    print("enter first name")
    login_name=input()
    print("enter password")
    passw=input()
    
    if fi_pw==passw and f_name==login_name:
        print("successfully logged in")
        print('\n')
    else:
        print(f"password: {passw} or name: {login_name} incorrect. Next time , Please confirm the password correctly.")  
        sys.exit()   

    while True:
        print("Use these short codes: cp - create a new password"," dp - display created password ", " fp - find a password", "delp - to delete password", "gp - generate password"," ex - exit app")    
        
        short_code=input().lower()

        if short_code == 'cp':  
            print("New Password")
            print("-"*10)

            print("Account name ...")
            account_name=input()

            print("password ...")
            password=input()

            save_credentials(create_credential(account_name,password))
            print('\n')
            print(f"new password for {account_name} : {password} created")
            print('\n') 

        elif short_code=='dp':
            if display_credentials():
                print("here is a list of all your passwords")
                print('\n')

                for credential in display_credentials():
                    print(f"{credential.account_name} {credential.password}")
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
            search_name=input()

            if check_existing_credentials(search_name):
                Credential =find_credential(search_name) 
                del_credentials(Credential)
                print(f"{Credential.account_name} deleted")
                print('\n')

                print("credential and password deleted")
            else:
                print("account name does not exist")  

        elif short_code == 'gp':
            print("enter account name")
            account_name=input()
            print("enter length of the password you wish to generate(enter number)")
            size=int(input())
            password=pw_gen(size)

            save_credentials(create_credential(account_name,password))
            print('\n')
            print(f"new password {password} created")
            print('\n') 


        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()


    
