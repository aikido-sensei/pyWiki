
from __future__ import annotations


class EvenNumberIterator:

    def __init__(self, numbers: list) -> None:
        self.numbers = numbers

    def __iter__(self) -> EvenNumberIterator:
        self.index = 0
        return self

    def __next__(self) -> int:
        while self.index < len(self.numbers) - 1 and self.numbers[self.index] % 2 != 0:
            self.index += 1
            pass

        if self.index == len(self.numbers):
            raise StopIteration

        self.index += 1
        return self.numbers[self.index - 1]


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers_iterator = EvenNumberIterator(numbers_list)
for even_number in even_numbers_iterator:
    print(even_number)

# TODO: Develop iterators to iterate a given list in the ascending or descending order.

class AscendingOrDescendingIterator:

    def __init__(self, numbers, isAscending) -> None:
        self.numbers = numbers
        self.isAscending = isAscending
        self.temp = 0

    def __iter__(self) -> AscendingOrDescendingIterator:
            self.index = 0
            return self

    def __next__(self) -> int:

        while (0 < self.index < len(self.numbers)) and (self.numbers[self.index] < self.temp if self.isAscending == True else self.numbers[self.index] > self.temp) :
            self.index += 1
            pass

        if self.index == len(self.numbers):
            raise StopIteration

        self.temp = self.numbers[self.index]
        self.index += 1
        return self.numbers[self.index - 1]

numbers_list = [1, 2, 3, 4, 2, 6, 7, 5]
ascending_numbers_iterator = AscendingOrDescendingIterator(numbers_list, False)
for ascending_number in ascending_numbers_iterator:
    print(ascending_number)

