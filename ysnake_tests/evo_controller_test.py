from ysnake.evo_controller import *


def forward_all_for_input(ec, n):
    #print("forward_all_for_input(", n , "), fintesses len ", len(sc.errors))
    for unit in range(pop_size):
        out = ec.forward(unit, inputs[n])
        error = manhattan(out, expected[n])
        ec.errors[unit] += error 
                    
def forward_all(ec):
    for n in range(len(inputs)):
        forward_all_for_input(ec,n)



inputs = np.array([[0,0,1],[0,1,0],[1,0,0]])


expected = np.array([[1,0,1,0,1], [0,1,0,1,0], [0,1,1,0,1]])
        
    
pop_size = 20


layer_dimms = 3,10,5

ec = EvoController(pop_size,*layer_dimms)


forward_all(ec)

#print(ec.layers[-1])
print(np.sum(ec.errors) )

ec.next_gen()

forward_all(ec)

print(np.sum(ec.errors) )

for _ in range(200):
    ec.next_gen()
    forward_all(ec)
    print("Sum error : ", np.sum(ec.errors) )
    
    

"""out = ec.forward(0, inputs[0])

print(out)

error  = manhattan(out, expected[0])

print(error)"""



"""
a = np.array([[1,2,3],[4,5,6]])

b = np.array([[10,20,30],[40,50,60]])


print( a.shape)             
print(np.abs(a-b).sum(0))"""

              

"""arr = np.array([1,2,3])

arr2 = np.array([10,20,30])


child = mate_interpolate(arr, arr2)

pp.pprint(child)"""