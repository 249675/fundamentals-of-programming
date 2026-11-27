#A class contained in the socialmedia.py models a social media profile, allowing users to add posts and display their timeline. 
# Add a display_timeline(self) method to the class that prints the user's name along with a list of posts. Number the list items. 
# Then write a program that creates a user 'johndoe'. Add the following posts. Print the user's name and posts.

#Hello, world!
#Had a great day at the park!
#What's up, Natalie? How are you?

class SocialMediaProfile:  # Klasa opisuje profil użytkownika w mediach społecznościowych.
    def __init__(self, username):  # Przy tworzeniu profilu self oznacza nowy profil, a username to podana nazwa użytkownika.
        self.username = username  # Zapisujemy podaną nazwę w profilu, żeby inne metody mogły jej użyć.
        self.posts = []  # Każdy nowy profil dostaje własną, pustą listę postów.

    def add_post(self, content):  # Metoda przyjmuje treść nowego posta w parametrze content.
        self.posts.append(content)  # append() dodaje treść posta na końcu listy tego profilu.
        print(f"{self.username} added a new post: {content}")  # Wyświetlamy, kto dodał post i co napisał.

    def display_timeline(self):  # Metoda wyświetla nazwę użytkownika i jego ponumerowane posty.
        print(self.username)  # Wyświetlamy nazwę użytkownika jako nagłówek.
        number = 1  # Zaczynamy numerowanie od 1. Przy każdym wywołaniu metody licznik startuje od nowa.
        for post in self.posts:  # W każdym obiegu pętli post oznacza treść kolejnego wpisu z listy.
            print(f"{number}. {post}")  # Wyświetlamy numer, kropkę i treść wpisu, np. „1. Hello, world!”.
            number += 1  # To samo co number = number + 1. Zwiększamy numer dla następnego wpisu.


profile = SocialMediaProfile("johndoe")  # Tworzymy profil. Tekst "johndoe" trafia do parametru username w __init__.
profile.add_post("Hello, world!")  # self to profile, a content to "Hello, world!". Metoda zapisuje post i wypisuje komunikat.
profile.add_post("Had a great day at the park!")  # Dodajemy drugi wpis do listy tego samego profilu.
profile.add_post("What's up, Natalie? How are you?")  # Dodajemy trzeci wpis. Lista zawiera teraz trzy posty.
print()  # Wyświetlamy pustą linię między komunikatami o dodaniu postów a listą wpisów.
profile.display_timeline()  # Wyświetlamy johndoe, a pod spodem trzy posty w kolejności dodania, z numerami 1, 2 i 3.