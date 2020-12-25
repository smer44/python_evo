from ysnake.gameobjs import *

gc = GameController(10,10)

#gc.reset_session()
dir = - gc.dim_x_singles
gc.create_snake(4, 4, -dir, 5)


print(gc.toTextArea())

nn_in = gc.toNInput()

#print(nn_in)

def ppr(nn_in, dimx):
    s = ""
    count = 0
    for x in range(0,len(nn_in),3):
        s+="|" + str(nn_in[x]) + "," +\
          str(nn_in[x+1]) + ","+\
           str(nn_in[x+2]) + "|"
        count +=1
        if (count%dimx == 0):
            s += "\n"
    return s

s = ppr(nn_in,12 )



print(s)
    
        
        
    