import numpy as np

a = np.arange(10)
print(a.shape)
print(a)

a.resize(2,5)
print(a.shape)
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.reshape(3,2))
print(b.shape)
print(b.ravel())         # or use np.ravel(b)
print(b.shape)