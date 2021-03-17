'''
Created on 03.03.2021

@author: peter
'''


fx = lambda x,y : 1.1 * x + 2.3*y + 5 
fy = lambda x,y : 2.1 * x + 3.4*y + 7 

def limx(a,b) :
    return (2*b - a*b)/ (1-a)/ (2-a)

lx = limx(2.6,5)
print(f"limit x = {lx}")

def opt1(a,b,n ):
    x0 =  0# 0  # real solution  # b/(1-a)
    alfa = 1. if a < 1 else -0.7/a
    
    #alfa = 1/(1-a)/2 # if a is set so, the solution does not depend on x0 !!!
    for i in range(n):
        x_old = x0
        x = a*x0 + b
        dx = x -x0
        x0 = x0 +dx * alfa
        
        print(f" step {i}: f ({x_old:<5}) = {x}, dx = {dx},  next x = {x0}")
    return x0 

def newton(a,b,n):
    x = 244
    for i in range(n):
        x_old = x
        fx = (1-a) * x + b 
        x = x - fx/(1-a)
        print(f" step {i}: f ({x_old:<5}) = {x}, fx = {fx},  next x = {x}")
    
    
    
#1.1x + 5 -> konvergiert  in 40 Schritten zu -50
#1.4x +5 -> konvergiert  in  12 Schritten zu -12.5
#2x +5 -> konvergiert  in  1 Schritt zu -5
#2.2 x +5 -> konvergiert  in  6-12 Schritt zu -4.166
#2.5 x +5 -> konvergiert  in  15 Schritten zu -3.33333
#2.8 x +5 -> konvergiert schlimmer in  40 Schritten zu -2.77 ,
#am Anfang gbt es Schwankungen:
# 
# es gibt kleine Schwankungen 
# step 0: fx = -9.0 , next x = -1.0
# step 1: fx = 2.2 , next x = -4.2
# step 2: fx = -6.76 , next x = -1.6400000000000006
# step 3: fx = 0.4079999999999986 , next x = -3.6879999999999997

#die dann kleiner werden  und gehen nah zum x : 

# step 36: fx = -2.779797004333875 , next x = -2.7772008559046073
# step 37: fx = -2.7761623965329 , next x = -2.7782393152763145
# step 38: fx = -2.7790700827736803 , next x = -2.7774085477789487
# step 39: fx = -2.7767439337810558 , next x = -2.7780731617768417



opt1(50,50, 40)




#opt2(fx, fy, 0,0,1,100)









    