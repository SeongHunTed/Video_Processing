import numpy as np

list = [1,2,3,4,5,6,7,8,9,10]
sha1 = np.array(list).reshape(2,-1)
sha2 = np.array(list).reshape(2,-1)

print(sha1)
print(sha2)

print(sha1 + sha2)

arr1 = [[1,2,3,4,5],[6,7,8,9,10]]
arr2 = [[1,2,3,4,5],[6,7,8,9,10]]
arr3 = [[],[]]

print(arr1)
print(arr2)

print(len(arr1))
print(len(arr1[0]))

for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        arr3 = np.add(arr1,arr2)

print(arr3)