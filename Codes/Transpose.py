import numpy as np

# transpose()
# Swaps the axes of an array
# 2D → rows become columns, columns become rows

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.shape)        # (2, 3)
print(arr)
# [[1 2 3]
#  [4 5 6]]

arr_T = arr.T           # shorthand for transpose
print(arr_T.shape)      # (3, 2)
print(arr_T)
# [[1 4]
#  [2 5]
#  [3 6]]

# Original:             Transposed:
# 1 2 3                 1 4
# 4 5 6                 2 5
#                       3 6
# rows <-> columns flipped across the diagonal


# Both syntaxes give same result

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr.T)                    # shorthand — cleaner, used for 2D
print(np.transpose(arr))        # function  — more flexible


# Another 2D example

arr = np.array([[10, 20],
                [30, 40],
                [50, 60]])

print(arr.shape)        # (3, 2)
print(arr.T.shape)      # (2, 3)
print(arr.T)
# [[10 30 50]
#  [20 40 60]]


# 1D array — transpose does NOTHING

arr = np.array([1, 2, 3, 4])
print(arr.shape)        # (4,)
print(arr.T)            # [1 2 3 4]  -> unchanged!

# Why? 1D has only ONE axis
# transpose swaps axes -> nothing to swap


# 3D array — reverses axis order by default

arr = np.arange(24).reshape(2, 3, 4)
print(arr.shape)                # (2, 3, 4)
print(arr.transpose().shape)    # (4, 3, 2)  -> axes reversed automatically


# Custom axis order (only with np.transpose)

arr = np.arange(24).reshape(2, 3, 4)

print(np.transpose(arr, (1, 0, 2)).shape)   # (3, 2, 4) -> swap axis0 & axis1
print(np.transpose(arr, (2, 0, 1)).shape)   # (4, 2, 3) -> custom reorder

# arr.T cannot do custom ordering -> use np.transpose() for that


# Memory Behavior — returns a VIEW

arr = np.array([[1, 2],
                [3, 4]])

arr_T = arr.T               # usually returns a VIEW (shared memory)

arr_T[0, 0] = 999
print(arr)                  # [[999  2]  -> original ALSO changed
                            #  [  3  4]]


# reshape() vs transpose() — NOT the same

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# reshape -> rearranges elements into new layout
print(arr.reshape(3, 2))
# [[1 2]
#  [3 4]
#  [5 6]]   -> elements just packed differently

# transpose -> swaps rows and columns (axes)
print(arr.T)
# [[1 4]
#  [2 5]
#  [3 6]]   -> actual orientation flipped



# FULL COMPARISON — 4 functions

# Function       Purpose         View or Copy?
#------------------------------------------------
# reshape()   -> change shape    View (usually)
# flatten()   -> to 1D           Always COPY
# ravel()     -> to 1D           View (usually)
# transpose() -> swap axes       View (usually)


# COMMON MISTAKES

# Mistake 1: thinking transpose changes values -> NO, only positions change

# Mistake 2: expecting arr.T to work on 1D
# arr = np.array([1,2,3])
# arr.T  -> same array, nothing happens

# Mistake 3: confusing reshape() and transpose()
# reshape   -> new layout of same elements
# transpose -> flip/swap the axes


# INTERVIEW TIPS

# Q1: difference between reshape() and transpose()?
# A:  reshape()   -> rearranges elements into new shape
#     transpose() -> swaps axes (rows<->columns for 2D)

# Q2: why does arr.T not change a 1D array?
# A:  1D has only one axis — nothing to swap