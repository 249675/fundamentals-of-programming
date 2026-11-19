# Functions for counting and sorting the words in a text.

def count_words(text):
    return len(text.split())


def words_by_length(text):
    return sorted(text.split(), key=len, reverse=True)


def words_alphabetically(text):
    return sorted(text.split(), key=str.lower)