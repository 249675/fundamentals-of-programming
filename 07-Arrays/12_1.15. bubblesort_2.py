#Define a function that sorts an array of numbers using the bubble sort algorithm. Use the information in the pseudocode provided earlier. Then, write a program that sorts the following collections of data:

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
###
# Bubble sort
#
def bubble_sort(arr):
    n = len(arr) # Zapisujemy liczbę elementów listy.
    for i in range (n): # Wykonujemy kolejne przebiegi sortowania.
        for j in range (n-i-1): # Porównujemy sąsiadów, pomijając elementy już ustawione na końcu.
            if arr[j] > arr[j+1]:  # Zamieniamy elementy, gdy lewy jest większy od prawego.
                temp = arr[j] # Zapamiętujemy wartość lewego elementu.
                arr[j] = arr[j+1] # Przenosimy prawy element na lewo.
                arr[j+1] = temp # Wstawiamy zapamiętaną wartość na prawo.
    return arr # Zwracamy posortowaną listę.




print(car_fuel_consumption) 
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)  

print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions) 
print(sorted_bank_transactions)