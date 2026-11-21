#Create a dictionary describing your mobile phone. Use 6 key-value pairs of data. Then, using for loop, display the contents of the dictionary. To read a key and value, use the items() method. Sample result:

mobile = {"OS": "Android", 
          "Brand": "Samsung", 
          "Model": "Galaxy S24",
          "Storage GB": 128, 
          "RAM GB": 8, 
          "5G": True}

for key, value in mobile.items():   # W każdym obrocie pobieramy klucz i jego wartość.
    print(f"{key}: {value}")
