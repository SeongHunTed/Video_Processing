import numpy as np, cv2

v1 = np.array([1,2,3], np.float32)

v1_exp = cv2.exp(v1)

print(v1.shape, v1)
print(v1_exp)
print(type(v1_exp), v1_exp.shape)