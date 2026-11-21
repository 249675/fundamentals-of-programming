#In an operating system, each user has some permissions. The user wants to perform some action that requires specific permissions. Write a program that checks whether the user has the required persmission.

required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# Sprawdzamy, czy użytkownik ma każde z wymaganych uprawnień.
has_permissions = required_permissions.issubset(user_permissions) # pytamy, czy każdy element required_permissions jest też w user_permissions. Nie jest wiec FALSE
print(has_permissions)
