###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed

import keyboard_9_5_3 as keyboard # Importujemy pierwszy plik jako moduł o krótszej nazwie „keyboard”.

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ') # str
last_name = keyboard.input_string('Enter surname: ') # str
age = keyboard.input_integer('Enter age: ') #int
salary = keyboard.input_real('Enter salary: ') # float
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n)') #bool, sprawdza czy wpisze Y

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name:', last_name)
print('Age:', age)
if is_salary_hidden == False:
    print('Salary', salary)