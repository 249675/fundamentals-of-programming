Price = input("Enter the price: ")
Price = float(Price)

Discount = input("Enter the discount in %: ")
Discount = float(Discount)

print(f'Price after discount: {Price - (Price * Discount / 100):.2f}')
print(f'Reducion amount: {Price * Discount / 100:.2f}')







