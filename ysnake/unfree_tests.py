from gameobjs import *


gc = GameController(5,5)

show = gc.toDebugStr

t = show()

print(t)
print(gc.frees)

gc.reset_free_indexes()

t = show()

print(t)

print(gc.frees)

gc.checkfrees()

print("create fruits unfree test")


amount = 5*5 

for _ in range(amount-2):
    gc.new_random_fruit()
    gc.checkfrees()
    gc.checkunfrees()
    

print(show())

print(gc.frees)

gc.new_random_fruit()
gc.checkunfrees()

print(show())
print(gc.frees)
# now there must be only one fruit 
# swap test:



grid_id_not_free = 2 
grid_id_free = gc.frees[0]


gc.changefree(grid_id_free, grid_id_not_free)

print("-- changefree test --")
print(show())
print(gc.frees)



