#Enter name: Anna
#Anna -- Polish female name

Name = str(input("Please enter name:"))
if Name[-1] == "a":
    print(f'{Name} is most likely female name.')
else:
    print(f'{Name} is most likely male name.')    
          