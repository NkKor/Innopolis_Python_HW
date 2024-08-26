import numpy as np


# 1

arr1 = np.zeros((5), int)
arr2 = np.zeros((5,4), int)
arr3 = np.zeros((5,10,2), int)
print(arr1)
print(arr2)
print(arr3)

# 2
arr1 = np.array([i for i in range(0,10)])
arr2 = np.array([i for i in range(5, 15)])
scalar = np.dot(arr1,arr2)
print(scalar)


#3
arr1 = np.array([i for i in range(15,105,2)])
mean = np.mean(arr1)
print(mean)


# 4
arr1 = np.array([2,5,3,6,8,11,13])
arr2 = arr1 * 5
arr3 = arr2 ** 0.25
res = np.median(arr3)
print(f"Медиана: {res:.4f}")