#The file email.txt contains a raw email. Write a program that uses regular expressions to fetch and print:

#sender email address
#recipient email address
#email subject
#email body
#For each of the above commands, define a separate function (see below) that returns the value read from the email. Place the functions in a separate module called emails.

#email_sender()
#email_recipient()
#email_subject()
#email_body()

from emails import email_sender, email_recipient, email_subject, email_body #importuje funkcje

with open("email.txt") as file: # Otwieramy plik txt z wiadomością do odczytu.
    message = file.read() # Wczytujemy całą wiadomość jako jeden tekst, razem z końcami wierszy.

print("Sender:", email_sender(message)) 
print("Recipient:", email_recipient(message))
print("Subject:", email_subject(message))
print("Body:")
print(email_body(message))
