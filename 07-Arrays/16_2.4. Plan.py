#The data below contains weekly meal plan. Write a program that prints the weekly meal plan along with the day name as in the example below.

#WEEKLY MEAL PLAN
#(Breakfast, Lunch, Dinner)
#==========================
#Monday: Oatmeal, Grilled Checken Salad, Spaghetti
#Tuesday: ...
#Wednesday: ...
#...
#...
#...
#...
# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]  # Odejmujemy 1, bo pierwszy dzień ma na liście indeks 0.

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number): # Przyjmujemy plan posiłków i numer dnia.
    return ", ".join(meal_plan[day_number-1])  # Pobieramy posiłki z danego dnia i łączymy je w tekst, wstawiając między nimi przecinek i spację. Połącz posiłki z wybranego dnia w jeden tekst, wstawiając ", " między nimi, i zwróć ten tekst.”

# Prints weekly meal plan
for current_day in range(1,8): # Przechodzimy przez dni od 1 do 7. Liczba 8 jest pomijana.
    print(f'{weekday(current_day)}: {day_meal_plan(meal_plan, current_day)}')  # Wyświetlamy nazwę dnia i przypisane mu posiłki.


