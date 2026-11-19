#The data below represents monthly expenses divided into categories and weeks. Write a program that calculates and prints:

#total expenses for each category
#total expenses for each week
#total expenses for a month
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
total_food = 0 # zaczynamy od 0 
for week in monthly_expenses: # Pobieramy po kolei każdy tydzień.
    total_food += week[0] # Dodajemy pierwszą kwotę z tygodnia, czyli wydatek na jedzenie.

total_transport = 0
# Calculates expenses
# Use loop statements
for week in monthly_expenses:
    total_transport += week[1] # Dodajemy drugą kwotę z każdego tygodnia.

total_utilities = 0
# Calculates expenses
# Use loop statements
for week in monthly_expenses:
    total_utilities += week[2] # Dodajemy trzecią kwotę z każdego tygodnia.

week1 = 0 #zero na początek
for expense in monthly_expenses[0]: # Pobieramy po kolei trzy kwoty z pierwszego tygodnia. Pierwszy wiersz.
    week1 +=expense

week2 = 0
for expense in monthly_expenses[1]: # Pobieramy trzy kwoty z drugiego tygodnia. 2gi wiersz
    week2 +=expense

week3 = 0
for expense in monthly_expenses[2]: # Pobieramy trzy kwoty z trzeciego tygodnia. 3ci wiersz
    week3 +=expense

week4 = 0
for expense in monthly_expenses[3]:  # Pobieramy trzy kwoty z czwartego tygodnia. 4ty wiersz.
    week4 +=expense

total_month = week1 + week2 + week3 + week4


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food: {total_food}.')
print(f'Transport: {total_transport}.')
print(f'Utilities: {total_utilities}.')
print(f'Week 1: {week1}')
print(f'Week 2: {week2}')
print(f'Week 3: {week3}')
print(f'Week 4: {week4}')
print('---------------')
print(f'TOTAL: {total_month}.')