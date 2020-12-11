import random as r

   

class GameController:
    
    
    def __init__(self, dim_x, dim_y):
        

        
        self.fruitn = 5
        
        
        self.deaths = []
        self.snakes = []
        self.fintesses = []
        
        self.reset_grid(dim_x, dim_y)
        
        print('__init__')
        
    
    def reset_grid(self,dim_x, dim_y):
        self.dim_x_pairs = dim_x+2
        self.dim_x_singles = self.dim_x_pairs * 2 
        self.dim_y = dim_y+2
        
        #self.dimall_pairs =  self.dim_x * self.dim_y
        
        self.displays = {0 : ' ', 
                    -2 : '<',
                    2 : '>', 
                    self.fruitn : '@',
                    3 : 'x', 
                    self.dim_x_singles:'V',
                    -self.dim_x_singles:'^'
        
                    }
     

        
        border_row = [3,-1] * self.dim_x_pairs
        
        inner_row = [3,-1] + [0,0] * dim_x + [3,-1]
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
        
        
    def new_random_fruit(self):
        fruit_index = r.choice(self.frees) 
        self.grid[fruit_index] = self.fruitn
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
            
        
        sn = [tail + (size-1)*dir, tail]
        self.snakes.append(sn) # snake = [head, tail]
        self.fintesses.append(0)
        #self.loosers.append(0)
        
        
    def create_first_snake(self):
        dir = - self.dim_x_singles
        self.create_snake(6, 6, dir, 3)

    def reset_session(self):
        self.reset_grid(self.dim_x_pairs -2 , self.dim_y-2)
        self.snakes = []
        self.create_first_snake()
        self.new_random_fruit()
        
    
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

        
    

        
    
    def new_fruit(self,x,y):
        self.grid[y *  self.dim_x + x] = self.fruitn 
            

        
    def is_inbounds(self, x):
        return 0 <= x and x < self.dimall and x  % self.dim_x
        
        #return 0 <= x and x <  self.dim_x  and 0 <= y and y < self.dim_y  
    

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
                #and create new fruit:
                self.new_random_fruit()
                self.fintesses[index] += 1000

            else:
                #there is a collision:
                self.loosers.append(index)
                self.fintesses[index] =0
                
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
        self.checkloosers()
                
    def checkloosers(self):
        if self.loosers:
            #for unit in self.loosers:
            #    unit.deaths +=1
            self.reset_session()
            print("session reseted")
            

    
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
        
    def toTextArea(self):
        s = ""

        
        for n in range(0,len(self.grid),2):
            
            if not (n % self.dim_x_singles):
                s+="\n"
            
            symbol = self.displays[self.grid[n]]
            s += '|' + symbol + '|'
 
      
        
               
        return s
        
        
        
    
    
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


            

            
