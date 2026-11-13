###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_code = ord(char) # read the character's code (use ord()) #zamieniamy litery na liczby ktore sa do nich przypisane

    new_code = char_code + 1 # add one to the character's code #dodajemy 1 do tej liczby ktora otrzymam

    encrypted_char = chr(new_code) # replace new character code with its corresponding character (use chr()) #rozkodowujemy nowe liczby, tzn. przypisujemy do nich litery
    
    encrypted_text = encrypted_text + encrypted_char # add encrypted character to encrypted text
    ...

print(plain_text) 
print(encrypted_text)