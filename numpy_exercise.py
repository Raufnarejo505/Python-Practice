import numpy as np
# basics of numpy arrays

# attributes of arrays
# np.random.seed(0)
x1 = np.random.randint(10,size=(3,4,5))
# print("X1 ndim: " , x1.ndim)
# print("X1 shape: " , x1.shape)
# print("X1 size: " , x1.size)
# print(x1)

# indexing of arrays

# slicing of arrays
# x[start:stop:step]
x = np.arange(10)
print(x)
# print(x[4:7])
# print(x[::2])
# print(x[::-1])
# print(x[4::-1])
# working multy dimensions arrays 
print(x1[:,0])
print(x1[0,:])
# reshaping of arrays
# joining and splitting of arrays


