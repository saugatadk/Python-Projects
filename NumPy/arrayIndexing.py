import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12, 14])

# access every third element of the array
sliced_numbers = numbers[0:6:3] # last element not considered
print(sliced_numbers)
sliced_numbers = numbers[::3] # last element is also considered if it satisfies condition
print(sliced_numbers)
sliced_numbers = numbers[::-1] # also reverses entire list, creates a slice that starts from the last element and goes towards the first element of the array numbers. 
print(sliced_numbers)
sliced_numbers = numbers[-1::-1] # slice the array in reverse order using negative indexing and negative step value 
print(sliced_numbers)


