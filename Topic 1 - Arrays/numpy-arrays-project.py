import numpy as np

# 3x3
seq_a = [1,2,3]
seq_b = [4,5,6]
seq_c = [7,8,9]
array_abc = np.array([seq_a, seq_b, seq_c])
# Creating an Array from multiple lists. Note how we have to include all the lists in a second set of square brackets
# This is one way to make a nested list in Python
print(array_abc)

# What happens when we add floats as a new row in our array?
seq_d = [10.5,11.5,12.5]


array_abcd = np.array([seq_a, seq_b, seq_c, seq_d])
print(array_abcd)
# When we add floats to our numpy array, the entire dataset must then have the same data type.
# int data type does not accurately explain our float numbers, so the entire dataset is converted to float

# Challenge Answer: Make a 2x5 Array in one line with nested lists
array_d = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])

