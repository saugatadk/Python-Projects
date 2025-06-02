import numpy as np

array1 = np.array([0, 2, 4])
array2 = np.array([[6], [8], [4]])

# add arrays of different dimension
# size of array1 expands to match with array2
result = array1 + array2

print(result)
#output:
# [[ 6  8 10]
#  [ 8 10 12]
#  [ 4  6  8]]

# Broadcasting only works with compatible arrays. NumPy compares a set of array dimensions from right to left.

# Every set of dimensions must be compatible with the arrays to be broadcastable. While checking compatibility of two shapes of arrays, we compare their dimensions from right to left.

# A set of dimension lengths is compatible when

#     one of them has a length of 1 or
#     they are equal

# Let's see an example.

# array1 = shape(6, 7)
# array2 = shape(6, 1)

# Here, array1 and array2 are arrays with different dimensions (6,7) and (6,1) respectively.

# The right-most dimension of array1 is 7 and array2 is 1. Since, one of them has a length of 1, they are compatible.

# Now, let's move to the left dimensions. 6 and 6 are compatible since they are the same.

# As both sets of dimensions are compatible, the arrays are broadcastable.



# Non-Broadcastable Shapes

#     (6, 7) and (7, 6)

# The right dimensions (7 and 6) are not equal and neither is 1. So, these shapes are not compatible.

#     (6, 7) and (6, )

# These shapes are not broadcastable because (6, ) when padded with one we get (1, 6) which is not compatible with (6,7).

# Scalar Broadcasting

arr1 = np.array([1, 2, 3])
scalar = 5
print(arr1 + scalar) #  5 is stretched to [5,5,5] and added with all individual elements with arr1