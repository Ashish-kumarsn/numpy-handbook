import numpy as np

# Sample Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# -----------------------------
# np.stack()
# Creates a NEW axis
# Both arrays must have the same shape
# -----------------------------

np.stack((arr1, arr2), axis=0)
# Shape: (2,3)
# [[1 2 3]
#  [4 5 6]]

np.stack((arr1, arr2), axis=1)
# Shape: (3,2)
# [[1 4]
#  [2 5]
#  [3 6]]

# -----------------------------
# np.vstack()
# Vertical stacking (Top -> Bottom)
# No new logical axis for common use
# -----------------------------

np.vstack((arr1, arr2))
# [[1 2 3]
#  [4 5 6]]

# -----------------------------
# np.hstack()
# Horizontal stacking (Left -> Right)
# -----------------------------

np.hstack((arr1, arr2))
# [1 2 3 4 5 6]

# -----------------------------
# np.dstack()
# Stack along depth (3rd axis)
# Mostly used for images / 3D arrays
# -----------------------------

a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

np.dstack((a, b))
# Shape: (2,2,2)

# -----------------------------
# np.column_stack()
# Converts 1D arrays into columns
# Very useful for ML datasets
# -----------------------------

np.column_stack((arr1, arr2))
# [[1 4]
#  [2 5]
#  [3 6]]

# -----------------------------
# np.row_stack()
# Same as vstack()
# -----------------------------

np.row_stack((arr1, arr2))
# [[1 2 3]
#  [4 5 6]]






# stack()         -> Creates a NEW axis.
# vstack()        -> Stack vertically (top to bottom).
# hstack()        -> Stack horizontally (left to right).
# dstack()        -> Stack along depth (3rd dimension).
# column_stack()  -> Convert 1D arrays into feature columns.
# row_stack()     -> Same as vstack().



# split() requires equal-sized divisions and raises a ValueError otherwise.
# array_split() automatically creates nearly equal parts, even when the division isn't exact.

