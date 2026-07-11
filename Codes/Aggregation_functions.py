# Aggregation means combining multiple values into a single summary value.

import numpy as np 

arr= np.array([10, 20, 30, 40, 50])


# Sum of elements of a 
print(np.sum(arr))
# same as 
print(arr.sum())

# Mean or avg 
print(np.mean(arr))

# Median -> return the middle value after sorting 
print(np.median(arr))
# offcourse if even number of element then avg of both middle elements 


# min and max
print(np.min(arr))
print(np.max(arr))

# argmin and argmax 
# It return the index of min and the max value of the array respectively 

print(np.argmin(arr))
print(np.argmax(arr))


# product of all the elements 
print(np.prod(arr))


# Standard deviation  -> study about the standard deviation in detail 
# it is important 
print(np.std(arr))


# Variance = (standard deviation)^2

print(np.var(arr))


# Logical aggregation
print(np.any(arr))   # At least one True
print(np.all(arr))   # All values True