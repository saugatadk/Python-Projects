import numpy as np
from numpy.ma import MaskedArray

# create a NumPy array
array1 = np.array([1, 2, 3, 4, 5])

# create a mask based on a condition
mask = array1 > 2

# create a MaskedArray using the original array and the mask
masked_arr = MaskedArray(array1, mask)

print("Original array:")
print(array1)
print("Masked array:")
print(masked_arr)

# In the masked array, the elements that correspond to True values are replaced with -- to indicate that they are masked or invalid while the element that correspond to the False values are preserved.