# An array contains a list of Polish names:
# Genowefa, Onufry, Celestyna, Alojzy, Pankracy.
# Create a program that prints the longest name.

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = names[0]

for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print("Names:", end=" ")  # Wyświetlamy etykietę i zostajemy w tym samym wierszu.
for name in names:
    print(name, end=" ")  # Wyświetlamy kolejne imię i spację.
print()  # Po wszystkich imionach przechodzimy do nowego wiersza.

print("Longest name:", longest_name)  # Wyświetlamy najdłuższe imię.