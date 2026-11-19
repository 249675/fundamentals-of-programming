# Write a program that checks whether the first array is a subset
# of the second one, meaning all elements of the first array appear
# in the second array.

array1 = [2, 5, 7]
array2 = [1, 2, 4, 5, 7, 9]
is_subset = True

for number in array1:
    if number not in array2:
        is_subset = False
        break

print("First array:", *array1)
print("Second array:", *array2)
print("Is the first array a subset of the second?", is_subset)
