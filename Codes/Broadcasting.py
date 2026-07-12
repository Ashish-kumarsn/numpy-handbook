import numpy as np

a = np.array([1, 2, 3])

print(a + 10)  # [11 12 13]

# first a.shape = (3,) and 10 shape = ()
# () will become (1) , thus operation will work 



a = np.array([
    [1,2],
    [3,4]
])

print(a + 100)

# a.shape  = (2,2) and 100 shape = ()
# () will become (1,1) , thus this will work 
# same will be working with any dimensional array and a scalar operations


a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([10,20,30])

print(a + b) #  [[11 22 33]
             #  [14 25 36]]

# a.shape  = (2,3) and b.shape = (3,)
#(3,) will become (1,3) . thus from right to left 3==3 and 1 compatiable with 2 , works 


a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([
    [10],
    [20]
])

# a.shape = (2,3) and b.shape = (2,1)
# 3 compatiable 1 and 2==2 


print(a + b) #  [[11 12 13]
             #  [24 25 26]]



a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([10,20])

# a.shape  = (2,3) and b.shape = (2,)
# (2,) will become (1,2) 
# 3!=2 error will be given 

print(a + b)




# Intresting Example 

# Broadcasting Example: (3,1) + (3,)

import numpy as np

a = np.array([
    [1],
    [2],
    [3]
])                  # Shape: (3,1)

b = np.array([10,20,30])   # Shape: (3,)
                           # NumPy treats it as (1,3)

print(a + b)

# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]


# ---------------------- Explanation ----------------------

# Step 1: Compare shapes
# a -> (3,1)
# b -> (1,3)   # Missing dimension is added on the LEFT

# Step 2: Apply broadcasting rules
# (3,1)
# (1,3)
#
# Right: 1 vs 3 -> 1 expands to 3 
# Left : 3 vs 1 -> 1 expands to 3 

# Final broadcasted shape -> (3,3)

# Conceptually (not actually in memory):

# a becomes:
# [[1 1 1]
#  [2 2 2]
#  [3 3 3]]

# b becomes:
# [[10 20 30]
#  [10 20 30]
#  [10 20 30]]

# Final addition:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# Key Takeaway:
# The dimension that is 1 gets expanded.
# (3,1): 1 column -> expanded to 3 columns
# (1,3): 1 row    -> expanded to 3 rows
# NumPy performs this expansion virtually (no actual data copying).
