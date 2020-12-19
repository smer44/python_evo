
from ysnake.gameobjs import *

gc = GameController(10,10)

#gc.reset_session()
dir = - gc.dim_x_singles
gc.create_snake(6, 6, dir, 5)

show = gc.toTextArea

print(show())

gc.grid[gc.snakes[0][0]] = 2
print(show())

gc.move_all()
print(show())

gc.grid[gc.snakes[0][0]] = -dir
print(show())

gc.move_all()
print(show())

gc.grid[gc.snakes[0][0]] = -2
print(show())

gc.move_all()
print(show())

