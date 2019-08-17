import numpy as np

array_a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

array_b = array_a.reshape(2,8)
print(array_b)

array_c = array_a.T
print(array_c.T)

print(array_c[0], array_c[1])

print(array_a[-1,-1])
