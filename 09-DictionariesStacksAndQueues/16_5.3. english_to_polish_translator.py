# Write a program to translate words from English to Polish. The user enters a word in English from the keyboard. 
# The program displays the translation of the word or information that the translation is unavailable.

translations = {"computer": "komputer", "mouse": "myszka",
                "keyboard": "klawiatura", "printer": "drukarka"}

word = input("English word: ").strip().lower() # strip() usuwa białe znaki z początku i końca, np. spacje i tabulatory. # lower() zamienia wielkie litery na małe.
if word in translations:  # Słowo angielskie jest kluczem słownika.
    print("Polish translation:", translations[word])
else:
    print("Translation unavailable.")

#Do print() trafiają dwa teksty: etykieta "Polish translation:" oraz pobrana ze słownika "myszka".