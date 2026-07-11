import numpy as np 

a = np.array([1,2,3])
b= np.array([4,5,6])


#Har index ke element par individually operation perform hoga.

print(a+b)

# This is only possible when the shape are compatiable ie same shape 

print(b-a)

print(a*b)   # This is element wise multiplication not matrix multiplication

print(a/b)   # will give you float value like 3.333

print(a//b)  # will print the lower bound like 3.333 to 3

print(b%a) 

print(a**b)  # a^b

# Element wise operation can also take place with the scalar 

print(a+10)  # [11,12,13]

# same we can do with other operation and scalar values


print(a<b)  # same for other comparision operator like > , < , >= ,<= 


print("Let's Try Shape mismatch")

a = np.array([1,2,3])

b = np.array([4,5])

print(a+b)