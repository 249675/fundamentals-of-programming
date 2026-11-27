#Create a program that handles the bank account.

#Familiarises yourself with a problem.
#Identify an object
#Define the states and behaviors of the object.
#Transform the states and behaviors of the object into the fields and methods of the class that will serve as a pattern for creating an object.
#Create a sketch of the class without creating any method content.
#Create the content of each method.
#Then, use the program and:

#Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
#Display account balance
#Deposit PLN 25,30
#Display account balance
#Withdraw PLN 31,70
#Display account balance
#Withdraw PLN 14
#Display account balance

# Szkic klasy przed implementacją: __init__(account_number),
# deposit(amount), withdraw(amount), show_info().
class BankAccount:
    # Stan konta to numer i saldo. Operacje to wpłata, wypłata i wyświetlenie danych.
    def __init__(self, account_number):
        # Podajemy numer jako tekst, już ze spacjami pomiędzy grupami cyfr.
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Dodajemy wpłatę do salda.

    def withdraw(self, amount):
        # Kwotę odejmujemy tylko wtedy, gdy saldo na to pozwala.
        if amount > self.balance:
            print("Insufficient funds on the account")
        elif amount > 0:
            self.balance -= amount

    def show_info(self):
        # Formatujemy do dwóch miejsc i zamieniamy kropkę na przecinek.
        balance = f"{self.balance:.2f}".replace(".", ",")
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {balance}")


account = BankAccount("12 3456 5555 9090 1111 0000 7722")
account.show_info()
account.deposit(25.30)
account.show_info()
account.withdraw(31.70)
account.show_info()
account.withdraw(14)
account.show_info()
