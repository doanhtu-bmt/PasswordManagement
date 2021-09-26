'''
Created on Aug 20, 2018

@author: Do Anh Tu doanhtu@live.com
'''
from PasswordManager import PasswordManager
import json, os

STORAGE_FILEPATH = "password.txt"

def saveUserInfoToFile(users_info):
    f = open(STORAGE_FILEPATH, 'w')
    str_users_info = json.dumps(users_info, indent=4, sort_keys=True)
    f.write(str_users_info)
    f.close()

def loadUserInfoFromFile():
    f = open(STORAGE_FILEPATH, 'r')
    str_user_info = f.read()
    f.close()
    users_info = json.loads(str_user_info)
    return users_info

if __name__ == '__main__':
    
    # load user names and encrypted passwords from file
    if os.path.exists(STORAGE_FILEPATH):
        all_users_info = loadUserInfoFromFile()
    else:
        all_users_info = {}
    
    def login(username, password):
        if username in all_users_info.keys():
            if all_users_info[username] == pm.encryptPassword(plain_text_password=password):
                print("Login successfully!")
                return True
            else:
                print("Login failed!")
                return False
    
    pm = PasswordManager()

    while (True):
        print('''
            ==== Home Test for Software Engineer ====
            
            Menu:
                A. New User
                B. Validate Password
                C. Login
                D. Change Password
                E. Exit
                
            ''')
        
        menu_selection = input("Enter your choice: ")
        
        # Menu cases
        if menu_selection.upper() == "E": # Exit program
            print("Program exit. Bye!")
            break # exit program loop
        
        elif menu_selection.upper() == "A": # New User
            result = False
            while (not result):
                username = input("Enter new user name: ")
                if username in all_users_info.keys():
                    print("This user is existing on the system!")
                    continue
                
                if not pm.validateUsername(username=username):
                    continue
                
                while(not result):
                    pm.showPasswordRules()
                    new_password = input("Enter password: ")
                    result = pm.validatePassword(plaintext_password=new_password)
                    if result:
                        all_users_info[username] = pm.encryptPassword(plain_text_password=new_password)
                        saveUserInfoToFile(users_info=all_users_info)
                        print("User data was saved!")
                        result = True
                        break

        elif menu_selection.upper() == "B": # Validate Password
            result = False
            while (not result):
                pm.showPasswordRules()
                password = input("Enter password: ")
                result = pm.validatePassword(plaintext_password=password)
                
        elif menu_selection.upper() == "C": # Login
            username = input("Enter user name: ")
            password = input("Enter password: ")
            login(username=username, password=password)
    
        elif menu_selection.upper() == "D": # Change password
                username = input("Enter user name: ")
                password = input("Enter password: ")
                if login(username=username, password=password):
                    result = False
                    while (not result):
                        pm.showPasswordRules()
                        new_password = input("Enter new password: ")
                        if pm.validatePassword(plaintext_password=new_password):
                            all_users_info[username] = pm.encryptPassword(plain_text_password=new_password)
                            saveUserInfoToFile(users_info=all_users_info)
                            result = True
     
