#Here's a program that writes data containing the title of a movie, its director, and the lead actor to a text #file. Copy the program to the movie.py file, then run the program. Finally, open the created text file in an #editor and check its contents.

#To write data to a file, you need to open it with the 'w' (write) parameter. The write() method writes one line #of data to the file. Note the '\n' character. It means to move the cursor to the next line. If you don't add it, #all subsequent data will be placed on one line.

movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"
file_name = "movie_details.txt"

with open(file_name, "w") as file: # Tryb "w" tworzy plik lub nadpisuje jego zawartość. 
    # Każdy zapis kończymy znakiem nowego wiersza.
    file.write(f"Movie Title: {movie_title}\n") # Zapisujemy tytuł. \n kończy wiersz.
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

# Po wyjściu z bloku with Python automatycznie zamyka plik.
print(f"Movie details have been written to {file_name}.")
