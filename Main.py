import math

# first_number = int(input('First number'))
#
# second_number = int(input('Second number'))
#
# third_number = int(input('Third number'))
#
# if first_number == second_number == third_number:
#     result_sum = first_number + second_number + third_number
#     result = result_sum *3
#
#     print(result)
#
# else:
#     result = first_number + second_number + third_number
#
#     print(result)

# Task 2 - get the difference

# Create two inputs

# Check if first number is greater than the second, calculate double difference

# Otherwise calculate the absolute difference between numbers

# first_number = int(input('First number'))
#
# second_number = int(input('Second number'))
#
# if first_number > second_number:
#     result = (first_number - second_number)*2
#     print(result)
#
# else:
#     result = abs(first_number - second_number)
#     print(result)

# Task 3 - odd or even number

# Create an input for odd
# Create an input for even

# number = int(input('Enter a number'))
# if (number % 2) == 0:
#     print('{0} is Even'.format(number))
#
# else:
#     print('{0} is odd'.format(number))

# Task 4-circle area

# from math import pi
#
#
# r = float(input('input the radius of the circle:'))
# print('The area of the circle with radius '+ str(r) + ' is: '+str(pi*r**2))

# Task 5- guess a number

# import random
#
# target_number, guessed_number = random.randint(1, 10), 0
# while target_number != guessed_number:
#     guessed_number = int(input('Guess a number between 1 and 10 until you get it right:'))
#     print('Well guessed!')

# Task 6- Celsius to Fahrenheit conversion
#
# temp = input('Input the temperature you would like to convert?')
# degree = int(temp[:-1])
# i_convention = temp[-1]
#
# if i_convention.upper() == 'C':
#     result = int(round((9 * degree) /5 + 32))
#     o_convention = 'Fahrenheit'
# elif i_convention.upper() == 'F':
#     result = int(round((degree-32)*5/9))
#     o_convention = 'Celsius'
#
# else:
#     print('Input proper convention.')
#     quit()
#     print('The Temperature in', o_convention, 'is', result,'degrees,')

# Task 7-pattern

# n = 5
#
# for i in range(n):
#     for j in range(i):
#         print('* ', end="")
#         print('')
#     for i in range(n, 0, -1):
#         for j in range(i):
#             print('* ', end="")
#             print('')

# Task 8-Fibonacci series

# x, y = 0, 1
#
# while y < 50:
#     print(y)
#     x, y = y, x+y