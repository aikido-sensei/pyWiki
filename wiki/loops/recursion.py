"""
5! = 5 * 4 * 3 * 2 * 1
"""


#from _typeshed import SupportsKeysAndGetItem


def factorial(n: int) -> int:
    if n < 0:
        raise AttributeError(f"Cannot compute factorial of a negative number - {n}")

    # Iterative method - Using loops
    # result = 1
    # for number in range(1, n + 1):
    #     result = result * number
    # return result

    # Recursion/Recursive method - Be careful with overflowing the stack.
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Tail recursion
def factorial_using_tail_recursion(n: int, accumulator: int = 1):
    if n < 0:
        raise AttributeError(f"Cannot compute factorial of a negative number - {n}")
    if n <= 1:
        return accumulator
    return factorial_using_tail_recursion(n - 1, n * accumulator)


""" 
    TODO: Try the above approaches for finding:
     1. The sum on n numbers.
     2. The value of pi - https://en.wikipedia.org/wiki/Leibniz_formula_for_π.
"""

#Sum of n numbers
def sum_on_n_numbers_recursion(n: int, accumulator: int = 0):
    if n <= 0:
        raise AttributeError("Cannot compute the sum of less than 1 number.")
    
    if n == 1:
        return accumulator + 1

    return sum_on_n_numbers_recursion(n-1, n + accumulator)

print(sum_on_n_numbers_recursion(5))

#Approximation of pi's value
def value_of_pi_using_recursion(n : int, accumulator: int = 0):
    if n < 0:
        raise AttributeError("Cannot approximate the value of pi with this number.")
    
    if n == 0:
        accumulator +=1
        return accumulator*4

    return value_of_pi_using_recursion(n-1, ((-1) ** n /(2*n+1)) + accumulator) 


print(value_of_pi_using_recursion(950))