import numpy as np

# AXIS OPERATIONS

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.shape)          # (2, 3) -> 2 rows, 3 columns


# Sum WITHOUT axis (adds everything)

print(np.sum(a))        # 21  -> 1+2+3+4+5+6


# axis=0 -> column-wise (moves vertically)

print(np.sum(a, axis=0))    # [5 7 9]   -> (1+4, 2+5, 3+6)


# axis=1 -> row-wise (moves horizontally)

print(np.sum(a, axis=1))    # [6 15]   -> (1+2+3, 4+5+6)


# Mean along axis

print(np.mean(a))           # 3.5   overall average

print(np.mean(a, axis=0))   # [2.5 3.5 4.5]  column-wise avg
print(np.mean(a, axis=1))   # [2. 5.]        row-wise avg


# Min / Max along axis

print(np.min(a, axis=0))    # [1 2 3]  smallest in each column
print(np.min(a, axis=1))    # [1 4]    smallest in each row

print(np.max(a, axis=0))    # [4 5 6]  largest in each column
print(np.max(a, axis=1))    # [3 6]    largest in each row


# Argmax along axis

a = np.array([
    [3, 8, 2],
    [9, 1, 5]
])

print(np.argmax(a))         # 3   -> index in flattened array [3 8 2 9 1 5]

print(np.argmax(a, axis=0)) # [1 0 1]  -> row-index of max value per column
print(np.argmax(a, axis=1)) # [1 0]    -> col-index of max value per row


# Functions that support axis parameter

# np.sum(), np.mean(), np.min(), np.max(),
# np.std(), np.var(), np.argmin(), np.argmax(), np.prod()


# 3-D ARRAY axis intro

a = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(a.shape)   # (2, 2, 2) -> Axis 0, Axis 1, Axis 2 now exist


# REAL WORLD EXAMPLE (Students x Subjects)

marks = np.array([
    [80, 90, 70],
    [60, 85, 95],
    [75, 88, 92]
])

print(np.mean(marks, axis=1))  # [80. 80. 85.]      avg marks per student
print(np.mean(marks, axis=0))  # [71.67 87.67 85.67] avg marks per subject


# COMMON MISTAKES

# Mistake 1: confusing axis=0 vs axis=1
#   axis=0 -> column-wise operation
#   axis=1 -> row-wise operation

# Mistake 2: axis=0 does NOT mean "row 0"
#   It means operate along the row-axis, combining values within each column

# Mistake 3: ignoring output shape
a = np.array([[1, 2, 3],
              [4, 5, 6]])
print(a.shape)              # (2, 3)
print(np.sum(a, axis=0).shape)  # (3,) -> one result per column