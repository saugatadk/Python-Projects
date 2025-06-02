squares = [n ** 2 for n in range(5)]
print(squares)# Output: [0, 1, 4, 9, 16]
# This is a list comprehension that generates a list of squares of numbers from 0 to 4.
# It is a concise way to create lists in Python.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
# This is a list comprehension that filters out even numbers from the list `numbers`.

pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# This is a nested list comprehension that generates pairs of numbers from 0 to 2.