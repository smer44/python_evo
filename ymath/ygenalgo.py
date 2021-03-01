
class GenAlgo:
    
    def __init__(self):
        pass
    
    def __call__(self, *args):
        self.known = {}
        self.steps = 0
        return self.__algo__(*args)

    def __algo__(self,k,n,m):
        
        kn = self.known.get((k,n), None)
        if kn != None:
            #print(f'known: {k}, {n} : {kn} ')
            return kn 
        
        if k==0 and n==0: return 1.0
        if k < 0 or k > n: return 0.0
        self.steps +=1
        kn = self.__algo__(k,n-1,m)*k/m + self.__algo__(k-1,n-1,m)*(m-k+1)/m
        self.known[(k,n)]= kn
        return kn
    
p = GenAlgo()

print(p(0,0,3))
print(p(1,1,3))
print(p(1,0,3))

#----

print(p(1,2,3))
print(p(2,2,3))

print(p(1,3,3))
print(p(2,3,3))
print(p(3,3,3))

#---
print("P(k,n,3)")
print(p(0,4,3))
print(p(1,4,3))
print(p(2,4,3))
print(p(3,4,3))
print(p(4,4,3))
print(p.steps)
print(p(2,3,2))
print(p(256,988,256))
print(p.steps)