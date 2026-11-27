#The Contact class contains the name, email and telephone fields enabling the description of a single contact on a smartphone.
#  The Contact_List class allows you to store contacts (store objects describing contacts in an array) and perform the following operations:

#Add a new contact
#Display the contact list
#Write a program consisting of 3 files (smartphone.py, contact.py, contact_list.py). In the mail program (smartphone.py), 
# create an object representing a contact list and add the following people data:

#John Brown     brown@onet.pl       555234000
#Anna May   	   am@o2.pl            232000199
#George Small   smallg@google.pl    222999100
#Paola Big      bigpaola@poczta.pl  100200300
#Then, display the contact list available on the smartphone.


from contact import Contact
from contact_list import Contact_List


def main():
    contacts = Contact_List()
    # Tworzymy osobny obiekt Contact dla każdej osoby i przekazujemy go do listy.
    contacts.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    contacts.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    contacts.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))
    contacts.show_contacts()


if __name__ == "__main__":
    main()
