#The file pets.txt contains humorous text about animals. Write a program that prints the text and counts the #number of words in the text.

#To calculate the number of words in a line, use the split() method, which splits a string into a list where each #word is a list item. Then read the length of this list. Use the len() function. Finally, sum the number of words #in each line.
#https://www.w3schools.com/python/ref_string_split.asp

with open("pets.txt") as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    print(line) # Wyświetlamy bieżący wiersz z pets.txt.
    total += len(line.split())  # Doliczamy słowa z bieżącego wiersza. # Dzielimy wiersz na słowa, liczymy je i doliczamy do sumy.

print("Number of words:", total)
