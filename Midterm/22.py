import numpy as np

def mat_acc1(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i,j]
            mat[i,j] = k*2
def mat_acc2(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat.item(i,j)
            mat.itemset((i,j), k*2)

mat1 = np.arange(10).reshape(2,5)
mat2 = np.arange(10).reshape(2,5)

lut = [255 - i for i in range(256)]

print(lut)