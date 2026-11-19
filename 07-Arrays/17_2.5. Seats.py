#The data below represents a cinema's seating arrangement. Write a program that:

#calculates how many seats are available
#calculates how many seats are booked
#informs what the status of a seat is in a given row and given place (available or booked)
# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
    return len(seats) * len(seats[0])  # Mnożymy liczbę rzędów przez liczbę miejsc w pierwszym rzędzie.


def seats_available(seats):
   available = 0
   for row in seats: # Pobieramy po kolei każdy rząd.
        for seat in row: # Sprawdzamy po kolei każde miejsce w bieżącym rzędzie.
            if seat == "A":
                available += 1 
   return available

def seats_booked(seats):
    booked = 0
    for row in seats:  # Pobieramy po kolei każdy rząd.
        for seat in row: # Sprawdzamy każde miejsce w bieżącym rzędzie.
            if seat == "B":
                booked += 1 
    return booked

def seat_status(seats, row, place):
    selected_row = seats[row-1] # Pobieramy rząd. Numeracja zaczyna się od 1, a indeksy od 0.
    selected_seat = selected_row[place-1] # Z wybranego rzędu pobieramy miejsce według tej samej zasady.
    if selected_seat == "A": 
        return "Available"
    else:
        return "Booked"

print('CINEMA INFORMATION TABLE')
print(f'Total seats: {seats_total(cinema_seats)}.')
print(f'Seats available: {seats_available(cinema_seats)}.')
print(f'Seats booked: {seats_booked(cinema_seats)}.')
print(f'Seat in row 1, place 1: {seat_status(cinema_seats, 1,1)}.')
print(f'Seat in row 5, place 5: {seat_status(cinema_seats, 5,5)}.')
print(f'Seat in row 3, place 5: {seat_status(cinema_seats, 3,5)}.')