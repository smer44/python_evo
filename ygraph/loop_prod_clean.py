import numpy as np


a02 = 5
a12 = 7 
a40 = 6
a31 = 0.1
a23 = 3
a35 = 0.9

x = np.ones(5)

#sparce graph is array of entries[<node1 number>, <edge1 weight>, <node2 number>, <edge2 weight>,... ]

sg = [[4,a40], # x0
     [3,a31], # x1
    [0,a02,1,a12], # demand of x2
    [2,a23],    # demand of x3
    [2,a35],    # x3
       ]

def dfs_path_check(sg):
   
    dejavu = [-1 for _ in sg]
    ptr = 0 # root 
    path_mults = []
    last_mult = 1
    child_index = 0
    indexes = []
    child_indexes = []
    children = sg[ptr]
    prods_per_node = [[].copy() for _ in sg]
    loop_paths =  [[].copy() for _ in sg]
    
    if dejavu[ptr] >= 0:
        print(f'dfs_path_check : we have already visited ROOT: {ptr}, return')
        return  loop_paths, prods_per_node             
    
     
    while (ptr >=0):
        
            print(f'dfs_path_check: !!-make entry for node: {ptr} having node_path: {indexes}, last_mult: {last_mult}')     
            prods_per_node[ptr].append( (indexes.copy() + [ptr], last_mult))        
        
            # go deep into this node 
            dejavu[ptr] = len(indexes)
            print(f'dfs_path_check: --- analysing node: {ptr} , with path_mults: {path_mults}, last_mult: {last_mult}')
            child_row_ptr = child_index*2
            
            child_not_found = True
            # look for the next valide child:
            while (child_not_found and child_row_ptr < len(children)):
                child_ptr = children[child_row_ptr]
                print(f'dfs_path_check : the child number {child_index} is a node {child_ptr} ')
                
                dejavu_index = dejavu[child_ptr]
                child_not_found = dejavu_index >= 0 
                print(f'dfs_path_check : child {child_ptr} has  dejavu_index: {dejavu_index}')
                
                edge_weight =children[child_row_ptr + 1]
                #if it was visited, handle a loop:
                if child_not_found:                 
                    print(f'dfs_path_check : for a path: {indexes}, ptr: {ptr}, child : {child_ptr}, found a loop with last_mult : {last_mult} edge_weight: {edge_weight}')
                    loop_prod = last_mult *  edge_weight
                    before_loop_factor = prods_per_node[dejavu_index][-1][1]
                    
                    loop_paths[child_ptr].append( (indexes[dejavu_index:] + [ptr,child_ptr], loop_prod/before_loop_factor))
                
                child_index +=1
                child_row_ptr +=2

            #if we have visited all children of ptr and have not found a valide child:
            if child_not_found:
                print(f'dfs_path_check: we have visited all children of  {ptr}')
                
                parent_not_found = True 
                while (parent_not_found and indexes):
                    dejavu[ptr] =-1
                    ptr = indexes.pop()
                    last_mult = path_mults.pop()
                    child_index = child_indexes.pop()
                    parent_not_found = dejavu[ptr] >= 0 
                                    
                # if we are at the root, end:
                if parent_not_found:
                    print(f'dfs_path_check: we have visited all nodes of  {ptr}')
                    return  loop_paths, prods_per_node 

                children = sg[ptr]
                child_index +=1 
                             
            
            else: 
                print(f'dfs_path_check: going deep from parent {ptr} into child {child_ptr}  ')
                
                prod = last_mult *edge_weight                 
                path_mults.append(last_mult)
                child_indexes.append(child_index)
                indexes.append(ptr)
                
                ptr = child_ptr
                children = sg[ptr]
                last_mult = prod
                # if we gone deep into the child, the child_index must be 0?
                child_index = 0

    assert False , f'dfs_path_check : end of function must not be reachable'           
                
                
 
                   
loop_paths, prods_per_node = dfs_path_check(sg)       

print('Paths with loop found:' , loop_paths) 
print('Products per paths found:', prods_per_node)         
                
                 
            
            
             
        
        
         
    
