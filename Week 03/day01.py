# import numpy as np
# arr = np.aarray ([1,2,3,4,5,])
# print(arr)

# zeros = np. zerox ((2,3))
# print(zeros)
# rand = np.random.randint(1, 10,4)
# print(rand)






# import numpy as np
# a - np.array ([[1, 2, 3],[4, 6, 6]])
# print(a.shape)
# print(a.dtype)
# print(a.size)
# print(a.ndim)










# ####3Arry Methods 

# import njmpy as np
# b = np.array ({3,5, 6,7,9})

# print(b.resahpe(5, 3))
# print(b.max(), b.min())
# print(b.argmax(), b.argmin())



# # ######Copying, Appending and Inseting

# import numpy as np
# c = np.array ({1,2,3})
# c_copy = c.copy()
# c_copy[0] = 99
# print(c, c_copy)
# d = np.array ([1,2,3])
# print(np.append(d, [4, 5]))
# print(np.insert(d, 1, 100))









# #####Sorting , Deleting, Combning and splitting 


# import numpy as np
# e = np.array([5,2,8,1])
# print(np.short(e))
# print(np.delete(e, 0))

# f1, f2 = np.array ([1,2]), np.array([3, 4])
# print(np.concatenate((f1, f2)))
# print(np.array_split(np.arange(1, 7), 4))


# #### Task...

# nums = [22, 25, 45, 66, 75, 7, 87]
# nums.sort()
# print("Sorted", nums)
# del nums [2]
# print("print after deleting index 2:", nums)





# import numpy as np
# arr = np.array([1,2,3,4])
# np.save = ('my_array.np', arr)

# loaded = np.load('my_array.np')
# print(loaded)




# ####Indexing and Selection  (2D, Logical)


# import numpy as np
# g = np.array ([[1,2,3],[4,5,6], [7,8,9]])

# print(g[1, 2])
# print(g[g > 5])


#####Brodcasting...


# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])

# print(arr + 1)

# ######Task

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5])

# arr = arr * 3
# arr = arr - 1

# print(arr)




# import numpy as np
# i = np.array ([1,3,4.2,3.11])
# print(i.astype(int))

# j = np.array({1,23})
# k = np. arry([4,5,6])
# print(j + k, j-k, j *k)






# ############Type casting and ARithmetic Operation 

# import numpy as np

# arr = np.array([10.5, 20.8, 30.2, 40.9])

# result = arr.astype(int)

# print("Float array:", arr)
# print("Integer array:", result)


# ###### Universal Array 

# # impot numy as np
# # m = np. array ([1, 2,3,4,5])
# # print(np.sqrt(m))
# # n= np. array ([1, 2, 9,16])

# ####Taskk


# import numpy as np

# arr = np.array([1, 4, 9, 16, 25])

# roots = np.sqrt(arr)

# print(roots)






















###Prectice  


# ##Create a numpy ndarray objecl

# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr)
# print(type(arr))

# # ##Numpy array indexing

# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr[1])

# ##Numpy Array Slicing

# import numpy as np 
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr[2:5])

# import numpy as np
# arr = np.array([1,2,3,4])
# print(arr.dtype)

# ###Numpy Array copy vs view

# import numpy as np
# arr = np.array([1,2,3,4,5,5])
# x = arr.copy()
# arr[1] = 42
# print(arr)
# print(x)
# # 
# #Numpy array shape and reshaping

# import numpy as np
# arr = np.array([[1,2,3,4],[5,6,7,8,]])
# print(arr.shape)

# arr = np.array([1,2,3,4,5,6,7,8,9,11,23,44])
# newarr = arr.reshape(4,3)
# print (newarr)


# ### Array Iterating

# import numpy as np
# arr = np.array([1,2,3,4])
# for x in arr:
#     print(x)
    
# ######## Splitting Array

# import numpy as np
# arr = np.array([1,2,3,4,44,5])
# newarr = np.array_split(arr, 3)
# print(newarr)

# #######Searching Arrays
# import numpy as np
# arr = np.array([1,2,3,4,5,5])
# x = np.where(arr==3)
# print(x)

# ####Numpy Shorting array

# import numpy as np
# arr = np.array([3,4,6,2,9,1,0,66,5,33])

# print(np.sort(arr))

### Rendom nmbr

from numpy import random
x = random.randint(50)
print(x)