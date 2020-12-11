
ar = [3,1] * 10

print(ar)


array = [0,1,1, 
         0,0,1, 
         0,0,0]

s = 0

def scan(arr):
    s = 0
    res  = []
    for x in arr:
        res.append(s)
        s += x ^1
        
    return res 



print(array)

sc = scan(array)
print(sc)

s = 0



free = [n for n,x in enumerate (array) if x == 0]
qid = 0

print("free : " , free)


#then we change  2 indexes in array :


array[1] = 0
array[3] = 1


# LIKE THAT :
print(array)

changing = sc[3]

print(changing)

free[changing]=1

print("free : " , free)







