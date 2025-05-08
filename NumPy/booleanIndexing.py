import numpy as np

# create an array of numbers
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# select only the even numbers from the array
even_numbers = numbers[numbers % 2 == 0]
print(even_numbers)

# Output: [ 2  4  6  8 10]