import numpy as np
import pandas as pd
myList=[1,2,3,4,5,6,6,7,8]
arr=np.array(myList)
mylist1=[[1,2,3,4],[5,6,7,8]]
arr1=np.array(mylist1)
print(myList)
print(mylist1)
print(arr1)
a=np.arange(1,10,2)
print(a)

print(np.zeros(10))
print(np.ones(10))
print(np.random.rand(10))
print(np.random.randn(10))
print(np.random.randint(1,100,10))
print(np.random.randint(1,90,10))
print(np.zeros((4,5)))
print(np.zeros((2,1)))
print(np.ones((4,5)))
print(np.eye(4,5))
print(np.random.rand(2,3))
print(np.random.randn(4,5))
b = np.arange(2,30,2)
print(b)
mat2=np.random.randint(1,100,25)
print(mat2.reshape(5,5))
print(mat2.dtype)
print(arr1.dtype)

city5=[1,1,1,1,1,1,2,3,3,4,5,6,7,8,9,6]
arr2=np.array(city5)
print(arr2.reshape(4,4))
arr3=np.random.randint(1,100,16)
print(arr3.reshape(4,4))
m=arr2+arr3
print(m.reshape)
mat6=np.random.randint(1,100,9).reshape(3,3)
mat7=np.random.randint(1,100,9).reshape(3,3)
print(mat6+mat7)
print(mat6.sum())
print(mat7.mean())
print(mat6.min())
print(mat6.max())
print(mat6.std())
x=len(city5)
print(x)
mat10=mat7*mat6
mat10=mat7**mat6
mat10=mat7-mat6
mat10=mat7/mat6
mat10=mat7+mat6
print(mat10)
mat9=np.random.randint(1,100,10)
mat9.sort()
print(mat9)