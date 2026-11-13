###
# Sums numbers entered by user
#
total_sum = 0
count = 0       

while True: # ciągle aż przerwiemy poniżej break 
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number #total_sum ciągle dodaje wpisywane nry
    count += 1 #ciągle liczymy kolejne wpisy, 1,2,3, itd potrzebne do sredniej

print(f"The total sum of the numbers is: {total_sum}")
print(f"The average of the numbers is: {total_sum / count}")