'''
Created on 16.03.2021

@author: peter
'''

def fib(n):
    assert n >= 0 
    f0,f1 = 0,1 
    for i in range(n-1):
        f0,f1 = f1, f0+f1
    return f1 

'''
f(2n) = f(n) * f(n-1) + f(n) * f(n+1),
f(2n+1) = f(n)**2 + f(n+1)**2
https://stepik.org/lesson/13236/step/6?unit=3422
'''

def qfib(n, with_next=False):    
    if n < 2:
        response = [n, 1]
    else:
        fa, fb = qfib(n//2, with_next=True)
        if n % 2 == 1:
            response = [fa**2 + fb**2,
                        fb * (fb + fa) + fa * fb,]
        else:
            response = [fa * (fb - fa) + fa * fb,
                        fa**2 + fb**2]
    if with_next:
        return response
    return response [0]


def euc_gcd(a,b):
    '''
    euclid algorithm of fiding greatest common denominator 
    from https://stepik.org/lesson/13229/step/3?unit=3415
    complexity : O (ln a + ln b) 
    
    '''
    assert a>= 0 and b >= 0
    if a > b:
        a, b = b,a 
    #steps = 0
    while a:        
        b = b % a 
        if a > b:
            a, b = b,a 
        #steps += 1
    #print(f"eucld_gcd : steps : {steps}")
            
    return b

def euc_gcdv2(a,b):
    '''
    euclid algorithm of fiding greatest common denominator 
    from https://stepik.org/lesson/13237/step/4?unit=3423
    complexity : O (ln a + ln b)     
    '''
    assert a>= 0 and b >= 0
    while a and b:        
        b = b % a 
        if a > b:
            a%=b 
        else: 
            b%=a 
    return max(a,b)
            
        #steps += 1
    #print(f"eucld_gcd : steps : {steps}")
            
    return b


ab = (3918848,1653264)

g = euc_gcd(*ab)
assert g == 61232

print(g)

print(fib(8000))

