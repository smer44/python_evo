from ysnake_new.gridcalcs import *
from ysnake_new.gridprint import *


gc = GridCalc(11,9,3)

gc.newgrid([1,2,3],[0,1,0])

pp = GridPrint()


print(gc)

x,y = 2, 3

pos = gc.xy_cell_to_1d(2, 3)



assert (x,y) == gc.real_1d_to_xy_cell(pos)




ps =  pp(gc)

print(ps)


#--- single cell gridcalc 

gc2 = GridCalc(11,9,2)

pp.all_cell = False # change print mode

fruit_nr = 5
osctacle = 3


gc2.newgrid([3,0],[0,0])
gc2.set_xy(2, 3, 0, fruit_nr)

gc2.set_xy(1, 2, 0,osctacle)

gc2.set_xy(4, 6, 0,fruit_nr)

gc2.set_xy(7, 8, 0,fruit_nr)

ps =  pp(gc2)

print(ps)


# - test the frame 

gc2.framedimm(5, 5)




for x in range(11):
    gc2.focus_xy(x, x)
    print(gc2.info_focus())
    ps =  pp(gc2)
    print(ps)
    
    



