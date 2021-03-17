

def newton2(f,g, dax, day, dcx, dcy, n ):
    '''lets solve like that linear equasion system :
    '''
    print(f'newton2 : dax = {dax} , day = {day} , dcx = {dcx} , dcy = {dcy} ,')
    x = 0#-bx/2
    y = 0#-by/2
    gxy = g(x,y) 
    for i in range(n):
        
        fxy = f(x,y)
        x = x - fxy * dax #- gxy*dcx 
        
        gxy = g(x,y)
        y = y - gxy*dcy   # - fxy * day
        
        #then concider  derivative x for g: 
        #gxy = g(x,y)  
        
        #x = x - gxy*dcx
        
        #fxy = f(x,y)  
        
        #y = y- fxy*day        
        

        print(f" fxy = {fxy} , gxy = {gxy}, x = {x} , y0 = {y}")
    return x ,y



def xerror(funcs, *vars):
    '''    
    Calculates error of all functons, what must be zero:
    ''' 
    sum = 0
    for   f in  funcs:
        fval = f(*vars)
        sum +=  abs (fval)
    return sum   
        




#eqs = (0.2, 0.3, 0.5,0.1,0.4, 0.7)  
af = -10.7-1
cf = 10.01
bf = 0.5

ag = -10.8
cg = 10.9-1 
bg = 0.7

# trying to get ax * x + cx * y + b = 0, with cx > 1, i normalize the first equasion:
#ax, cx, bx = ax / cx, cx / cx, bx / cx, # such scaling has low effect

print(f'f (x) = {af}x  + {cf}y  +{bf} ')
print(f'g (x) = {ag}x  + {cg}y  +{bg} ')

ka = abs(af/ag)
kc = abs(cf/cg)

print(f' ka = abs(af/ag) =  {ka}  +  kc = abs(cf/cg) {kc}')

# i want following functions to be zero:
f = lambda x,y : af * x + cf * y + bf
g = lambda x,y : ag * x + cg * y + bg

daf, dag, dcf, dcg = 1/af, 1/ag, 1/cf, 1/cg

#Make it True to swap values iif need:
to_swap = True

if (kc > ka) and to_swap:
    #wap f and g:
    print(f' because kc > ka, swab f and g')
    f,g = g,f
    daf, dag, dcf, dcg = dag, daf, dcg, dcf 
    
    

x,y = newton2(f, g, daf, dag, dcf, dcg, 20)    
    
err = xerror ((f,g) ,x,y )
    
#ch = check(*eqs,x,y)

print(f'error = {err}')    
    








    