import numpy as np

# create a 3-D array
array1 = np.arange(1, 9).reshape(2, 2, 2)

# slicing the 3-D array
entire_array = array1[:, :, :]    # slice the entire array
print("\nEntire Array:")
print(entire_array)

second_matrix = array1[1, :, :]    # slice the second matrix
print("\nSecond matrix:")
print(second_matrix)

second_row_each_matrix = array1[:, 1, :]    # slice the second row of each matrix
print("\nSecond row of each matrix:")
print(second_row_each_matrix)

second_column_each_matrix = array1[:, :, 1]    # slice the second column of each matrix
print("\nSecond column of each matrix:")
print(second_column_each_matrix)

np_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\nSlicing 2d:")
print(np_array[:2, :])   # Here, we used the colon : operator to indicate that we want to extract all elements in the first two rows (indices 0 and 1) of the array.



# take list input
# list1 = eval(input())
list1 = [[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]]

# create the given array
arr = np.array(list1)
                 
# slice the first matrix
print(arr[0, :, :])

# slice the third column of the second matrix
print(arr[1, :, 2])

# slice the second row of each matrix
print(arr[:, 1, :])
#Output:
#[[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]]
# [[1 2 3 4]
#  [5 6 7 8]]
# [11 15]
# [[ 5  6  7  8]

#  create a 1D array
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# reshape the array with -1 for the second dimension
result = np.reshape(array1, (2, -1))

print("Reshaped array:")
print(result)

# flatten the array using -1
flattened_array = np.reshape(array1, -1)
print(flattened_array)


# flatten the array
flattened_array = array1.flatten()
print(flattened_array)
