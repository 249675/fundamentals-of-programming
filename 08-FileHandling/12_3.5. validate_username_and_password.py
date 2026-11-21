#Many applications require that you create an account with a username and password to use them. Often, #applications specify requirements for the username and password. Write a program that checks whether a username #and password entered from the keyboard meet the requirements below. Use regular expressions.

#username is at least 6 characters long
#username contains only lowercase letters
#password is at least 8 characters long
#password contains only letters (lowercase and uppercase), numbers, and the underscore character


import re # Importujemy moduł do wyszukiwania tekstu za pomocą wyrażeń regularnych.

# read username and password from keyboard
username = input("Username: ")
password = input("Password: ")

# pattern (criteria) for username and password
username_match = re.fullmatch(r"[a-z]{6,}", username) # Cały login musi składać się z co najmniej 6 małych liter od a do z.
password_match = re.fullmatch(r"[a-zA-Z0-9_]{8,}", password) # Całe hasło musi mieć co najmniej 8 znaków: litery a–z lub A–Z, cyfry albo podkreślenia.

# check if username and password are ok
if username_match and password_match: # Oba wpisy muszą pasować do swoich wzorców.
    print("Username and password are valid.")
else:
    print("Username or password is invalid.")
