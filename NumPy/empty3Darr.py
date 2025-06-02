import numpy as np

# create an empty 3-D array with 2 "slices" of 2 rows and 2 columns each
np_array = np.empty((2, 3, 4)) #axis0 = 2, axis1 = 3, axis2 = 4

print(np_array)

# Create a 5D array with shape (2, 3, 4, 5, 6)
# array_5d = np.zeros((2, 3, 4, 5, 6))

# print(array_5d)

# create 2x2 array all filled with the value 5
numpy_array = np.full((2, 2), 5)

print("Array:", numpy_array)