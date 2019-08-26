import numpy as np

array_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_b = np.array([[2,2,2],[3,4,5],[6,7,8]])
print(array_a)
print(array_b)

print(array_a.sum(axis=0))

print(array_a.ptp())

print(array_a.min(axis=1))
print(array_a.max(axis=1))
print(array_a.mean(axis=1))

# power
print(np.power(array_a, array_b))
array_c = np.array([[1,1,1],[2,2,2],[3,3,3]])
print( array_a + array_b + array_c)
