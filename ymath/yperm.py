
def next_combi(shifts, max):
    max -=1
    n = len(shifts)-1
    while(shifts[n]== max):
        n-=1
        max -=1
        if n < 0:
            return None 

    val = shifts[n]+1
    for m in range(n, len(shifts)):
        shifts[m] = val 
        val += 1
    return shifts
        
        
def yield_combi_indexes(k,n):
    shifts = [x for x in range(k)]
    #shifts = [0,3]
    while shifts:
        yield shifts
        #print(shifts)
        shifts = next_combi(shifts.copy(), n)
        
        

#x = [ a for a in yield_combi_indexes(6,16)] # C 6/16 is 8008 

#print(len(x))



def balls_task():
    arr = [x//4 for x in range(16)]
    print(arr)         
    results = {}
    for indexes in yield_combi_indexes(6,16):
        combi = tuple(arr[x] for x in indexes)
        histo = [0 for x in range(4)]
        for item in combi:
            histo[item] +=1
        if histo[0] and histo[1] and histo[2] and histo[3] :
            print(combi)
            fr_combi = combi
            results[fr_combi] = results.get(fr_combi, 0) +1
    
    print(results)
        
    


#balls_task()

def yield_heaps_perm(n):
    arr= [x for x in range(n)]
    print(arr)
    i = 0
    while i < n :
        if arr[i] < i:
            if i%2 == 0:
                arr[0] , arr[i] = arr[i] , arr[0] 
            else:
                arr[arr[i]] , arr[i] = arr[i] , arr[arr[i]] 
            print(arr)
            arr[i] +=1
            i = 0
        else:
            arr[i] =0
            i +=1
            
        

# Generating permutation using Heap Algorithm
 
 
def heapPermutation(a, size, n, depth = 0):
    #print (f"{'-'*depth } enter: size = {size}, n = {n}")
 
    # if size becomes 1 then prints the obtained
    # permutation
    if (size == 1):
        print(f"{'-'*depth } exit: OUTPUT {a} ")
        return
    heapPermutation(a, size-1, n, depth+1)
    for i in range(size-1):
        #heapPermutation(a, size-1, n, depth+1)
        
        
        k1 = 0  if size & 1 else i        
        k2 = size-1        
        
        #print (f"{'-'*depth } swap: size : {size } , pos : {k1} <-> {k2}")
        a[ k1], a[k2] = a[k2], a[k1]
        heapPermutation(a, size-1, n, depth+1)
        
        
    #print (f"{'-'*depth } exit after loop")    
 
# Driver code
a = [1, 2, 3,4]
n = len(a)
heapPermutation(a, n, n)

            

        
    
        
        
    
    