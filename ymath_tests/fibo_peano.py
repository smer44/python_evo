'''
Created on 01.03.2021

@author: peter

'''

#data : n , m , expected:
tests= [ (9,2,0) , 
          (10,2,1),
          (1025,55,5),
          (12589,369, 89),
          (1598753,25897, 20305),
          (60282445765134413,2263, 974),
         ]



def calc_period(n,m):
    '''
    assuming, there will be some periodicity, in Fib % n, 
    calculate it empirically: 
    
    '''
    known = [] 
    if m == 1: return 0
    dejavu = 0
    fnm2, fnm1 = 0, 1
    for i in range(n-1):
        backup = fnm1
        fnm1 = (fnm1 + fnm2 ) % m
        fnm2 = backup
        #check, if we are repeating the pattern:
        dejavu+=1
        i_check = dejavu 
        i_known = 0
        ln = len(known)
        while(known[i_known] == known[i_check]): 
            i_check+=1
            i_known +=1
            if(i_check == ln):
                return ln
                
        
           
    

def fib_mod(n,m):
    if not n: return 0
    fnm2, fnm1 = 0, 1
    for i in range(n-1):
        backup = fnm1 
        fnm1 = (fnm1 + fnm2 ) % m
        fnm2 = backup
    return fnm1


def main():
    #n, m = map(int, input().split())
    
    for n,m, expected  in tests:
        print(calc_period(n, m))


if __name__ == "__main__":
    main()