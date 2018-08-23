'''
Created on Aug 21, 2018

@author: Do Anh Tu
'''
import re
import hashlib
import os
# import getpass

class PasswordManager():
    '''
    Provide the password management methods
    '''
    PASSWORD_PATTERN_CHECKS =   [
                                    ['\d', 'does not contain a digit'],
                                    ['[A-Z]', 'does not contain a upper-case character'],
                                    ['[a-z]', 'does not a lower-case character'],
                                    ['\W', 'does not contains a symbol'],
                                    ['^(?!.* ).*$', 'does not contains any white space'],
                                    ['^.{6,}$', 'minimum length was not 6']
                                ]

    def __init__(self, username=None, encrypted_password=None):
        '''
        Constructor
        '''
        self.__username = username
        self.__encrypted_password = encrypted_password
        
    def _encrypt(self, plain_text):
        '''
        This method takes a password (string) and returns the encrypted form of the password
        '''
        if not plain_text:
            raise Exception("plain_text should not be None or Empty")
        
        # just a simple hash, not encrypt
        encryped_text = hashlib.sha1(plain_text.encode('utf-8')).hexdigest()
        return encryped_text
    
    def _verifyPassword(self, plaintext_password):
        '''
        This method takes a string (a password) and returns true if, once encrypted,
        it matches the encrypted string stored in the member variable. Else returns false
        '''
        if self._encrypt(plain_text=plaintext_password) == self.__encrypted_password:
            return True
        
        return False
    
    def _verifyUsername(self, username):
        '''
        This method takes a string (a user name) and returns true if 
        it matches the username string stored in the member variable. Else returns false
        '''
        if self.__username == username:
            return True
        
        return False
    
    def encryptPassword(self, plain_text_password):
        '''
        This method takes a password (string) and returns the encrypted form of the password
        '''
        return self._encrypt(plain_text=plain_text_password)
    
    def showPasswordRules(self):
        password_rules =  '''
            |-------------------------------------------------------------------------------------------|
            |    Password rules:                                                                        |
            |    - The password must not contain any whitespace                                         |
            |    - The password must be at least 6 characters long.                                     |
            |    - The password must contain at least one uppercase and at least one lowercase letter.  |
            |    - The password must have at least one digit and symbol.                                |
            |-------------------------------------------------------------------------------------------|
        '''
        print(password_rules)
        
    def validatePassword(self, plaintext_password):
        '''
        This method takes a string (a password) and returns true if it meets the following criteria
        - The password must not contain any whitespace
        - The password must be at least 6 characters long.
        - The password must contain at least one upper-case and at least one lower-case letter.
        - The password must have at least one digit and symbol.
        If the password does not meet these requirements,
        the program should display a message telling the user why the password is invalid,
        specifically. It should also continue to loop until the user enters a valid password.
        '''
        is_valid = True
        error_message = '\tINVALID: your password:'
        for check in PasswordManager.PASSWORD_PATTERN_CHECKS:
            if not re.search(check[0], plaintext_password):
                error_message = '{0}{1}\t\t- {2}'.format(error_message, os.linesep, check[1])
                is_valid = False
        
        if is_valid:
            print("Password is valid!")
            return True
        else:
            print(error_message)
            return False
    
    def validateUsername(self, username):
        '''
        This method takes a string (a proposed user name)
        if user name is not None, returns true.
        Otherwise returns false.
        '''
        if username:
            print("User name OK!")
            return True
        else:
            print("Invalid user name!")
            return False  
         
    def setNewPassword(self, plaintext_password):
        '''
        This method takes a string (a proposed password). If it meets the criteria in validatePassword,
        it encrypts the password and stores it in the member variable and returns true.
        Otherwise returns false.
        '''
        validation_result = self.validatePassword(plaintext_password=plaintext_password)
        if validation_result == True:
            self.__encrypted_password = self._encrypt(plain_text=plaintext_password)
            print("Password OK!")
            return True
        else:
            print("    Invalid password! %s." % validation_result)
            return False

            
            