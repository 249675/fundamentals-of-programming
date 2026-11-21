#Write a program that writes a list of the Seven Wonders of the World to a text file, in alphabetical order, with each name on a separate line. Then, open the created file in the editor and check if its contents match the task.

seven_wonders = [
    "Great Wall of China", "Petra", "Christ the Redeemer", "Machu Picchu",
    "Chichen Itza", "Roman Colosseum", "Taj Mahal",
]

with open("seven_wonders.txt", "w") as file:
    for wonder in sorted(seven_wonders):
        file.write(wonder + "\n")  # Każdy cud zapisujemy w osobnym wierszu.
