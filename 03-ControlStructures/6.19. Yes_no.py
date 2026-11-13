#Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. Write a program that prints a survey consisting of three questions. Save the answers to logical type variables. Then view the survey result. Sample result:

#SURVEY Are you interested in computer science? (y/n): y
#Do you like playing computer games? (y/n): n
#Do you have an Instagram account? (y/n): y

#SURVEY RESULTS Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

science = input("Are you interested in computer science?(y/n): ")  == 'y' #dla y robi True
games = input("Do you like playing computer games? (y/n): ") == 'y'
instagram = input("Do you have an Instagram account? (y/n): ") == 'y'

print(f'SURVEY RESULTS Interested in computer science: {'Yes' if science else 'No'}')
print(f'Playing computer games: {'Yes' if games else 'No'}')
print(f'Has an Instagram account: {'Yes' if instagram else 'No'}')
