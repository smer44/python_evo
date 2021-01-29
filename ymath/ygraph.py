

# set -> inheritence graph algorithm


input = ['ab', 'a' , 'b'  , 'abcd', 'bc' ]


frsets = [frozenset(x) for x in input]

print(frsets)

# sort : 
#frsets = sorted(frsets, key = lambda x : len(x))


def check_extend(lst, pos, default,fill = None):
    ln = len(lst)
    ext = pos - ln+1 
    if ext > 0:
        lst.extend([fill]*ext) 
    
    if lst[pos] == None:
        lst[pos] = default
    
    return lst 

"""
lst = [0,1,2 ]

lst = setextend(lst, 5, 5)

print(lst)
"""

        


def to_floors(frsets):
    floors = []
    for unit in frsets:
        ln = len(unit)
        check_extend(floors, ln, [])
        floors[ln].append(unit)
    
    return floors




floors = to_floors(frsets)

print(floors)


def yget (graph, positions, last_index):
    for pos in positions[:last_index]:
        graph = graph[pos]
    return graph


graph = [10,[20,[220,221], 22],4]


positions =   [1,2]      

yg = yget(graph, positions,2) # 0 -> root, one digit = level one child

print(yg)
        
        

#def next_sibling(graph, positions):
    
    
"""    


def find_inherite(graph, unit):
    for nodes in graph:
        if node in unit:
            
"""

        
        