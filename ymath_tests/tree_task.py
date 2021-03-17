# put your python code here
import re
import sys






taskdump = []
for i, line in enumerate(sys.stdin):
    if len(line) < 2 : continue
    taskdump.append(line)
    llst = line.split()
    assert len(llst) == 2, 'Assertion error '  + str(llst)
    if not i:
        vmax, e = llst
        vmax, e = int(vmax), int(e) 
        node_group = { n: {n}.copy() for n in range(1,vmax+1)}
        groups = {  tuple(v) for v in  node_group.values()}
    else:
        #print(node_group)
        v0,v1 = llst 
        v0,v1 = int(v0), int(v1)
        g0, g1 = node_group[v0], node_group[v1]
        
        tg1 = tuple(g1)
        groups.remove(tuple(g0))
        
        if not tg1 in groups:
            print("taskdump:" , taskdump)
        else:
            groups.remove(tg1)  
            
        
        
              
        
        g0.update(g1)
        node_group[v0] = g0 
        node_group[v1] = g0 
        groups.add(tuple(g0))
     
    #print(groups)   
    #print(vmax - len(groups))
    
#print("END:")     
#print(groups)   
print(len(groups))    