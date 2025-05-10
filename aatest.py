import numpy as np


# create a numpy array
array1 = np.arange(1, 13)

# get n as user input
n = int(input())

# get every nth element from array1
every_nth_element = array1[::2]
print(every_nth_element)

# calculate the standard deviation of every nth element
std_deviation = np.std(every_nth_element)

# display the resulting value
print(std_deviation)