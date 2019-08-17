import numpy as np

array_a = np.array([[1,2,3],[4,5,6]], dtype=float)
print(array_a)

array_b = np.zeros((3,3))
print(array_b)

array_c = np.ones((3,3))
print(array_c)

array_d = np.full((3,3), 5)
print(array_d)

array_e = np.random.random((3,4))
print(array_e)
