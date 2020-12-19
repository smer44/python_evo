import numpy as np 

print("Numpy Tutorials ")
arr = np.random.normal(0.5,0.2,(2,3))

arr2 = np.random.normal(0.5,0.2,(2,3))

print("arr : " , arr )

print("arr2 : " , arr2 )


randints  = np.random.randint(0,2,(2,3))


print("randints : " ,  randints )

child = np.where(randints, arr,arr2) # 0 - select from second if there is 0, from first if there is 1


print("--- selection from first or from second ---")
print("child : " , child)


randfloats = np.random.uniform(0,1,(2,3)) 

print("---")
print("randfloats : " ,  randfloats )

child2 = arr + (arr2 - arr) * randfloats# [a,b,c] * [d,e,f] = [a*d, b*e, c*f]





print("--- interpolation ---")
print("child2 : " , child2)

input = np.array([1,0])
print("---")
print("input : " , input)

y = np.matmul(input, arr)

print("input mult arr : " , y )



print("---")
input2 = np.array([[1,0],[0,1], [1,1]])
                   
print("input2 : " , input2)

y = np.matmul(input2, arr)

print("input2 mult arr : " , y )                   




