#Write a program that prints a popular computer games, each game name on a separate line. Use the while statement. Additionally, number the list (print the next number before each list item) and sort the list alphabetically (use one of a Python built-in functions for sorting)

computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games = sorted(computer_games) # Sortujemy tytuły i zapisujemy posortowaną listę pod tą samą nazwą.
i = 0 # Zaczynamy od indeksu 0, czyli od pierwszej gry.
while i < len(computer_games): # wykonuj pętlę, dopóki i jest mniejsze od liczby gier na liście.
    print(f'{i+1}. {computer_games[i]}') # Wyświetlamy numer pozycji i tytuł gry
    i += 1 # Zwiększamy indeks o 1, żeby przejść do następnej gry.