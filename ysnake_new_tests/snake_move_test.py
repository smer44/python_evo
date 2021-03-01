from ygrid.calc import *
from ygrid.frees import *
from ygrid.pprint import *
from ysnake import *


gc = Calc(5,5,2)
gc.newgrid([3,0],[0,0])


fr = Frees(gc)

pp = PPrint()


pp.setgrid(gc)

pp()

gcnn = Calc(5,5,3)
gcnn.newgrid([1,0,0],[0,0,0])

pp2 = PPrint()
pp2.set_print_mode('all')

pp2.setgrid(gcnn)

pp2()

sn = SnakeActors(gc,gcnn,fr)

sn.set_snake_start(1,1,2,3)

sn.create_snake(0)
assert fr.check()
pp()
pp2()

sn.move_snake(0)
assert fr.check()
pp()
pp2()

sn.move_snake(0)

pp()
pp2()


