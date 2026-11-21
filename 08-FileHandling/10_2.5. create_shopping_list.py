#Write a program that allows you to create a shopping list. The program takes user input from the keyboard until #the user enters 0. Each value taken is saved to a text file 'shopping_list.txt'.

#Hint: Open the file in append mode using the 'a' (append) parameter in the open() function.

with open("shopping_list.txt", "a") as file: # Tryb "a" dopisuje tekst na końcu pliku. Jeśli pliku jeszcze nie ma, Python go tworzy.
    item = input("Product (0 to finish): ") # Pobieramy pierwszy produkt z klawiatury.
    while item != "0": # Powtarzamy pętlę, dopóki użytkownik nie wpisze "0".
        file.write(item + "\n") # Zapisujemy produkt i kończymy wiersz znakiem \n.
        item = input("Product (0 to finish): ") # Pobieramy kolejny produkt lub "0".
