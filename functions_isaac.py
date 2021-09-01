# single line comment

"""
Multiline comment
"""


def add(number1: float, number2: float) -> float:
    """
    Add two numbers.
    :param number1: first number
    :type number1: float
    :param number2: second number
    :type number2: float
    :return: the sum of two numbers
    :rtype: float
    """
    return number1 + number2

def add2(number1: int, number2: int) -> int:
    """
    Add two numbers.
    :param number1: first number
    :type number1: int
    :param number2: second number
    :type number2: int
    :return: the sum of two numbers
    :rtype: int
    """
    return number1 + number2

def list1(listA: list)-> list:
    for i in list:
        print(i)

def add_tuple(number1: tuple, number2: tuple) -> tuple:
    """
    Add two tuples.
    :param number1: first tuple
    :type number1: tuple
    :param number2: second tuple
    :type number2: tuple
    :return: the sum of two tuples
    :rtype: tuple
    """
    number1 += number2
    return number1