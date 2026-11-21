#JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for 
# machines to parse and generate. It is often used to transmit data between a server and a web application, as well as to store structured data.

#Note the key characteristics of JSON:

#Readability: JSON is text-based, so it can be easily read by humans.
#Simplicity: It is built on key-value pairs.
#Language Agnostic: Although it derives from JavaScript, JSON is supported by many programming languages like Python, Java, PHP, C#, and more.


import json # Importujemy moduł do zamiany danych Pythona na JSON i z powrotem.

# Tworzymy słownik z imieniem, listą umiejętności i informacją, czy osoba jest aktywna.

data = {"name": "Anna", "skills": ["Python", "SQL"], "active": True}

# Zamieniamy słownik na tekst w formacie JSON.
# ensure_ascii=False pozwala zachować polskie znaki w czytelnej postaci.
# indent=4 ustawia wcięcia po 4 spacje.
json_text = json.dumps(data, ensure_ascii=False, indent=4)
print(json_text)

restored = json.loads(json_text) # Zamieniamy tekst JSON z powrotem na słownik.
print()
print("Name:", restored["name"]) # Pobieramy spod klucza "name" wartość "Anna" i ją wypisujemy.
print("Skills:", restored["skills"])
print("Active:", restored["active"])


# dumps() daje tekst
# loads() odczytuje tekst. 
# przechodzisz od słownika data do tekstu json_text, a z niego z powrotem do słownika restored.