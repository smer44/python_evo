
import pprint as pp


def div2(tup1, tup2 ):
    if tup1[0] == 0:
        return [tup1[0] ,1]
    return [tup1[0]*tup2[1] , tup2[0]*tup1[1]]

def mul2(tup1, tup2 ):
    
    return [ tup1[0]*tup2[0] , tup1[1]*tup2[1]]


def add2(a, b):
    if a[1] == b[1]:
        return [a[0]+ b[0], a[1]]
    
    return  [a[0]*b[1] + b[0]*a[1], a[1]*b[1]]
        
def sub2(a, b):
    if a[1] == b[1]:
        return [a[0]- b[0], a[1]]
    
    return  [a[0]*b[1] - b[0]*a[1], a[1]*b[1]]

def tokramer_line(y, elements):
    
    adds= [[0,1] for _ in elements]
    adds[y] = [1,1]
    
    return [[el, 1] for el in elements ] + adds
 
 
def  sub_line(line,next_line):
    
    return [sub2(line[x],next_line[x]) for x in range(len(next_line)) ]

def mul_scalar_line(a, line):
    return [mul2(a,b) for b in line]
 
 
def tokramer_all(lines):
    
    return [tokramer_line(y, line)  for y, line in enumerate(lines)]






def normalize_left_line(elements):
    #look for first non zero elements 
    for n, e in enumerate(elements):
        if e[0] != 0:
            div_on = e
            elements[n] = [1,1]
            for m in range(n+1, len(elements)):
                elements[m] = div2(elements[m] , div_on)

            
            return 




def normalize_left_all(eqs):
    for line in eqs:
        normalize_left_line(line)
        
        
def simplify_line(line):
    for x in range(len(line)):
        line[x] = simplify_naive(*line[x])
        
        

def simplify_naive(a,b):
    if a%b == 0:
        return [a//b,1]
        
    if a <0 and b < 0:
        a,b = -a , -b 
    
    m = min(abs(a),abs(b))+1
    x = 2
    while (x < m):
        while a%x == 0 and b%x == 0:
            a , b = a//x , b//x 
        m = min(abs(a),abs(b))+1
        x = x+1
    return [a, b]


def det3(a,b,c,d,e,f,g,h,i):
    return a*e*i +b*f*g+c*d*h-a*f*h-b*d*i-c*e*g


arr0 = [2,1,-3,1,-3,2,3,-4,-1]
arr1 = [-1,1,-3,10,-3,2,5,-4,-1]
arr2 = [2,-1,-3,1,10,2,3,5,-1]
arr3 = [2,1,-1,1,-3,10,3,-4,5]


print("arr0 :" , det3(*arr0))
print("arr1 :" , det3(*arr1))
print("arr2 :" , det3(*arr2))
print("arr3 :" , det3(*arr3))
        

xsim= simplify_naive(12,168)

print("simplify: " , xsim)     
        


els = [0,3,1,4,2]

tl = tokramer_line(2, els) 




print(tl)

normalize_left_line(tl)

print(tl)


ares = sub2([2,9], [3,11])

print(ares)



#---test : 

lines = [[3,2,-3 ], [0,3,4],[6,-7,-2]]


eqs = tokramer_all(lines)

pp.pprint(eqs)


print("---")


normalize_left_all(eqs)

pp.pprint(eqs)


eqs[2] = sub_line(eqs[2],eqs[0])

simplify_line(eqs[2])


print("---")

pp.pprint(eqs)



normalize_left_line(eqs[2])

simplify_line(eqs[2])


print("---")

pp.pprint(eqs)


#---

eqs[2] = sub_line(eqs[2],eqs[1])

simplify_line(eqs[2])


print("---")

pp.pprint(eqs)


#---

normalize_left_line(eqs[2])

simplify_line(eqs[2])


print("---")

pp.pprint(eqs)

#---

second_temp = mul_scalar_line(eqs[0][1], eqs[1])


simplify_line(second_temp)


print("---")

pp.pprint(second_temp)


eqs[0] = sub_line(eqs[0],second_temp)


simplify_line(eqs[0])

print("---")

pp.pprint(eqs)

#---

third_temp =  mul_scalar_line(eqs[0][2], eqs[2])

simplify_line(third_temp)


print("---")

pp.pprint(third_temp)



eqs[0] = sub_line(eqs[0],third_temp)


simplify_line(eqs[0])

print("---")

pp.pprint(eqs)


third_temp =  mul_scalar_line(eqs[1][2], eqs[2])


simplify_line(third_temp)


print("---")

pp.pprint(third_temp)



eqs[1] = sub_line(eqs[1],third_temp)

simplify_line(eqs[1] )


print("---")

pp.pprint(eqs)







            