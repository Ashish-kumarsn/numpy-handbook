import numpy as np

# reshape()
# Changes shape WITHOUT changing the data
# Same elements, different arrangement

arr = np.arange(6)
print(arr)          # [0 1 2 3 4 5]
print(arr.shape)    # (6,)

arr2 = arr.reshape(2, 3)
print(arr2)         # [[0 1 2]
                    #  [3 4 5]]
print(arr2.shape)   # (2, 3)


# RULE 1 —> Total elements must stay same

arr = np.arange(12)   # 12 elements

arr.reshape(2, 6)     #  2×6   = 12
arr.reshape(3, 4)     #  3×4   = 12
arr.reshape(12, 1)    #  12×1  = 12
arr.reshape(2, 2, 3)  #  2×2×3 = 12

# arr.reshape(5, 2)   #  5×2  = 10 → ValueError
# arr.reshape(4, 4)   #  4×4  = 16 → ValueError


# RULE 2 — Elements filled row by row (C-order)

arr = np.arange(12)
print(arr.reshape(3, 4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]    <- fills left to right, top to bottom


# Reshaping into 3D

arr = np.arange(24)
print(arr.reshape(2, 3, 4))   # 2 layers, 3 rows, 4 cols
# think of it as: 2 blocks, each block has 3 rows × 4 cols


# -1 (Auto calculate that dimension)

arr = np.arange(12)

print(arr.reshape(3, -1))    # -1 → 12÷3 = 4 → shape (3,4)
print(arr.reshape(2, -1))    # -1 → 12÷2 = 6 → shape (2,6)
print(arr.reshape(-1, 6))    # -1 → 12÷6 = 2 → shape (2,6)

# arr.reshape(-1, -1)        # only ONE -1 allowed at a time ->wrong


# 1D ↔ 2D ↔ 3D conversions

arr = np.arange(6)

print(arr.reshape(2, 3))    # 1D → 2D
print(arr.reshape(6))       # 2D → 1D
print(arr.reshape(-1))      # 2D → 1D (flexible way, preferred)

arr = np.arange(24)
print(arr.reshape(2, 3, 4)) # 1D → 3D
print(arr.reshape(6, 4))    # 3D → 2D




# reshape() usually creates a VIEW, not a copy
# no data is duplicated → very fast & memory efficient
