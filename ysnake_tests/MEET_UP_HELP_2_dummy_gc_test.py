from ysnake.dummy_game_controller import *
from ysnake.evo_controller import *



game_size = 10

gc = DummyGC(game_size)
gc.reset()

gc.position = 0

print(gc) 

print(gc.to_nn()) 

gc.move_left()

#print(gc.position)
#print(gc.check())fff

print(gc) 

gc.reset()

gc.position = 9


print(gc) 
gc.move_right()
print(gc) 
gc.reset()
#- evo controller now 

pop_size = 50#20


layer_dimms = game_size, 100,2

ec = EvoController(pop_size,*layer_dimms)


#----- iterative function 
#TODO - further like that 


def iterative_unit(unit_nr, show = False):
    pass 
    




