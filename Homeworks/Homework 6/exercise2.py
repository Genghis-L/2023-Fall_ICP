"""
PROGRAMMING ASSIGNMENT 06
Filename: 'exercise2.py'

The file 'exercise2.py' is a module that offers functions for managing a list of users and their
passwords.
The usernames and passwords are stored in a list of lists that we will name userList.
Each inner list represents a username/password pair in that order [username, password].
"""

# Place your imports here if any


def valid_username(user, L):
    """
    1. Displays a message (Valid , Invalid or User Name Exists) depending on username rules
    2. Returns if the username is valid → type bool
    """
    # WRITE YOUR CODE BELOW

def valid_password(pwd):
    """
    1. Displays a message ( Valid or depending on password rules
    2. Returns if the password is valid → type bool
    """
    # WRITE YOUR CODE BELOW

def add_user(L):
    """
    1. Continuously ask the user to input a username, until it is a valid one
    2. Ask for a password with the following logic:
        (a) continuously ask the user to input a password, until it is a valid one
        (b) ask the user to input the password again:
            • if the 2 passwords match → move to 3.
            • otherwise → display `Passwords do not match` and go back to 2.(a)
    3. Add the username/password pair to the userList and display User created
    """
    # WRITE YOUR CODE BELOW


    
# DO NOT CHANGE THE CODE BELLOW
if __name__ == '__main__':
    userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'],
    ['likeA', 'pwd3AAAAAA'], ['qwerty', 'pwd4QWERTY']]

    add_user(userList)

    print(userList)
