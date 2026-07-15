import numpy as np

# expand_dims()
# Adds a NEW dimension of size 1 to an array
# Does NOT add new data — only adds a new axis

arr = np.array([10, 20, 30, 40])
print(arr.shape)        # (4,)


# axis=0 — adds dimension at the BEGINNING

new_arr = np.expand_dims(arr, axis=0)
print(new_arr)          # [[10 20 30 40]]
print(new_arr.shape)    # (1, 4)  -> one row containing four values


# axis=1 — adds dimension AFTER first axis

new_arr = np.expand_dims(arr, axis=1)
print(new_arr)          # [[10]
                        #  [20]
                        #  [30]
                        #  [40]]
print(new_arr.shape)    # (4, 1)  -> one column containing four values


# axis=0 vs axis=1 — quick comparison

arr = np.array([10, 20, 30, 40])    # shape (4,)

print(np.expand_dims(arr, axis=0).shape)    # (1, 4)  -> row
print(np.expand_dims(arr, axis=1).shape)    # (4, 1)  -> column

# Think of shape as a list  →  (4,)
# axis=0  inserts BEFORE  → (1, 4)
# axis=1  inserts AFTER   → (4, 1)


# expand_dims() on 2D array

arr = np.array([[1, 2, 3],
                [4, 5, 6]])         # shape (2, 3)

print(np.expand_dims(arr, axis=0).shape)    # (1, 2, 3)
print(np.expand_dims(arr, axis=1).shape)    # (2, 1, 3)
print(np.expand_dims(arr, axis=2).shape)    # (2, 3, 1)

# Notice: only a single 1 is inserted at the chosen position
# rest of the shape stays exactly the same


# General Rule

# Original shape (2, 3) — 2 dimensions
# axis=0  →  (1, 2, 3)   insert 1 before everything
# axis=1  →  (2, 1, 3)   insert 1 in the middle
# axis=2  →  (2, 3, 1)   insert 1 at the end


# expand_dims() vs np.newaxis — same result

arr = np.array([10, 20, 30, 40])

# axis=0
print(np.expand_dims(arr, axis=0).shape)    # (1, 4)
print(arr[np.newaxis, :].shape)             # (1, 4)  -> same!

# axis=1
print(np.expand_dims(arr, axis=1).shape)    # (4, 1)
print(arr[:, np.newaxis].shape)             # (4, 1)  -> same!

# both are valid — expand_dims() is more readable in code


# Memory Behavior — returns a VIEW

arr = np.array([1, 2, 3, 4])
new_arr = np.expand_dims(arr, axis=0)   # view, not a copy

new_arr[0, 0] = 999
print(arr)          # [999   2   3   4]  -> original ALSO changed


# COMMON MISTAKES

# Mistake 1: thinking new values are added
# NO — only a new dimension of size 1 is added, data stays same

# Mistake 2: confusing these three shapes
arr = np.array([1, 2, 3, 4])
print(arr.shape)                                # (4,)   1D
print(np.expand_dims(arr, axis=0).shape)        # (1,4)  row
print(np.expand_dims(arr, axis=1).shape)        # (4,1)  column
# these are 3 different shapes — don't mix them up

# Mistake 3: wrong axis for intended result
# always check what shape the model/function expects
# then pick axis accordingly


# INTERVIEW TIPS

# Q1: what does expand_dims() do?
# A:  inserts a new axis of size 1 at the given position
#     does NOT change the data, only the shape

# Q2: difference between reshape() and expand_dims()?
# A:  reshape()     -> can completely reorganize the shape
#                      total elements must stay same
#     expand_dims() -> only inserts a single dimension of size 1
#                      data is never rearranged


# SUMMARY so far — Shape Manipulation functions

# reshape()     -> change overall shape       | View (usually)
# flatten()     -> convert to 1D              | Always COPY
# ravel()       -> convert to 1D              | View (usually)
# transpose()   -> swap axes                  | View (usually)
# expand_dims() -> add a new axis of size 1   | View (usually)