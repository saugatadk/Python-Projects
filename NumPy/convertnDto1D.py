#  if we just pass -1 as the shape argument, the reshape() function reshapes the original array into a one-dimensional array.

import numpy as np
array1 = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
# flatten the array using -1 as second argument
reshaped_array = np.reshape(array1, -1)
print(reshaped_array)
# Output

# [0 1 2 3 4 5 6 7]