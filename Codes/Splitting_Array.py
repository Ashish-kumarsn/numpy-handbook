import numpy as np

# 1. split() — Equal splits only

arr = np.array([10, 20, 30, 40, 50, 60])

parts = np.split(arr, 2)
print(parts)            # [array([10,20,30]), array([40,50,60])]
print(parts[0])         # [10 20 30]   → output is a LIST of arrays
print(parts[1])         # [40 50 60]

parts = np.split(arr, 3)
print(parts)            # [array([10,20]), array([30,40]), array([50,60])]

# Unequal split → ERROR
# np.split(np.array([1,2,3,4,5]), 2)   #  ValueError: not equal division


# split() at specific indices (cut points)

arr = np.array([10, 20, 30, 40, 50, 60])

parts = np.split(arr, [2, 5])
print(parts)            # [array([10,20]), array([30,40,50]), array([60])]

# [2,5] means → cut before index 2, cut before index 5
# 10 20 | 30 40 50 | 60


# 2. array_split() — Equal OR unequal splits

arr = np.array([1, 2, 3, 4, 5])

parts = np.array_split(arr, 2)
print(parts)            # [array([1,2,3]), array([4,5])]  → no error!

arr = np.arange(10)
parts = np.array_split(arr, 3)
print(parts)            # [array([0,1,2,3]), array([4,5,6]), array([7,8,9])]
                        # extra element goes to earlier splits


# 3. hsplit() — Horizontal (column-wise) split

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])   # shape (2,4)

parts = np.hsplit(arr, 2)
print(parts[0])         # [[1 2]    → left half
                        #  [5 6]]
print(parts[1])         # [[3 4]    → right half
                        #  [7 8]]

# Visualization:
# 1 2 | 3 4
# 5 6 | 7 8   ← vertical cut


# 4. vsplit() — Vertical (row-wise) split

arr = np.array([[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]])   # shape (4,2)

parts = np.vsplit(arr, 2)
print(parts[0])         # [[1 2]    → top half
                        #  [3 4]]
print(parts[1])         # [[5 6]    → bottom half
                        #  [7 8]]

# Visualization:
# 1 2
# 3 4
# ----   ← horizontal cut
# 5 6
# 7 8


# 5. dsplit() — Depth split (3D arrays)

arr = np.arange(24).reshape(2, 2, 6)   # shape (2,2,6)
print(arr.shape)        # (2, 2, 6)

parts = np.dsplit(arr, 2)
print(parts[0].shape)   # (2, 2, 3)   → split along depth
print(parts[1].shape)   # (2, 2, 3)



# COMMON MISTAKES

# Mistake 1: using split() for unequal division → use array_split()
# np.split(np.arange(5), 2)    #  ValueError

# Mistake 2: confusing hsplit and vsplit
# hsplit → cuts columns (vertical cut line)
# vsplit → cuts rows (horizontal cut line)

# Mistake 3: forgetting output is a LIST
# parts = np.split(arr, 2)
# parts[0]  → first array   
# parts     → whole list    (not an array)