from ysnake.gameobjs import *
from ysnake.evo_controller import *

#List of modifications : 
#1)

dx, dy = 5 ,5

dimx = (dx+2)

gc = GameController(dx,dy)

dir = - gc.dim_x_singles
gc.create_snake(2, 2, -dir, 3)

print(gc.toTextArea())

input = gc.toNInput()

len_input = len(input)

print("input length : " , len_input)
print("dimx, cells : " , dimx)
print("input length assume: " , dimx * (dy+2)*3)


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

s = ppr(input,dimx )



print(s)


#  nn usage

pop_size = 20

 
layer_dimms = len_input, 100,4

print("layer_dimms : ", layer_dimms )


ec = EvoController(pop_size,*layer_dimms)



# ---- what do we do each step --- :
# gain decision from Controller, with  network number n :
out = ec.forward(0, input)

print("out : " , out)

# maximal value from out vector is the best move
sndir = np.argmax(out)
print("argmax=direction : " , sndir)

# make this move in the game
gc.turn(0,sndir)

# get result of the move - false if snake crashed
move_result = gc.move_all()
print("moved_without_crash : " , move_result)


# the score of the snake is in fintesses[<snake_nr>)
score = gc.fintesses[0] if move_result else gc.last_fintesses[0]

print("score : " , score )

# now, lets put it into a method:

gc.reset_session()
def iterative_forward():
    count = 0
    max_steps = 200
    good_step = True
    print("iterative_forward start" )
    while(count < max_steps and good_step):
        input = gc.toNInput()    
        s = gc.toTextArea()
        print(" --- input ---")
        print(s)
        
        out = ec.forward(0, input)
        sndir = np.argmax(out)
        gc.turn(0,sndir)
        good_step = gc.move_all()
        
        score = gc.fintesses[0] if good_step else gc.last_fintesses[0]
        #check:
        print("score : " , score )
    score = gc.last_fintesses[0]
    print("final_score : " , score )
        
    
print("--- DENOMSTRATES THE INERATIVE RUN FRO A SNAKE NUMBER 0")        
iterative_forward()    
    
    
    




    
        