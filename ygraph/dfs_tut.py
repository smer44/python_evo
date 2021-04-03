
G = {
    'a': ['b', 'c'],
    'b': ['c'],
    'c': ['a', 'd'],
    'd': ['a']
}

start_node = 'a'
visited = set()
stack = [start_node]

while stack:
    #print('Stack:' , stack)
    current_node = stack.pop()
    if current_node in visited:
        print(f'revisited {current_node}')
        continue
    print(f'reached {current_node}')
    visited.add(current_node)
    stack.extend(G[current_node])



        
        
        