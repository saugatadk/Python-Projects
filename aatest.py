import numpy as np

# take user input
array1 = np.array(list(map(int, input().split())))

# find even numbers using condition
even_arr1 = array1[array1 % 2 == 0]

# find even numbers using where()
even_arr2 = np.where((array1 % 2 == 0), array1, 0)

# print the results
print(even_arr1)
print(even_arr2)