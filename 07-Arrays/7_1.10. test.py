#The array contains the student's test results. A value of True indicates that the student answered the question correctly, while a value of False indicates an incorrect answer. Write a program that prints information about the test results:

#Number of questions:
#Number of correct answers:
#Number of incorrect answers:
#Percentage of correct answers:
###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results) # liczy wszystkie odpowiedzi w array'u

# calculates the number of correct answers
correct_answers = 0 # Zaczynamy liczenie poprawnych odpowiedzi od zera.
for answer in test_results:  # Przechodzimy po kolei przez wszystkie odpowiedzi.
   if answer == True: 
      correct_answers += 1

# calculates the number of incorrect answers
incorrect_answers = 0 # Zaczynamy liczenie błędnych odpowiedzi od zera.
for answer in test_results:# Ponownie przechodzimy przez wszystkie odpowiedzi.
   if answer == False:
      incorrect_answers += 1

# calculates the percentage of correct answers
percentage = correct_answers / question_number *100  # Dzielimy liczbę poprawnych odpowiedzi przez liczbę pytań i mnożymy przez 100.

print('TEST STATISTICS')
print('===============')
print(f'Number of questions: {question_number}')
print(f'Number of correct answers: {correct_answers}')
print(f'Number of incorrect answers: {incorrect_answers}')
print(f'Percentage of correct answers: {percentage:.2f} %')