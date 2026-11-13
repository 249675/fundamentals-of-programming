#In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:

#Number of products purchased: 5
#Product price: 40
#Amount to pay: 170.00

number = 5 #number of products
price = 40 #product price

if number >= 2:
    disc_price = (2 * price) + (number - 2) * price * 0.75 #tylko to powyżej 2 sztuk z znizka 25%. Pierwsze dwie sztuki nromalna cena
    print(disc_price)
elif number <= 2:
    print(number * price)
