#E-book is a digital book that can be read using a computer or other electronic devices (electronic book readers). 
# Write a program in which define a class that describes states and behaviors of an e-book. 
# Each book has a title, author, number of pages and the current page number that is currently being read.
#  It is possible to open a book - then we can read it. If a book is open, it is possible to go to the next or previous page.

#Place the class describing e-books in a separate file/module. In the main program file, try using the e-book:

#Create a book with a title, author, number of pages (check how to set the initial values of the fields at the time 
# of creating the object using the __init__ method / constructor and passing the initial values as arguments to the method call)
#Open a book
#Display a book status (title, author, page numbers, current page no)
#Read a few pages
#Display a book status
##Close a book
#Read a few pages (it should not be possible to perform this operation - display the message that the book is closed).

class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def next_page(self):  # Metoda przechodząca do następnej strony.
        if not self.is_open:  # Sprawdzamy, czy książka jest zamknięta.
            print("The book is closed.")  # Wyświetlamy informację o zamkniętej książce.
        elif self.current_page < self.pages:  # Sprawdzamy, czy aktualna strona jest mniejsza od liczby wszystkich stron.
            self.current_page += 1  # Zwiększamy numer aktualnej strony o 1.

    def previous_page(self):  # Metoda przechodząca do poprzedniej strony.
        if not self.is_open:  # Sprawdzamy, czy książka jest zamknięta.
            print("The book is closed.")  # Wyświetlamy informację o zamkniętej książce.
        elif self.current_page > 1:  # Sprawdzamy, czy aktualna strona jest większa od 1.
            self.current_page -= 1  # Zmniejszamy numer aktualnej strony o 1.

    def show_status(self):  # Metoda wyświetlająca aktualne informacje o książce.
        print(f"{self.title} by {self.author}")  # Wyświetlamy tytuł książki i jej autora.
        print(f"Page {self.current_page} of {self.pages}")  # Wyświetlamy aktualną stronę oraz liczbę wszystkich stron.
