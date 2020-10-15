import numpy as np

i = 10

print("The data type of i is",type(i))

a_i = np.zeros(i,dtype=int)#declare a array of zeroes
print("The data type of i is",type(a_i)) #np.ndarray
print("The data type of i[0] is",type(a_i[0])) #np.ndarray

x = 119.0
print("The data type of x",type(x))
y = 1.19e2
print("The data type of x",type(y))

z = np.zeros(i,dtype=float)
print(type(z))
print(type(z[0]))