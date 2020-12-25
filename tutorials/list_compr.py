

arr = [ 1,3,5,7]


arr2 = [x * x for x in arr ]

#for x in arr 
#    append(x*x)

print(arr2)


arr2 = { x: x * x for x in arr }

print(arr2)

arr2 = { x * x for x in arr }

print(arr2)

arr2 = tuple( x * x for x in arr )

print(arr2)