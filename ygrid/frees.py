import random


class Frees :
    
    
    def __init__(self, gridcalc):
        self.cell_frees_position = 1
        
        self.gridcalc = gridcalc 
    
    def backup(self):
        self.frees_backup = self.frees.copy()
        
    def restore(self):
        self.frees = self.frees_backup.copy()
        

        
    
    def new(self):
        xdim = self.gridcalc.xdim
        size = self.gridcalc.size
        xcelldim = self.gridcalc.xcelldim
        grid = self.gridcalc.grid        
        border = 0#gridcalc.border
        
        y_border = border*xdim
        x_border = border*xcelldim
        
        cell_frees_position = self.cell_frees_position
        
        self.frees = []
        
        for row_begin in range(y_border, size - y_border, xdim):
            #row_begin = y*self.dim_x_singles
            #print("reset_free_indexes : row_begin : " , row_begin)
            for cell_index in range(row_begin + x_border, row_begin+xdim - x_border,xcelldim ):
                #print("reset_free_indexes : cell_index : " , cell_index)
                cell = grid[cell_index]
                if not cell:
                    pos = cell_index+cell_frees_position
                    val = len(self.frees)
                    #print("reset_free_indexes : assign to position " ,pos, "val" , val)
                    grid[cell_index+cell_frees_position] = len(self.frees)
                    self.frees.append(cell_index) 
                else:
                    grid[cell_index+cell_frees_position] = -1
                      
        #print("reset_free_indexes :  grid" , grid)
                    
    def __str__(self):
        return f"Frees:{self.frees}"     
    
    def checkfrees(self):  
        grid = self.gridcalc.grid
        for index in self.frees:
            if grid[index]:
                print("Frees.checkfrees : non free index entry in frees: " , index)
                return False
        #print("checkfrees : ok")  
        return True
        
    def check(self):
        grid = self.gridcalc.grid
        xcelldim = self.gridcalc.xcelldim
        cell_frees_position = self.cell_frees_position
        
        for cell_id in range(0,len(grid),xcelldim):
            value = grid[cell_id]
            free_flag = grid[cell_id+cell_frees_position] 
            if value:
                if( free_flag != -1):
                    print(f"Frees.check : free_flag of not free cell {cell_id} is {grid[cell_id:cell_id +xcelldim]} must be -1")
                    return False  
            else:
                if not ( 0 <= free_flag and free_flag < len(self.frees)):
                    print(f"Frees.check : free_flag of  free element is not in range (0, {len(self.frees)}) but is  :  {free_flag}")
                    return False 
                                
                if ( self.frees[free_flag] != cell_id):
                    print(f"Frees.check : self.frees[{free_flag}] is {self.frees[free_flag] }, does not points to the cell  {cell_id}")
                    return False  
                
        #print("checkunfrees : ok") 
        return True    
    
    def unfree(self, cell_ptr):
        '''
        permanently delete the cell from free cell index 
        glue the free indexes by moving the last frees element 
        to deleted position
        frees : ABCD -> AxCD -> ADC   
        
        '''
        gridcalc = self.gridcalc
        grid = gridcalc.grid
        
        grid = gridcalc.grid
        cell_frees_position = self.cell_frees_position
        cell_fees_ptr = cell_ptr+cell_frees_position
        
        #get the position of a grid free cell , in a frees array:
        unfree_index = grid[cell_fees_ptr]
        #mark the cell in grid to be busy:
        grid[cell_fees_ptr] = -1 
        #remove the last free position from frees array:
        last_free_pos = self.frees.pop()
        
        if last_free_pos == cell_ptr:
            #we just deleted the last frees entry, do further nothing
            return  
        
        #mark 
        grid[last_free_pos + cell_frees_position] = unfree_index
        
        self.frees[unfree_index] = last_free_pos
        
    def changefree(self, cell_ptr_free, cell_ptr_not_free):
        
        fr_pos = self.cell_frees_position
        ptr_from = cell_ptr_free+ fr_pos
        ptr_to = cell_ptr_not_free+fr_pos
        grid = self.gridcalc.grid
        
        free_id_from = grid[ptr_from]
        free_id_to = grid[ptr_to]# must be -1 # check
        
        assert free_id_to == -1, \
        f"Frees.changefree : cell_ptr_not_free is free, is a free cell: {grid[cell_ptr_not_free:cell_ptr_not_free+ self.gridcalc.xcelldim]} "
        self.frees[free_id_from] = cell_ptr_not_free               
        
        grid[ptr_to] = free_id_from
        grid[ptr_from] = free_id_to
         
    def random_unfree(self):
        ptr = random.choice(self.frees)
        self.unfree(ptr)
        return ptr
        