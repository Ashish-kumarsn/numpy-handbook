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


# 2-D ARRAY 

darr = np.array (
    [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
)

print(darr[1][2]) #first method of access  [row][col]
print(darr[1,2]) #second method of access [row,col]



print(darr[1])   # printing row (1-d)

print(darr[1].shape) 

print("Printing multiple rows ")
print (darr[0:2])  ## printing multiple row 


print("sub-matrix printing ")    # this is called sub-matrix slicing 
print(darr[0:2,0:2]) # printing the sub-matrix of 2*2

print("printing column ")
print(darr[:,1])  ## take all row from column 1 (thoda socho )


print("entire row ") 
## there are two methods 

print(darr[0:2])  
print(darr[0:2,:])  # simillar to print the entire column 



# Negative Indexing in 2D

print("Working with negative index")
print(darr[-1])  # print entire last row 

print(darr[:,-1])  # print entire last column 

print(darr[-1,-1]) # print last element 






# 3-D ARRAY 

print("Now we are working with 3-D")

arr = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],

    [
        [7,8,9],
        [10,11,12]
    ]
])


print(arr.shape)

# syntax for accessing the element 
# arr[layer,row,column]

print(arr[1,1,1])
print(arr[0,0,2])

#selecting the entire row 
print(arr[0])  # this will print the entire 2-d raw of 0 index 

# Selecting Rows Inside a Layer

print("Selecting Rows inside a  layer ")
print(arr[0,1])  #arr[layer,row]


# printing Whole column 
print("Selecting entire column of a layer")
print(arr[0,:,1])   # arr[layer,: , column] 

#slicing layers
print("Slicing layers ")
print(arr[0:2])  # this will print the whole 3-d matrix 
print(arr[0:1])  # this will print only the first layer 2-d



