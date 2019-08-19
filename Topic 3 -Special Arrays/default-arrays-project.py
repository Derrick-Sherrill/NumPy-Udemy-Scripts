import numpy as np

# Available Data types

# np.int16 Integer (-32768 to 32767)
# np.int32 Integer (-2147483648 to 2147483647)
# np.int64 Integer (-9223372036854775808 to 9223372036854775807)

array_a = np.array([32766, 32767, 32768])

# Checking dtype
print(array_a.dtype)

array_b = np.array([32766, 32767, 32768], dtype=np.int16)
print(array_b)
#Overflow of NumPy Data Type (Unexpected Results)
# Argument for using smaller data types outside scope of course

# np.uint16 Unsigned integer (0 to 65535)
# np.uint32 Unsigned integer (0 to 4294967295)
# np.uint64 Unsigned integer (0 to 18446744073709551615)

array_c = np.array([-1,0,1], dtype=np.uint64)
print(array_c)

# np.float64 matches python float

# Other NumPy Data Types:
# np.bool_ (True/False)
# np.complex_ (Complex Numbers)
