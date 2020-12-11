import numpy as np 


arr = np.random.normal(0.5,0.2,(2,3))

arr2 = np.random.normal(0.5,0.2,(2,3))

print("arr : " , arr )

print("arr2 : " , arr2 )


randints  = np.random.randint(0,2,(2,3))


print("randints : " ,  randints )

child = np.where(randints, arr,arr2) # 0 - select from second if there is 0, from first if there is 1



print("child : " , child)





input = np.array([1,0])

print("input : " , input)

y = np.matmul(input, arr)

print("input X arr : " , y )


