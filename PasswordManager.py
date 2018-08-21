'''
Created on Aug 21, 2018

@author: Do Anh Tu
'''
import re
import hashlib
import os, json
# import getpass

class PasswordManager():
    '''
    Provide the password management methods
    '''
    STORAGE_FILEPATH = "password.txt"
    PASSWORD_PATTERN_CHECKS =   [
                                    ['\d', 'password must contains a digit'],
                                    ['[A-Z]', 'password must contains an upper-case character'],
                                    ['[a-z]', 'password must contains a lower-case character'],
                                    ['\W', 'password must contains a symbol'],
                                    ['^(?!.* ).*$', 'password must not contains any white space'],
                                    ['^.{6,}$', 'password minimum length is 6']
                                ]

    def __init__(self):
        '''
        Constructor
        '''
        # load user name and password from file
        if os.path.exists(PasswordManager.STORAGE_FILEPATH):
            username, encrypted_password = self.loadUserInfoFromFile()
            self.__username = username
            self.__encrypted_password = encrypted_password
        else:
            self.__username = None
            self.__encrypted_password = None
        
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
    
    def login(self, username, plaintext_password):
        '''
        Login method, check user name an password if match, return true
        Else returns false
        '''
        result =    self._verifyUsername(username=username) \
                    and self._verifyPassword(plaintext_password=plaintext_password)
                    
        if result:
            print("Login successfully!")
            return True
        else:
            print("Login failed!")
            return False 
    
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
        
        for check in PasswordManager.PASSWORD_PATTERN_CHECKS:
            if not re.search(check[0], plaintext_password):
                return check[1]
        return True
    
    def setNewUserName(self, username):
        '''
        This method takes a string (a proposed user name)
        if user name is not None, store it in the member variable and returns true.
        Otherwise returns false.
        '''
        if username:
            self.__username = username
            self.__encrypted_password = None
            self.saveUserInfoToFile(self.__username, self.__encrypted_password)
            print("User name saved!")
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
            self.saveUserInfoToFile(self.__username, self.__encrypted_password)
            print("Password saved!")
            return True
        else:
            print("    Invalid password! %s." % validation_result)
            return False

    def saveUserInfoToFile(self, username, encrypted_password):
        f = open(PasswordManager.STORAGE_FILEPATH, 'w')
        user_info = {
                        'username' : username,
                        'encrypted_password': encrypted_password
                    }
        str_user_info = json.dumps(user_info)
        f.write(str_user_info)
        f.close()
    
    def loadUserInfoFromFile(self):
        f = open(PasswordManager.STORAGE_FILEPATH, 'r')
        str_user_info = f.read()
        f.close()
        user_info = json.loads(str_user_info)
        return (user_info['username'], user_info['encrypted_password'])
            
            