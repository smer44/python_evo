


a02 = 5

a12 = 7 

a40 = 6

a31 = 0.1

a23 = 3

a35 = 0.9

edges =  [[4], # x0
     [3], # x1
    [0,1], # demand of x2
    [2],    # demand of x3
    [2],    # x3
    ]


weights=  [[a40], # x0
     [a31], # x1
    [a02,a12], # demand of x2
    [a23],    # demand of x3
    [a35],    # x3
       ] 


visited = [-1 for _ in edges]

#sg = np.array(sg,dtype=np.float32)

def dfs_path_check(edges,weights, visited):

    prods_per_node = [0 for _ in edges]
    loop_prods =  [[].copy() for _ in edges]
    ptr = 0 
    stack = [ptr]
    prod_stack = [1]
       
        
    while stack:
           
            ptr = stack.pop()
            last_prod = prod_stack.pop()
            
            print(f'visiting {ptr}  visited : {visited} ')
            print(f'prod_stack : {prod_stack}  last_prod : {last_prod} ')
            visited_index = visited[ptr]
            if visited_index >= 0:
                prod_befor_loop = prods_per_node[ptr]
                print(f'reviseted {ptr} , with prod_befor_loop {prod_befor_loop}')
                loop_prod = last_prod/prod_befor_loop
                loop_prods[ptr].append(loop_prod)
                continue
            
            prods_per_node[ptr] = last_prod
            print(f'reached {ptr}')     
            visited[ptr] = 1 
            stack.extend(edges[ptr])
            
            new_factors =[w *last_prod for w in weights[ptr]]
            prod_stack.extend(new_factors)
            
    return loop_prods        

loop_prods = dfs_path_check(edges, weights, visited)

print(f'loop_prods : {loop_prods}')       


                 
            
            
             
        
        
         
    
