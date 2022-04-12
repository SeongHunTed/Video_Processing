import numpy as np

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr1 = np.array(list)
arr2 = np.array(list)

print(arr1 + arr2)

arr3 = []

for i in range(0, 10):
    arr3 = np.add(arr1, arr2)

print(arr3)