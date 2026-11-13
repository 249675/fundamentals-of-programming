###
# Calculates the sum of even numbers in the range <1,10>
#
sum = 0

for i in range(1,11):
    if not i%2 == 0: #negujemy, warunek prawdziwy dla parzystych
        continue #pomijamy, kontynuujemy
    sum += i #sumujemy same parzyste

print(f'Sum of even numbers in the range <1,10> is {sum}')