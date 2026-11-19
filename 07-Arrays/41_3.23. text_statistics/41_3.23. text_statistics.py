# A variable contains the text "An apple a day keeps the doctor away".
# Create a module MyText with functions that return the number of words,
# the words ordered from longest to shortest, and the words in alphabetical
# order. Then call the functions and print the results.

from MyText import count_words, words_alphabetically, words_by_length


text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", count_words(text))
print("Words from the longest:", ",".join(words_by_length(text)))
print("Words ordered alphabetically:", ",".join(words_alphabetically(text)))