import numpy as np

# create an array of numbers
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# select only the even numbers from the array
even_numbers = numbers[numbers % 2 == 0]
print(even_numbers)

# Output: [ 2  4  6  8 10]


print("Enter numbers to print only the odd numbers:")
numbers_list = list(map(int,input().split())) #converts "10 20 30".split() -> ["10", "20", "30"] -> map object with integer values -> list
# create an array of numbers
numbers = np.array(numbers_list)

# select only the odd numbers from the array
odd_numbers = numbers[numbers % 2 != 0]

# print the resulting value
print(odd_numbers)
