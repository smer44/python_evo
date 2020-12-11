
from graphick_tutorials.gameobjs import *

gc = GameController(10,10)

gc.reset_session()

show = gc.toTextArea

#gc.new_fruit(10, 8)
#vertical step = (n+2) *2

#gc.new_random_fruit()

#gc.create_snake(6, 6,-24,3)

tt = show()
print(tt)


gc.move_all()
tt = show()
print(tt)

#turn right
gc.grid[gc.snakes[0][0]] = 2

tt = show()
print(tt)

#move further
gc.move_all()
tt = show()
print(tt)

gc.move_all()
tt = show()
print(tt)


#turn down
gc.grid[gc.snakes[0][0]] = 24

tt = show()
print(tt)


#---

gc.move_all()
tt = show()
print(tt)

gc.move_all()
tt = show()
print(tt)


