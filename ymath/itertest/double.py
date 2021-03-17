import numpy as np
import matplotlib.pyplot as plt

def iter2(ax,cx, bx,ay,cy, by, alfax, alfay, n ):
    x = -bx/2
    y = -by/2

    for i in range(n):
        fx = ax * x + cx * y + bx
        fy = ay * x + cy * y + by 
        
        dfx = fx - x 
        dfy = fy - y

        x = x + dfx*alfax
        y = y + dfy*alfay
    return x,y


def iter2old(ax,cx, bx,ay,cy, by, alfax, alfay, n ):
    '''lets solve like that linear equasion system :
    x = ax * x + cx * y + bx
    y = ay * x  + cy * y + by
    
    '''
    x = 0#bx/(1-ax if ax != 1 else 0.1)#-bx/2
    y = 0#by/(1-cy if cy != 1 else 0.1)#-by/2

    for i in range(n):
        fx = ax * x + cx * y + bx
        fy = ay * x + cy * y + by 
        
        dfx = fx - x 
        dfy = fy - y
        """        
        dx1 = dfx*ax / (ax+cx)
        dy1 = dfx*cx / (ax+cx)
        
        dx2 = dfy*ay / (ay+cy)
        dy2 = dfy*cy / (ay+cy)        
        
        dx = dx1+ dx2
        dy = dy1+ dy2"""
        # if dx/dy becomes a constant  != there will be a overflow
        x = x + dfx*alfax
        y = y + dfy*alfay
        #print(f"iter2:step{i}: fx = {fx} , fy = {fy}, x0 = {x0} , y0 = {y0}")
        #print(f"iter2:step{i}: dfx = {dfx} , dfy = {dfy}, x = {x} , y = {y}")
        #print(f"-------------: dx1 = {dx1} , dx2 = {dx2}, dy1 = {dy1} , dy2 = {dy2}")
        #print(f"iter2:step{i}: dx/dy = {dx/dy if dy else 'dy is 0'}")
    return x,y


# converges:(0.4, 3.3, 0.5,0.1,0.4, 0.7) 
#does not converges:#(0.4, 6.3, 0.5,0.1,0.4, 0.7)
#say, cx >>1.
#lets try to heal it 
#healed with alfay = 
#eqs = (0.2, 0.3, 0.5,0.1,0.4, 0.7)


#eqs = (1.1, 2.3, 5,2.1,2.4, 7)

#alfax = 1
#alfay = -0.350 # is some function from ax,ay,cx,cy!!!

#x,y = iter2(*eqs,alfax, alfay, 10)

def look_for_alfay(*eqs,fro, to, n,iters):
    alfax = 1 #* 0.2
    step = (to-fro) / n
    #x,y = iter2(*eqs,-rangge, rangge, 10)
    #ch_old = check(*eqs,x,y)
    #try to make a step:
    ch_old = float('inf')
    #recalculate: 
    alfay_opt = 0
    for alfay in np.arange(fro,to,step):
        #alfay += step  
        x,y = iter2(*eqs,alfax, alfay, iters)    
        ch = check(*eqs,x,y)
        #print(f'look_for_alfay: alfay:{alfay}, error:{ch}')
        if ch < ch_old:
            alfay_opt = alfay
            ch_old = ch
    return alfay_opt , ch_old
            

    
        
    
    



def check(ax,cx, bx,ay,cy, by,x0,y0):
        x = ax * x0 + cx * y0 + bx
        y = ay * x0 + cy * y0 + by    
        #print(f'check =  x = {x} , y = {y}')   
        return abs(x-x0) + abs(y-y0)   
    
def checkxy(ax,cx, bx,ay,cy, by,x0,y0):
        x = ax * x0 + cx * y0 + bx
        y = ay * x0 + cy * y0 + by    
        #print(f'check =  x = {x} , y = {y}')   
        return x,y
    
#ch = check(*eqs,x,y)

#eqs = (0.4, 2.2, 0.5,0.1,0.3, 0.7)

fro = -10#-0.36
to = 10#-0.30
#alfay , ch = look_for_alfay(*eqs,fro = fro, to = to, n = 100, iters = 100)

cns = [x for x in  np.arange(0,5,0.01)]

alfays = []
for cn in cns:
    #eqs = (4, 0.3 , 0.5,0.8,cn, 70)
    eqs = (0.2, cn, 50,0.1,0.4, 0.7)
    alfay , ch = look_for_alfay(*eqs,fro = fro, to = to, n = 1000, iters = 100)
    print(f'cn : {cn}, alfay:{alfay}, error:{ch}')   
    alfays.append(alfay)
    
    
plt.plot(cns,alfays)

plt.show()


#print(f'error = {ch}')    
#print(f'END: alfay:{alfay}, error:{ch}')   

# with cx = 6.3:  iters = 10 : alfay:-0.3399999999999994, error:0.1631091893299934
# with cx = 6.3: iters = 50 : alfay:-0.22999999999999932, error:1.9565014024447436e-06
# with cx = 6.3: iters = 100 : alfay:-0.2099999999999993, error:3.1235014574804154e-12

# with cx = 2.3:  iters = 10 : alfay:2.326000000000005, error:0.14093737008488372
# with cx = 2.3:  iters = 50 : alfay:2.332000000000005, error:0.00010416188997552922
# with cx = 2.3:  iters = 100 : alfay:2.332000000000005, error:1.3257751785289429e-08


# with cx = 1.3:  iters = 10 : alfay:2.343999999999995, error:0.020366179627741454
# with cx = 1.3:  iters = 50 : alfay:2.3350000000000053, error:4.359160143962981e-09
# with cx = 1.3:  iters = 100 : alfay:1.779999999999995, error:0.0 (hard to evaluate, lost of 0 )

#with cx = 100 is it really messy,small change in alfay completely destroys it)

# with cx = 100:  iters = 50 : alfay:-0.009380000000000065, error:4.1465334662399433e-07 
# with cx = 100:  iters = 100 : alfay:-0.009640000000000055, error:1.0200174038743626e-14 

#now try with small values:

# with cx = 0, cy = 0  iters = 100 : alfay:0.5000000000000013, error:0.0

# with cx = 1, cy = 0  iters = 100 : alfay:0.5000000000000013, error:0.0

# with cx = 1, cy = 1  iters = 100 : alfay:-0.9199999999999999, error:0.0

# with cx = 1, cy = 3  iters = 100 : alfay:-0.7199999999999998, error:5.551115123125783e-17

# with cx = 3, cy = 3  iters = 100 : alfay:-0.7399999999999998, error:5.551115123125783e-17

# with cx = 0.5, cy = 0.5  iters = 100 : alfay:0.9200000000000017, error:0.0   


