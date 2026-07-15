import numpy as np

# ravel()
# Converts multi-dimensional array → 1D array
# Looks same as flatten() BUT behaves differently

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

flat = arr.ravel()
print(flat)             # [1 2 3 4 5 6]
print(flat.shape)       # (6,)


# THE REAL DIFFERENCE  — ravel() returns a VIEW
# flatten() → always COPY
# ravel()   → usually VIEW (shared memory)

arr = np.array([[1, 2],
                [3, 4]])

flat = arr.ravel()

flat[0] = 100           # modify raveled array

print(flat)             # [100   2   3   4]   → changed
print(arr)              # [[100  2]            → ALSO changed !!
                        #  [  3  4]]

# Why? both arr and flat point to SAME memory location
# arr  → Memory A
# flat → Memory A  (same!)


# COMPARE: flatten() vs ravel()

arr = np.array([[1, 2],
                [3, 4]])

# flatten() — COPY
flat_f = arr.flatten()
flat_f[0] = 100
print(arr)              # [[1 2]   → original UNCHANGED
                        #  [3 4]]

# ravel() — VIEW
flat_r = arr.ravel()
flat_r[0] = 100
print(arr)              # [[100 2] → original CHANGED
                        #  [  3 4]]


# Does ravel() ALWAYS return a view? NO

# ravel() TRIES to return a view
# if not possible → automatically returns a copy
# example: transposed arrays may force a copy



# ravel() vs reshape(-1)

arr = np.arange(6).reshape(2, 3)

print(arr.ravel())          # [0 1 2 3 4 5]
print(arr.reshape(-1))      # [0 1 2 3 4 5]  → same output

# both usually return a VIEW
# difference:
# reshape(-1) → general reshaping operation
# ravel()     → specifically meant to flatten to 1D



# WHEN TO USE WHAT

# Use flatten() when:
# → you need independent array (safe to modify)
# → you don't want original to change

# Use ravel() when:
# → performance matters
# → memory matters
# → you just need flattened view, not a separate copy



# FULL PICTURE — View vs Copy in NumPy

# reshape()  → usually VIEW
# ravel()    → usually VIEW
# flatten()  → ALWAYS COPY
