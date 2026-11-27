#Create a class that represents pieces of music. Define a class constructor that allows you to set the initial values of the 
# music piece (artist, track title, album, year) when the object is created. Complete the class with the __str__ method 
# returning the song data as a string, in the format as below (4 lines). Then, create two objects that represent two pieces 
# of music and print their data. Sample result:

class Song:
    def __init__(self, performer, title, album, year):
        # Argumenty konstruktora stają się atrybutami utworu.
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        # Każde \n rozpoczyna nowy wiersz w zwracanym tekście.
        return (
            f"Performer: {self.performer}\n"
            f"Title:     {self.title}\n"
            f"Album:     {self.album}\n"
            f"Year:      {self.year}"
        )


song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

# print sam wywołuje __str__ dla podanego obiektu.
print(song1)
print()
print(song2)
