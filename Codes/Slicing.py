import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])


print(arr[1:4])  # Output: [20, 30, 40]

# Grab everything from index 3 to the end
print(arr[3:])   # Output: [40, 50, 60]

# Grab everything up to index 3
print(arr[:3])   # Output: [10, 20, 30]

# Step by 2 (take every second element)
print(arr[::2])  # Output: [10, 30, 50]

print(arr[::-1]) #reverse the array 