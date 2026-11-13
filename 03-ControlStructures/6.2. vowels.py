###
# Counts vowels in the text
#
text = "This is a sample text." #tekst
vowels = "aeiouAEIOU" #samogłoski
vowel_count = 0 #lecimy od 0

# Count vowels in the text
i = 0

while i < len(text): #powtarza pętlę, dopóki indeks i jest mniejszy od długości tekstu
    if text[i] in vowels: # sprawdza czy aktualny znak jest samogloska
        vowel_count += 1 # dodaje samogloski, sumuje
    i += 1 #przechodzi do następnego znaku tekstu

print(f"The number of vowels in the text is: {vowel_count}")

