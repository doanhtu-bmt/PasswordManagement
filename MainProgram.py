'''
Created on Aug 20, 2018

@author: Do Anh Tu
'''
from PasswordManager import PasswordManager

if __name__ == '__main__':
        
    pm = PasswordManager()

    exit_program = False
    
    while (not exit_program):
        print('''
            ==== Home Test for Software Engineer ====
            
            Menu:
                A. New User
                B. Validate Password
                C. Login
                D. Change Password
                E. Exit
                
            ''')
        menu_selection = input(prompt="Enter your choice: ")
        
        # Menu cases
        if menu_selection.upper() == "E":
            print("Program exit. Bye!")
            break
        
        elif menu_selection.upper() == "A":
            result = False
            while (not result):
                username = input(prompt="Enter user name: ")
                result = pm.setNewUserName(username=username)
                
        elif menu_selection.upper() == "B":
            result = False
            while (not result):
                password = input(prompt="Enter password: ")
                result = pm.setNewPassword(plaintext_password=password)
                
        elif menu_selection.upper() == "C":
#             result = False
#             while (not result):
                username = input(prompt="Enter user name: ")
                password = input(prompt="Enter password: ")
                result = pm.login(username=username, plaintext_password=password)
    
        elif menu_selection.upper() == "D":
#             result = False
#             while (not result):
                username = input(prompt="Enter user name: ")
                current_password = input(prompt="Enter current password: ")
                result = pm.login(username=username, plaintext_password=current_password)
                if result:
                    result = False
                    while (not result):
                        new_password = input(prompt="Enter new password: ")
                        result = pm.setNewPassword(plaintext_password=new_password)
     
