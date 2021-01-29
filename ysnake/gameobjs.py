import random as r

   

class GameController:
    
    
    def __init__(self, dim_x, dim_y):
        

        
        self.fruitn = 5
        
        
        self.deaths = []
        self.snakes = []
        self.fintesses = []
        #self.last_fintesses = []
        self.reset_grid(dim_x, dim_y)
 
         
        self.set_snake_start(self.xhalf//2-2, self.yhalf, -self.dim_x_singles, 3)
        
        print('__init__')
        
    #SHOW: Small change 
    def set_snake_start(self, x,y, dir, sn_len):
        print("init snake start ", x,y, dir, sn_len)
        self.snake_start_x , self.snake_start_y = x,y
        self.snake_start_dir , self.snake_start_len = dir, sn_len 
        
    #2: self.xhalf variable = size of half width pf cells, + 1 if it is odd
    def reset_grid(self,dim_x, dim_y):
        self.dim_x_pairs = dim_x+2
        self.dim_x_singles = self.dim_x_pairs * 2 
        self.dim_y = dim_y+2
        
        self.xhalf= (self.dim_x_pairs//2 + self.dim_x_pairs%2) *2
        
        self.yhalf = (self.dim_y//2 + self.dim_y%2)
        print(" self.xhalf" ,  self.xhalf)
        
        #self.dimall_pairs =  self.dim_x * self.dim_y
        
        self.displays = {0 : ' ', 
                    -2 : '<',
                    2 : '>', 
                    self.fruitn : '@',
                    3 : '#', 
                    self.dim_x_singles:'V',
                    -self.dim_x_singles:'^'
        
                    }
        
        self.nnmap= {0:[0,0,0],
                    -2:[1,0,0],
                     2:[1,0,0], 
                     self.fruitn : [0,1,0],
                     3 :[1,0,0],
                     self.dim_x_singles:[1,0,0],
                     -self.dim_x_singles:[1,0,0],
            }
     
        #xxxxxx
        #x0000x
        #xxxxxx
        
        border_row = [3,-1] * self.dim_x_pairs# = 3,-1,3,-1,3,-1, ... x self.dim_x_pairs times 
        
        inner_row = [3,-1] + [0,0] * dim_x + [3,-1]# = 3,-1 , 0,0 x dim_x [3,-1] 
        #print(inner_row)
        
        self.grid =  border_row + inner_row*dim_y + border_row
        self.directions = [-2,-self.dim_x_singles,2,self.dim_x_singles] 
        self.reset_free_indexes()
        print("reset_grid")
        
    
    def reset_free_indexes(self):
        self.frees = []
        for y in range(1,self.dim_y -1,1 ):
            row_begin = y*self.dim_x_singles
            #print("reset_free_indexes : row_begin : " , row_begin)
            for x in range(2,self.dim_x_singles-2,2 ):
                cell_index = row_begin + x
                #print("reset_free_indexes : cell_index : " , cell_index)
                cell = self.grid[cell_index]
                if not cell:
                    self.grid[cell_index+1] = len(self.frees)
                    self.frees.append(cell_index)
                    
                    
                     
    #test, if all indexes in frees are zero in self.grid
    def checkfrees(self):  
        for index in self.frees:
            if self.grid[index]:
                print("checkfrees : non free index entry in frees: " , index)
                return False
        print("checkfrees : ok")  
        return True
        
    def checkunfrees(self):
        for cell_id in range(0,len(self.grid),2):
            if self.grid[cell_id] and self.grid[cell_id+1] != -1:
                print("checkunfrees : !!!! frees-index of not free element must be -1 : " , self.grid[cell_id] ,  " : " , self.grid[cell_id+1] )
                return False
        print("checkunfrees : ok") 
        return True
                 
                
               
        
    #permanently delete the cell from free cell index 
    #glue the free indexes by moving the last frees element 
    # to deleted position
    # frees : ABCD -> AxCD -> ADC
    def unfree(self, cell_index):
        #print(" --- unfree --- ")
        #print("cell_index : " , cell_index)
        unfree_index = self.grid[cell_index+1]
        #print("unfree_index : " , unfree_index)
        self.grid[cell_index+1] = -1
        #print("self.grid.cell_index : " , self.grid[cell_index] , " : " , self.grid[cell_index+1])
        last_free_pos = self.frees.pop()
        if last_free_pos == cell_index:
            #we just deleted the last frees entry, do further nothing
            return 
         
        
        
        #last_free_index = len(self.frees) - 1
        #last_free_pos = self.frees[last_free_index]
        #print("last_free_pos : " , last_free_pos)
        #print("last_free_index : " , last_free_index)
        self.grid[last_free_pos+1] = unfree_index
        #print("self.grid.last_free_index after: " , self.grid[last_free_pos] , " : " , self.grid[last_free_pos+1])
        self.frees[unfree_index] = last_free_pos
        #self.frees.pop()
        
    #8: previous new_random_fruit function to put random obstacle on the firld :
    # def new_random_fruit(self):
        
    def new_random_object(self, value):
        fruit_index = r.choice(self.frees) 
        self.grid[fruit_index] = value
        self.unfree(fruit_index)
        
   
    #swap one free and one non free squares in frees entries:     
    #frees ABC -> ADC
    def changefree(self, grid_id_free, grid_id_not_free):    
        free_id_from = self.grid[grid_id_free+1]
        # free_id_to = self.grid[grid_id_to+1] must be -1 # check
        self.frees[free_id_from] = grid_id_not_free
        
        self.grid[grid_id_not_free+1] = free_id_from
        self.grid[grid_id_free+1] = -1
        
   
        
  
    def create_snake(self,x,y,dir, size):
        
        tail = y * self.dim_x_singles + x
        
        for n in range(size):
            grid_id = tail + n * dir
            self.grid[grid_id] = dir 
            self.unfree(grid_id)
            
        
        head = tail + (size-1)*dir
        
        sn = [head, tail]
        
        self.snakes.append(sn) # snake = [head, tail]
        self.fintesses.append(0)
        print("reset fintess for snake ", len(self.snakes)-1 )
        #self.loosers.append(0)
        return sn
        
    # 1:  self.player_snake   
    def create_player_snake(self):
        dir = - self.dim_x_singles
        self.player_snake = self.create_snake(self.snake_start_x*2, self.snake_start_y, dir, 3)
        
     
    def reset_fintesses(self):
        self.last_fintesses = self.fintesses
        self.fitnesses = []
    
    def reset_session(self, obstakles = 0):
        self.reset_fintesses()
        self.reset_grid(self.dim_x_pairs -2 , self.dim_y-2)
        self.snakes = []
        self.create_player_snake()
        #8: change it to new_random_object
        self.new_random_object(self.fruitn)
        #9: create some obstacles : 
        for _ in range(obstakles):
            self.new_random_object(3)
        
    
    def turn_first_right(self):
        if self.grid[self.snakes[0][0]] != -2: 
            self.grid[self.snakes[0][0]] = 2   
        
    def turn_first_left(self):
        if self.grid[self.snakes[0][0]] != 2: 
            self.grid[self.snakes[0][0]] = -2      
        
    def turn_first_up(self):
        #if we were moving down, ignore:
        if self.grid[self.snakes[0][0]] != self.dim_x_singles: 
            self.grid[self.snakes[0][0]] = -self.dim_x_singles   
        
    def turn_first_down(self):
        if self.grid[self.snakes[0][0]] != -self.dim_x_singles: 
            self.grid[self.snakes[0][0]] = self.dim_x_singles   
            
     
    #+100: turn function       
    def turn(self, snake_nr, dir_index):
        snake_head = self.snakes[snake_nr][0]
        old_dir = self.grid[snake_head]
        new_dir = self.directions[dir_index]       
        #hard rules - lost if opposite direction chosed:
        self.grid[snake_head] = new_dir
        print("turn : old_dir : " , old_dir , "new_dir : " , new_dir)


    #3: calculate a view frame if the hero is on some position:
    #    
    def calcframe(self,pos,xdim,ydim):
        xhalf = xdim//2 + xdim%2
        yhalf = ydim//2 + ydim%2
        xhalf *=2 # // because dim_x cell is of size 2
        
        assert pos%2 == 0
        #print("calcframe", pos,xhalf,yhalf)
        xpos = pos % self.dim_x_singles
        assert ((pos - xpos) %  self.dim_x_singles) == 0
        ypos = pos //self.dim_x_singles
        

        #align frame to max borders:
        x1 = min(xpos + xhalf, self.dim_x_singles ) - xdim*2
        y1 = min(ypos + yhalf, self.dim_y ) - ydim
        
        #align the frame to minimum borders 
        x0 = max(x1,0)
        y0 = max(y1,0)
                
        
        
        
        assert (x0 %2) == 0
        return x0//2,y0
        
    #7: helper for calcframe function 
    def calcframeh(self,x,y,xdim,ydim):
        return self.calcframe(x*2+y*self.dim_x_singles,xdim,ydim)
    
 

    def move_snake(self,sn, index):
        head_pos = sn[0]
        dir_head = self.grid[head_pos]   
        next_pos = head_pos + dir_head   
        
        # we do not need to check in bounds,
        #since arena is bordered by obstacles
        #if not self.is_inbounds(next_pos):
        #   self.loosers.append(sn)
        #    return
        
        next_value = self.grid[next_pos]   
        if next_value:
            if next_value == self.fruitn:
                #if the fruit is eaten:
                # just move the head forwards:
                self.grid[next_pos] = dir_head
                sn[0] = next_pos
                #8: change to new_random_object #  create new fruit:
                self.new_random_object(self.fruitn)
                self.fintesses[index] += 1000
                #9: create new obstacle : 
                self.new_random_object(3)
                

            else:
                #there is a collision:
                self.loosers.append(index)
                #self.fintesses[index] =0
                
        else:
            #get coordinates and direction of the tail:
            tail = sn[1]
            dir_tail = self.grid[tail]
            #erace tail:
            self.grid[tail] = 0
            #set  new tail position to the snake:
            sn[1] = tail + dir_tail             
            #set snake head to the grid facing in the same direction
            self.grid[next_pos] = dir_head
            #set  new head position to the snake:
            sn[0] = next_pos
            self.changefree(next_pos, tail)
            self.fintesses[index] += 1
            

            
            
            
    
    def move_all(self):
        
        all_ln = len(self.snakes)
        self.loosers = []
        print("move_all len" , all_ln)
        for x in range(all_ln):
            self.move_snake(self.snakes[x],x)
        return self.checkloosers()
                
    def checkloosers(self):
        if self.loosers:
            #for unit in self.loosers:
            #    unit.deaths +=1
            self.reset_session()
            print("session reseted")
            return False
        return True
            

    
    def toDebugStr(self):
        s = ""
        for n in range(0,len(self.grid),2):
            
            if not (n % self.dim_x_singles):
                s+="\n"
                
                
            if self.grid[n] ==self.fruitn:
                s+= '|@'+ ':'+str(self.grid[n+1])  + '| '
            else:
                s+= '|' + str(self.grid[n]) + ':'+str(self.grid[n+1])  + '| '

      
        
               
        return s
        #return str(self.snakes[0])
    
    #6: printout helper:
    def toTextAreax(self, x,y , dimx, dimy ):
        print("toTextAreax : " , x, y)
        return self.toTextAread(2*x+y* self.dim_x_singles, dimx*2, (y+dimy)* self.dim_x_singles)
        
          
    

         
    
    
    
    #5: function to printout    
    def toTextAread(self, pos, dimx, posmax ):  
        #print("toTextAread : pos :" , pos , " dimx : " , dimx , " posmax ", posmax)  
        s = ""
        while( True):
            for x in range(0,dimx,2):
                symbol = self.displays[self.grid[pos+x]]
                s += symbol+' '
            pos+=self.dim_x_singles
            if(pos >= posmax):
                return s            
            s+="\n"

                
    #11: lets create a view frame for snake head:
    
    
    def  toTextAreaHead(self, xdim, ydim):
        pos = self.snakes[0][0]
        x0y0 = self.calcframe(pos,xdim,ydim)
        s= self.toTextAreax(*x0y0, xdim, ydim)
        return s
             
        
    def toTextArea(self):
        s = ""        
        for n in range(0,len(self.grid),2):            
            if not (n % self.dim_x_singles):
                s+="\n"            
            symbol = self.displays[self.grid[n]]
            s += symbol+' ' 
        return s
    
    # obstacke[1,0,0}, fruit =[0,1,0], head = [0,0,1]
    # obstacke = 1, fruit = 0.5 ,head = 0
    
    def toNInput(self):
        s = []
        for n in range(0,len(self.grid),2):  
            symbol = self.nnmap[self.grid[n]]
            
            s+=symbol
        # mark sneak head 
        head_pos = self.snakes[0][0] //2 * 3
        print("head_pos : " , head_pos)
        s[head_pos] = 0
        s[head_pos+1] = 0
        s[head_pos+2] = 1
        return s
        
        
             
            
        
        
        
    
'''    
class SnakeBotMover:
    
    
    def __init__(self, grid, sn, dimx):
        self.grid = grid
        self.dim_x = dimx
        self.sn = sn 
        self.mode = 0 # 0 - go to border , 1 - get fruit
        self.extra_border = 0
        self.fruitn = 1000*1000
        self.desigions = [self.turnRight]
    
    
    def rightOfDir(self,dir):
        if dir == 1:# right
            return self.dim_x #down
        if dir == -1:# left
            return -self.dim_x # up 

        if dir > 1:#up
            return -1#left  
        return 1 # else, if the direction is down return right
        
    #decide how to move - tryes to move to the fruit along the border, then 
    # circle around the border
    # goToBorder tryes to go to the 
    def decideDirectionGoToBorder(self,sn):
        #get direction of a head
        dir = self.grid[sn[0]]
        #turn one step right then go down until skane body or border found, then go around the border 
        
    def turnRightIfPossible(self, dir , head):
        
        right_dir =  self.turnRight(dir)
        next_pos =  self.grid[right_dir]
        #if there is empty space or fruit rotate, else go straight: 
        if next_pos == 0 or next_pos == self.fruitn:
            self.grid[right_dir]
            
            
        
    def decide(self):
        dir =  self.grid[self.sn[0]]
        
        
     
      
            
#todo - bot                 
'''

            

            
