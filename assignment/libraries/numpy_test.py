import numpy as np


#create a array with zeroes/ones
print(np.zeros(5))
print(np.ones(5))
print(np.full(5,4))


#range function in np
print(np.arange(0,8,2))


#matrix multiploication
a=np.array([[2,4],[8,5]])
b=np.array([[2,4],[8,5]])
print(np.dot(a,b))


#reshape into matrix
list1 = [1,2,5,4,7,8]
list1= np.array(list1).reshape(3,2)
print(list1)
list1= np.array(list1).reshape(2,-1)
print(list1)


