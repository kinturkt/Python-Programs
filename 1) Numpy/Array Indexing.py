import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a[0])
print(a[2])
print(a[-4])
print(a[-1])         # Negative index is from Left to right
print('----------------------------------------')

x = np.array([10,20,30,40,50,60,70,80,90,100])
print(x[2] + x[6])              # 30+70
print('----------------------------------------')

y = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', y[0, 1])
print('----------------------------------------')

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])