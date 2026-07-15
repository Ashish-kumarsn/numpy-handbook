import numpy as np

# flatten()
# Converts multi-dimensional array → 1D array
# "Take all elements, put in a single row"

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)        # (2, 3)

flat = arr.flatten()
print(flat)             # [1 2 3 4 5 6]
print(flat.shape)       # (6,)


# 3D → 1D

arr = np.arange(24).reshape(2, 3, 4)
print(arr.shape)        # (2, 3, 4)

flat = arr.flatten()
print(flat.shape)       # (24,)   all 24 elements in one row


# Does flatten() change original? NO

arr = np.array([[1, 2],
                [3, 4]])

flat = arr.flatten()

print(flat)             # [1 2 3 4]
print(arr)              # [[1 2]   → original unchanged
                        #  [3 4]]


# MOST IMPORTANT — flatten() creates a COPY

arr = np.array([[1, 2],
                [3, 4]])

flat = arr.flatten()

flat[0] = 100           # modify flattened array

print(flat)             # [100   2   3   4]   → changed
print(arr)              # [[1 2]              → NOT changed
                        #  [3 4]]

# Why? because flatten() made a completely new array in new memory
# arr  → Memory A
# flat → Memory B  (separate copy)


# flatten() vs reshape(-1):-

arr = np.arange(6).reshape(2, 3)

print(arr.flatten())    # [0 1 2 3 4 5]
print(arr.reshape(-1))  # [0 1 2 3 4 5]  → same output

# BUT they behave differently in memory:

# | Function      | Returns  |
# | flatten()     | COPY     |  → safe to modify, uses extra RAM
# | reshape(-1)   | VIEW     |  → modifying affects original




#  Why is flatten() slower than reshape(-1)?
#  flatten() creates a full copy of data → needs extra memory allocation
#    reshape(-1) returns a VIEW of original → no copying → faster & efficient