import numpy as np

# UNIVERSAL FUNCTIONS (ufuncs)

a = np.array([1, 4, 9, 16])

print(np.sqrt(a))       # Output: [1. 2. 3. 4.]
print(np.sqrt(16))      # works on scalar too -> 4.0


# WITHOUT ufunc (manual loop way)
import math
result = []
for x in a:
    result.append(math.sqrt(x))
print(result)


# 1. UNARY ufuncs (one input array)

a = np.array([1, 4, 9, 16, 25])
print(np.sqrt(a))       # [1. 2. 3. 4. 5.]

a = np.array([2, 3, 4])
print(np.square(a))     # [4 9 16]

a = np.array([-10, -5, 3])
print(np.abs(a))        # [10 5 3]

a = np.array([1, 2, 3])
print(np.exp(a))        # [2.71828183 7.3890561 20.08553692]

a = np.array([1, np.e, np.e**2])
print(np.log(a))        # [0. 1. 2.]

angles = np.array([0, np.pi/2, np.pi])
print(np.sin(angles))   # [0. 1. 0.]   -> NumPy uses radians

angles = np.array([0, np.pi])
print(np.cos(angles))   # [ 1. -1.]


# 2. BINARY ufuncs (two input arrays)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.add(a, b))       # [5 7 9]   same as a+b
print(np.subtract(a, b))  # [-3 -3 -3] same as a-b
print(np.multiply(a, b))  # [4 10 18]  same as a*b
print(np.divide(a, b))    # same as a/b

a = np.array([20, 50, 30])
b = np.array([10, 60, 25])
print(np.maximum(a, b))   # [20 60 30]
print(np.minimum(a, b))   # [10 50 25]


# Operators internally call ufuncs
# a + b      -> np.add(a, b)
# a - b      -> np.subtract(a, b)
# a * b      -> np.multiply(a, b)
# a / b      -> np.divide(a, b)





print(np.log(0))     # -inf  (log of 0 is undefined)
print(np.sqrt(-4))   # nan   (sqrt of negative number not real)