#4: write this test:

from ysnake.gameobjs import *


gc = GameController(5,5)

print("gc.dim_x_singles : " , gc.dim_x_singles )

gc.grid[14*1+1*2] = 3
gc.grid[14*2+1*2] = gc.fruitn

gc.grid[14*1+4*2] = gc.fruitn

gc.grid[14*2+2*2] = -2
gc.grid[14*3+2*2] = 2
gc.grid[14*3+3*2] = gc.dim_x_singles
gc.grid[14*4+3*2] = -gc.dim_x_singles
gc.grid[14*4+4*2] = 3
gc.grid[14*5+4*2] = 2
gc.grid[14*5+5*2] = -2


show = gc.toTextArea

print(show())

"""
fr = gc.calcframe(18,2,2)

print(fr)



fr = gc.calcframe(14*3+3*2 ,2,2)

print(fr)


tt = gc.toTextAreax(0,0, 3, 3)

print(tt)
print("---")"""


#tt = gc.toTextAreax(2,1, 3, 3)

#print(tt)
print("--Start of loop size 2--")

for x in range(0,7):
    for y in range(0,7):
        fr = gc.calcframeh(x,y ,2,2)
        #print(fr)
        tt = gc.toTextAreax(*fr, 2, 2)
        print(tt)
        print("--")
        
        

print("--Start of loop size 3--")

for x in range(0,7):
    for y in range(0,7):
        fr = gc.calcframeh(x,y ,3,3)
        #print(fr)
        tt = gc.toTextAreax(*fr, 3, 3)
        print(tt)
        print("--")


print("--Start of loop size 4--")

for x in range(0,7):
    for y in range(0,7):
        fr = gc.calcframeh(x,y ,4,4)
        #print(fr)
        tt = gc.toTextAreax(*fr, 4, 4)
        print(tt)
        print("--")


