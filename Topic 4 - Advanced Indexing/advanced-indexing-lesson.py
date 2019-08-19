import numpy as np


row_1 = [1,2,3,4,5]
row_2 = [6,7,8,9,10]
row_3 = [11,12,13,14,15]
row_4 = [16,17,18,19,20]
row_5 = [21,22,23,24,25]

test_data = np.array([row_1,row_2,row_3,row_4,row_5])
print(test_data)

# Using Python Slices
print(test_data[:,2:4:1])
# Same Elements but reversed
print(test_data[:,-2:-4:-1])

#boolean index
greater_than_five = test_data > 5
# returns one dimensional array
print(greater_than_five)
# single line operation
print(test_data[greater_than_five])
print(test_data[test_data>5])

# But what if we wanted to retain shape?
drop_under_5_array = np.where(test_data > 5, test_data, 0)
print(drop_under_5_array)

# Using Multiple Logic Conditions
drop_under_5_and_over_20 = np.logical_and(test_data>5, test_data<20)
print(drop_under_5_and_over_20)
print(test_data[drop_under_5_and_over_20])
