import numpy as np

# 4 x 4 array of random integers between 1 and 50
arr = np.random.randint(1,50, size=(4,4))

print("Original Array:/n", arr)

#find square of each element 
square = arr **2
print("/nSquare of each Array:/n", square)

#find row-wise sum
row_sum = np.sum(arr, axis=1)
print("/nRow-wise sum:/n",row_sum)
