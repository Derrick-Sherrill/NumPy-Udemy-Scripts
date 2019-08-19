import numpy as np

# Introduce arange function
array_a = np.arange(0,100,5)
print(array_a)
print(array_a.size)

array_a = array_a.reshape(4,5)
print(array_a)

# Return Every Last Value of Row with Negative Indexing
print(array_a[:,-1])

# boolean practice:
array_above_50 = array_a[array_a > 50]
print(array_above_50)

#Indexing using Python Slices on one dimensional array
print(array_above_50[0:len(array_above_50):2])

#Taking Slice from Each Row of Array
print(array_a[:,0:5:2])

# Challenges Reverse each array row using negative indexing.
# index all values greater than 20 and less than 75, make everything else a value of zero and retain shape.
