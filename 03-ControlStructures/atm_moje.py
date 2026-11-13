# The atm.py program simulates a simple ATM where the user can deposit, withdraw, or check the balance. Analyze the program code and then run the program. Next, add two more functions to the program:

# Check PIN
# Change PIN
# The PIN should consist of exactly 4 digits. To check if a string contains only digits, you can use the isdigit() method. This method returns True if all characters in the string are digits and False otherwise:

balance = 100
PIN = "4567"

print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Check PIN")
print("5. Change PIN")
choice = int(input("Choose an option: "))
if choice == 1 :
    print(f'Account balance is: {balance}')
elif choice == 2:
    amount = int(input("Enter the amount you want to deposit: "))
    balance += amount
    print(f'Account balance is: {balance}')
elif choice == 3: 
    amount = int(input("Enter the amount you want to withdraw: "))
    balance -= amount
    print(f'Account balance is: {balance}')
elif choice == 4:
    print(f'Your PIN is: {PIN}')
elif choice == 5:
    new_PIN = (input("Please enter your new PIN: "))
    if (len(new_PIN) == 4 and new_PIN.isdigit()):
        PIN = new_PIN
        print(f'Your PIN has been set to new PIN: {new_PIN}')
    else:
        print ("PIN must contain exactly 4 digits")