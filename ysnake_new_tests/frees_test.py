from ygrid.calc import *
from ygrid.pprint import *
from ygrid.frees import  *


#init grid
gc = Calc(5,3,2)

fruit_nr = 5
obctacle = 3

gc.newgrid([3,0],[0,0])

gc.set_xy(2, 3, 0, fruit_nr)

#gc.set_xy(1, 2, 0,osctacle)

#gc.set_xy(4, 6, 0,fruit_nr)

#gc.set_xy(7, 8, 0,fruit_nr)

#init GridPrint
pp = PPrint()
pp.setgrid(gc)

pp()

# init frees:

fr = Frees(gc)

fr.new()

print('- after frees - ')

pp()
print(fr)


assert fr.check()

# unfree test: 
gc.set_xy(3, 3, 0, fruit_nr)

assert not fr.check()

fr.unfree(gc.ptr(3, 3))
assert fr.check()

pp()

# fruit is moving from 3,3 to 4,3 position:

gc.set_xy(3, 3, 0, 0)
gc.set_xy(4, 3, 0, 5)

#not the check must fail:
assert not fr.check()

#now i change free indexes:
fr.changefree(gc.ptr(4, 3), gc.ptr(3, 3))

print("-- FATER CHANGEFREE -- ")
pp()

#not the check must work:
assert fr.check()


 
