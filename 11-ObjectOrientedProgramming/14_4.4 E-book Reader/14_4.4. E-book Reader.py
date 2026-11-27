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

from ebook import EBook


def main():
    # Numer strony zaczyna się od 1, a książka jest zamknięta.
    book = EBook("The Hobbit", "J. R. R. Tolkien", 310)
    book.open()
    book.show_status()

    # Czytamy trzy kolejne strony i wracamy o jedną.
    for _ in range(3):
        book.next_page()
    book.previous_page()
    book.show_status()

    book.close()
    book.next_page()
    book.previous_page()


if __name__ == "__main__":
    main()
