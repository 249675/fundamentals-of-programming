#Create a dictionary as in the example below. Do you know what type of value was used in each of the six key-value pairs?

#person = {
#   "name": "Marek",
#   "surname": "Banach",
#   "age": 25,
#   "hobby": ["swimming","excursions"],
#   "married": True,
#   "phone":{"landline":"123444321","mobile":"777888999"}
#}
#Then, create a program that:

#Displays name
#Displays hobby
#Displays the entire contents of the dictionary
#Changes surname to 'Nowak'
#Changes person's marriage status
#Adds gender: 'male'
#Adds a new hobby: 'bicycle'
#Adds work phone to existing phones: '313131444'
#Displays the entire contents of the dictionary (iterate over dictionary items)

person = {
    "name": "Marek",  # str
    "surname": "Banach",  # str
    "age": 25,  # int
    "hobby": ["swimming", "excursions"],  # list
    "married": True,  # bool
    "phone": {"landline": "123444321", "mobile": "777888999"},  # dict
}

print(person["name"])
print(person["hobby"])
print(person)

person["surname"] = "Nowak"
person["married"] = not person["married"]  # Odwracamy wartość logiczną.
person["gender"] = "male"
person["hobby"] = person["hobby"] + ["bicycle"]
person["phone"]["work"] = "313131444"  # Dodajemy wpis do słownika telefonów.

for key, value in person.items():
    print(f"{key}: {value}")
