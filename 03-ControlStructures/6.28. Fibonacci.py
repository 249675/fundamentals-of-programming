#Write a program that prints the first twenty words of the Fibonacci sequence. The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. Sample result:

a = 0
b = 1
for i in range(0,20):
    print (a, end=' ') # wypisuje a i spację, bez przechodzenia do nowej linii
    c = a + b # oblicza kolejną liczbę ciągu i zapisuje ją w c
    a = b # przesuwa a na wartość b
    b = c # przesuwa b na obliczoną kolejną liczbę