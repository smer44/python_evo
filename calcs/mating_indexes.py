

def mating_indexes(poplen, next_gen_size):
    
    arr = [ (x%poplen, (x+1+x//poplen)% poplen ) for x in range(next_gen_size)]
    return arr



arr = mating_indexes(11, 23)

print(arr)