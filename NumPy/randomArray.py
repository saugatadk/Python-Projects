import numpy as np

# array of length 5 with random integer values ranging from 1 to 100
rand_array = np.random.randint(1, 100, size=5)
print("5 random integer values ranging from 1 to 100:", rand_array)










# Array Creation Using np.random.rand()

# NumPy has the function called np.random.rand() to create an array of random numbers between 0 and 1.

# Let's see an example to create an array of 4 random numbers.

import numpy as np

# generate an array of 4 random numbers between 0 and 1
array1 = np.random.rand(4)
print(array1)

# Output Sample
# [0.68602938 0.34937158 0.62020974 0.54050377]







# Sometimes we may want to create an empty array and then add data later.

# In NumPy, we can create an empty array using the np.empty() function provided by the library. For example,

import numpy as np


# create an empty with total capacity of 5

empty_array = np.empty(5)


print("Empty Array:", empty_array)