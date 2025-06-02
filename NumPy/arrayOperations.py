import numpy as np
array1 = np.array([[1,2,-1,-2,10,12,20],
                   [1,2,3,-6,1,-10,-1]])

filtered_arr = array1[array1 < 0]

print(filtered_arr)

# replace negative values with 0
print(np.where(array1>0,array1,0)) #If the condition is true, it selects the corresponding element from array1, otherwise, it selects 0.


# if element is less than 2 or greater than 6, test condition is True
test_condition1 = (array1 < 2) | (array1 > 6)

# select element of x if test condition is True
# return 0 if test condition is False
result1 = np.where(test_condition1, array1, 0)
print(result1)


result = np.any(array1 > 3)
print(result)  # Output: True Since there is at least one element greater than 3 (4 and 5), the output is True.


# check if all element is less than 21
result = np.all(array1 < 21)
print(result)  # Output: True

array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
 
# check if all element in each row is greater than 5
result_row = np.all(array2 > 5, axis=1)
print(result_row)    # Output: [False  False  True]

# check if all element in each column is negative
result_column = np.any(array2 < 0, axis=0)
print(result_column)    # Output: [False False False]

#using stack operation axis 0 = rows and axis 1 = columns exception
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print("array1: \n", array1)
print("array2: \n", array2)

result = np.stack((array1, array2), axis = 0)
print("Result: \n",result)
result = np.stack((array1, array2), axis = 1)
print("Result: \n",result)

# calculate the sum along rows (axis 0)
array1 = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# calculate the sum along columns (axis 0)
sum_columns = np.sum(array1, axis=0)
print("Sum along columns:")
print(sum_columns)

# calculate the sum along rows (axis 1)
sum_columns = np.sum(array1, axis=1)
print("Sum along rows:")
print(sum_columns)

# calculate the average along columns (axis 0)
mean_columns = np.mean(array1, axis=0)
print("Average along columns:")
print(mean_columns)