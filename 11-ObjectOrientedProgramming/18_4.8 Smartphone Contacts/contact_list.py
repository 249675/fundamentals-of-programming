class Contact_List:
    def __init__(self):
        self.contacts = []  # Lista przechowuje całe obiekty Contact.

    def add_contact(self, contact):
        self.contacts.append(contact)

    def show_contacts(self):
        # Z każdego obiektu odczytujemy trzy atrybuty.
        for contact in self.contacts:
            print(f"{contact.name:<14} {contact.email:<20} {contact.telephone}")
