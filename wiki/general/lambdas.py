square_function = lambda number: number * number
sum_function = lambda number1, number2: number1 + number2
is_even_function = lambda number: number % 2 == 0

print(sum_function(3, 10))

"""
TODO: Try to define the functions as a part of the TODOs in the recursion.py file as lambda functions.
1. The sum on n numbers.
2. The value of pi - https://en.wikipedia.org/wiki/Leibniz_formula_for_π.
"""

#1
sum_of_n_numbers = lambda n, accumulator = 0: accumulator + 1 if n == 1 else sum_of_n_numbers(n-1, n + accumulator)

print(sum_of_n_numbers(5))

#2
value_of_pi = lambda n, accumulator = 0: (accumulator + 1)*4 if n == 0 else value_of_pi(n-1, ((-1) ** n /(2*n+1)) + accumulator) 

print(value_of_pi(950))