from ymath.ylineq import *


# - simple test 
arrp= [[1,2], [4,5]]
#answers [[1,0],[4,1]] , [[1,2], [0,-3] 

arr = np.array(arrp, dtype=np.float32)

l,u = lu_decompose(arr)

print('L = \n', l)

print('U = \n',u)

#next test ---

arrp= [[1,2], [4,5]]


arrp= [2,1,1, 4,-6,0,-2,7,2]
'''
answers
L = 
 [[ 1.  0.  0.]
 [ 2.  1.  0.]
 [-1. -1.  1.]]
U = 
 [[ 2.  1.  1.]
 [ 0. -8. -2.]
 [ 0.  0.  1.]]
 '''
arr = np.array(arrp, dtype=np.float32)

arr = arr.reshape(3,-1)

l,u = lu_decompose(arr)

print('L = \n', l)

print('U = \n',u)



#next test  from https://stepik.org/lesson/9582/step/11?unit=1810

arrp= [1,1,1, 2,9,3,5,12,2]

'''
L = 
 [[1. 0. 0.]
 [2. 1. 0.]
 [5. 1. 1.]]
U = 
 [[ 1.  1.  1.]
 [ 0.  7.  1.]
 [ 0.  0. -4.]]
'''

arr = np.array(arrp, dtype=np.float32)

arr = arr.reshape(3,-1)

l,u = lu_decompose(arr)

print('L = \n', l)

print('U = \n',u)

#next test ---

'''
L = 
 [[1. 0. 0. 0.]
 [2. 1. 0. 0.]
 [3. 5. 1. 0.]
 [4. 6. 7. 1.]]
U = 
 [[1. 7. 6. 4.]
 [0. 1. 5. 3.]
 [0. 0. 1. 2.]
 [0. 0. 0. 1.]]

'''



arrp= [1,7,6,4,2,15,17,11,3,26,44,29,4,34,61,49]

arr = np.array(arrp, dtype=np.float32)

arr = arr.reshape(4,-1)

l,u = lu_decompose(arr)

print('L = \n', l)

print('U = \n',u)



