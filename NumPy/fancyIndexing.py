# Fancy Indexing

# In NumPy, we can also use fancy indexing to select and modify elements of an array based on a list of indices. For example,

import numpy as np


# create a numpy array

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])


# select elements at index 1, 2, 5, 7

elements = numbers[[1, 2, 5, 7]]

print(elements)


# Output: [2 3 6 8]