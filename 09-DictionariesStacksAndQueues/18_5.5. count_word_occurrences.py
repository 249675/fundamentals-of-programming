#Write a program that counts how many times each word appears in a paragraph.
#Hint: Check the dictionary to see if the next word appears in it. If so, increase the number of times the word appears by 1. You can easily split a paragraph into individual words using the split() method. Search the Internet for how to use it.

paragraph = "cat dog mouse cat rat cat mouse"
counts = {}

for word in paragraph.split():  # split() dzieli tekst według białych znaków.
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1  # Pierwsze wystąpienie danego słowa.

for word, count in counts.items():
    print(f"{word}: {count}")
