import random as r

arr = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]

tryes = 100000

successes = 0

for _ in range(tryes):
    sel = r.sample(arr,6)
    #greate histo:
    histo = [0 for _ in range(4)]
    hitso_set = {}
    for x in sel:
        histo [x] +=1
    if histo[0] and histo[1] and histo[2] and histo[3]:
        successes += 1
    
    key = frozenset(histo)
    print(key)
    
        
print(successes/ tryes) 
        
    
