# Functions for counting and sorting the words in a text.

def count_words(text):
    return len(text.split()) # Dzielimy tekst na słowa i liczymy elementy otrzymanej listy.


def words_by_length(text):
    return sorted(text.split(), key=len, reverse=True) # Sortujemy słowa od najdłuższego do najkrótszego.


def words_alphabetically(text):
    return sorted(text.split(), key=str.lower)  # Przy sortowaniu porównujemy słowa tak, jakby były zapisane małymi literami.