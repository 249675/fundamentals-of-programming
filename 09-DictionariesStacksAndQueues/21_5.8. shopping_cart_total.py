#Write a program to calculate the total cost of a shopping cart using a price list.

prices = {"milk": 1.49, "butter": 2.09, "juice": 1.19, "bread": 1.99}
cart = {"juice": 3, "bread": 1, "milk": 2}

total = 0
for product, quantity in cart.items():
    total += prices[product] * quantity  # Mnożymy cenę jednostkową przez liczbę sztuk.

print(f"Total cost: {total:.2f}")
