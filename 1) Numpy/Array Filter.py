import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

print('--------------------------------------')

arr = np.array([41, 42, 43, 44])
filter_arr1 = arr > 42
newarr1 = arr[filter_arr1]
print(filter_arr1)
print(newarr1)

print('--------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr2 = arr % 2 == 0
newarr2 = arr[filter_arr2]
print(filter_arr2)
print(newarr2)

print('--------------------------------------')

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)