#Write a program that copies the contents of the file 'healthy_lifestyle.txt' to the file copy_healthy_lifestyle.txt'.

with open("healthy_lifestyle.txt", newline="") as source:
    content = source.read() # źródło

with open("copy_healthy_lifestyle.txt", "w", newline="") as target:
    target.write(content)  # Przenosimy cały odczytany tekst do nowego pliku. #target
