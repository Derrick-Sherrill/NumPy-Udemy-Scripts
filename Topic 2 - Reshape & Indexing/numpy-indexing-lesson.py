import numpy as np

#Create simple array
array_a = np.array([[1,2,3],[4,5,6]])
print(array_a.shape)

# New Attribute Array Size
print(array_a.size)
# Number of Rows times Number of Columns

# Reshape Array
array_b = array_a.reshape(3,2)
print(array_b)
print(array_b.shape)

#transpose array_a
array_c = array_a.T
print(array_c)
print(array_c.shape)

# Access Row
print(array_c[0])

# Access Columns
print(array_c[:,0])

# Access Specific Values
print(array_c[1,1])
