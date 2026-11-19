#Very often, there is a need to organize the data contained in the array. Organized data allows for faster retrieval, analysis, and presentation of information. There are many sorting algorithms that organize data in the array. One of the simplest is bubble sort, which organizes data in ascending or descending order.

#Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list or array, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until no more swaps are needed, which means the list is sorted.

#Here is the bubble sort algorithm expressed in pseudocode, a universal notation that is independent of the programming language:

#procedure bubbleSort(arr):
#   n = length(arr)
#   for i = 0 to n-1:
#      for j = 0 to n-i-2:
#         if arr[j] > arr[j+1]:
#               swap arr[j] and arr[j+1]
#   return arr

def bubble_sort(arr):
    n = len(arr) # Zapisujemy liczbę elementów listy.
    for i in range (n): # Wykonujemy kolejne przebiegi sortowania.
        for j in range (n-i-1):  # Porównujemy sąsiadów, pomijając już ustawione elementy na końcu.
            if arr[j] > arr[j+1]: # Jeśli lewy element jest większy od prawego, zamieniamy je miejscami.
                temp = arr[j] # Zapamiętujemy lewy element, zanim go nadpiszemy.
                arr[j] = arr[j+1]  # Przenosimy prawy element na lewo.
                arr[j+1] = temp # Wstawiamy zapamiętany element na prawo
    return arr # Zwracamy posortowaną listę.


arr = [5,2,4]

print (arr)
print(bubble_sort(arr))