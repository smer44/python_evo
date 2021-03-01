'''
Created on 25.02.2021

@author: peter
'''
from ygrid.calc import *
from ygrid.pprint import *


gc = Calc(5,3,1)
gc.newgrid([3],[0])
print(gc)

pp = PPrint()
#pp.all_cell = False# one symbol printout

pp.setgrid(gc)

pp()

print(gc)


# ohh, it is line 0,1 - 2,1 with border concidering:


assert gc.check_line(1, 1,  3,5)
assert gc.check_line(1, 1, 2, 3)
assert gc.check_line(5, 3,  1,5)
assert gc.check_line(5, 3,  0,3)

print("xstart or ystart must be reported out of bounds")

assert not gc.check_line(0, 2, 3, 5)
assert not gc.check_line(1, 0, 2, 3)
assert not gc.check_line(6, 3, 1, 5)
assert not gc.check_line(5, 4, 0, 3)

print("must be false by snake length:")

assert not gc.check_line(1, 2, 3, 6)
assert not gc.check_line(1, 1, 2, 4)
assert not gc.check_line(5, 3, 1, 6)
assert not gc.check_line(5, 3, 0, 4)
assert not gc.check_line(1, 2, 3, 0)








