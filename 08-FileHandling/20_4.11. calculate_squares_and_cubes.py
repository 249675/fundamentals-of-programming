#Write a program that calculates, prints, and saves to a text file integers from 1 to 100 and their second and third powers. Sample result:

#1,1,1
#2,4,8
#3,9,27
#...
#...

with open("powers.txt", "w") as file:
    for number in range(1, 101):
        line = f"{number},{number ** 2},{number ** 3}"
        print(line)
        file.write(line + "\n")  # Ten sam wiersz zapisujemy do pliku. # \n nowy wiersz
