
# it is sort of game controller then

class SnakeActors:
    
    def __init__(self, gridcalc,gcnn, frees):
        
        self.snakes = []
        self.deaths = []
        self.fintesses = []
        self.start_variants = []
        self.frees = frees 
        
        self.fitness_per_move = 1
        self.initial_fitness = 0#50
        self.fruitn = 5# ir import that from options 
        self.game_runs = True
        self.loosers = []
        
        assert gridcalc.xcelldim == 2,\
        f'SnakeActors. __init__: gridcalc must have xcelldim 2 but has {gridcalc.xcelldim}'
        
        self.gridcalc = gridcalc   
        gridcalc.backup()
        
        assert gcnn.xcelldim == 3,\
        f'SnakeActors. __init__:  gcnn  must have xcelldim 3but has {gcnn.xcelldim}'
        self.gcnn = gcnn
        gcnn.backup()
        
        frees.gridcalc = gridcalc
        frees.new()
        frees.backup()
        self.fintesses = []
        self.fitness_per_move = 1

    #move to gridmap - check if the line is in some rechtangle 
    

    def reset(self):
        self.gridcalc.restore()
        self.gcnn.restore()
        self.frees.restore()
        for n in range(len(self.start_variants)):
            self.create_snake(n) 
        
    # dir = [up, left, down,right]
    # check line and init snake
    #also init random snake in the some half or a frame:
    
    def set_snake_start(self, xstart,ystart, dir, sn_len):
        
        assert self.gridcalc.check_line(xstart,ystart, dir, sn_len),\
            f"SnakeActor.set_snake_start : wrong parameters ({xstart},{ystart}, {dir}, {sn_len})"
            
        gc_dir = self.gridcalc.dirs[dir]
        gcnn_dir = self.gcnn.dirs[dir]
        self.start_variants.append((xstart,ystart, gc_dir,gcnn_dir,sn_len))
        
        print(f"SnakeActor.set_snake_start succesfull stored:  (xstart = {xstart},ystart = {ystart}, gc_dir = {gc_dir},gcnn_dir = {gcnn_dir}, sn_len = {sn_len} )")


    def create_snake(self, snake_start_variant):
        xstart, ystart, step_gc, step_gcnn, sn_len = self.start_variants[snake_start_variant]
        
        gc = self.gridcalc
        gcnn = self.gcnn
        fr = self.frees
        
        ptr_gc = gc.ptr(xstart, ystart)
        ptr_gcnn = gcnn.ptr(xstart, ystart)
        
        gc_tail_ptr = ptr_gc
        gcnn_tail_ptr = ptr_gcnn
        
        for _ in range(sn_len-1):
            fr.unfree(ptr_gc)
            gc.grid[ptr_gc] = step_gc
            gcnn.grid[ptr_gcnn:ptr_gcnn+3] =[1,0,0]#body part
            ptr_gc+=step_gc
            ptr_gcnn+=step_gcnn
           
        fr.unfree(ptr_gc)    
        gc.grid[ptr_gc] = step_gc
        gcnn.grid[ptr_gcnn:ptr_gcnn+3] =[0,0,1] # head       
        
        #snake entry will have :gc_head_ptr, gcnn_head_ptr, gc_tail_ptr, gcnn_tail_ptr
        self.snakes.append((ptr_gc, ptr_gcnn, gc_tail_ptr, gcnn_tail_ptr ))  
        self.fintesses.append(0)

    def new_random_object(self, value):
        ptr = self.fr.random_unfree()
        self.gc.grid[ptr] = value

         
            
    def move_snake(self, snake_nr):  
        '''
        Very big method, any ideas how to refactor that?
        If it is so messy, it is an indicator that you should 
        move the functionality, maybe particulaty in other class,
        gridcalc for example
        
        '''      
        #get the head and tail pointers of the snake:
        head_ptr_gc, head_ptr_gcnn, tail_ptr_gc, tail_ptr_gcnn = self.snakes[snake_nr]
        grid = self.gridcalc.grid
        gcnn = self.gcnn.grid
        #get direction of the head from gridcalc
        dir_head = grid[head_ptr_gc]
        #       
        next_pos = head_ptr_gc + dir_head 
        
        gcnn_next_pos = next_pos//2*3 
        
        # we do not need to check in bounds,
        #because arena is bordered by obstacles
        #next_value can be empty, fruit or obstakle  
        next_value = grid[next_pos]   
        
        if next_value:
            #if next cell is not empty 
            if next_value == self.fruitn:
                #if the fruit is eaten:
                # just put the head forwards,
                # this will increace the length.
                #Mark in gcnn old position as 
                #snake body and new position as snake head
                grid[next_pos] = dir_head
                
                #mark last head as obstacle:
                gcnn[head_ptr_gcnn:head_ptr_gcnn+3] =[1,0,0]
                #mark new position as head:
                gcnn[gcnn_next_pos:gcnn_next_pos+3] =[0,0,1]
                # do not update frees, since a fruit is already unfreed 
                self.fintesses[snake_nr] += 1000

                #put new fruit:
                fruit_index = self.new_random_object(self.fruitn)
                
                #set updated stake entry:
                self.snakes[snake_nr] = next_pos,  gcnn_next_pos , tail_ptr_gc, tail_ptr_gcnn  

            else :
                #crash 
                self.loosers.append(snake_nr)
                self.game_runs = False 
        else:
            #move to the next position
            #get direction of a tail:
            dir_tail = grid[tail_ptr_gc]
            
            #erace tail:
            grid[tail_ptr_gc] = 0
            
            # set new head :
            grid[next_pos] = dir_head           
            
            #erace tail in gcnn:
            gcnn[tail_ptr_gcnn:tail_ptr_gcnn+3] =[0,0,0]
            
            #set body part on previous head:
            gcnn[head_ptr_gcnn:head_ptr_gcnn+3] =[1,0,0]
            
            #set  head on prev_empty:
            gcnn[gcnn_next_pos:gcnn_next_pos+3] =[0,0,1]
            
            #mark next_pos unfree and tail_ptr_gc free 
            self.frees.changefree(next_pos, tail_ptr_gc)
            
            self.fintesses[snake_nr] += self.fitness_per_move

            #set updated stake entry:
            self.snakes[snake_nr] = next_pos,  gcnn_next_pos , tail_ptr_gc, tail_ptr_gcnn             
            

    def move_all(self):
        
        #print("move_all")
        for snake_nr in range(len(self.snakes)):
            self.move_snake(snake_nr)
        return not  self.loosers           
            
                
    def turn_snake(self, snake_nr, dir):        
        head_ptr_gc,  head_ptr_gcnn , tail_ptr_gc, tail_ptr_gcnn = self.snakes[snake_nr]
        grid = self.gridcalc.grid
        #get direction of the head from gridcalc
        dir_head = grid[head_ptr_gc]
        #refactor - how move it to gridcalc
        new_dir = self.gridcalc.dirs[dir]  
        
        grid[head_ptr_gc] = new_dir
        print("ysnake: turn_snake : old_dir : " , dir_head , "new_dir : " , new_dir)  
        
        
    