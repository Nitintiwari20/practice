# Creating 1 - D AND 2 - D ARRAYS IN NUMPY
import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# Using np.zeros/ones/empty/random() to create arrays
arr3 = np.zeros((2,3))
print(arr3)

arr4 = np.ones((3,3))
print(arr4)

arr6 = np.empty((2,3))
print(arr6)

arr7 = np.random.random((2,3))
print(arr7)

# Using np.arange() / np.linspace() to create arrays

arr8  = np.arange(10,20,3)
print(arr8)

arr9 = np.linspace(10,20,5)
print(arr9)

# Copying an array/ identity of an array

arr10 = np.array(arr1).copy()
print(arr10)

arr11 = np.identity(4)
print(arr11)