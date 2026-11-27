#A dictionary contains course names along with the number of hours. Write a program that calculates and prints the total number of hours.
#  Sample results:

winter_semester = {"math": 60, "programming": 30, "history": 15}

total_hours = 0
for hours in winter_semester.values():  # Pobieramy same liczby godzin. Values wskazuje int dlatego hours zlicza poprawnie
    total_hours += hours
print("The total number of hours in the winter semester is", total_hours)
