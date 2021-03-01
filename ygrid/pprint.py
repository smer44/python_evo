

class PPrint:
    
   
    def __init__(self):
        # problem - pprint does not know 
        #parameters for different symbols.
        #soluton - set the gridcalc:
        """        
        Was:
            self.symbol_table = {0 : '-', 
            -2 : '<',
            2 : '>', 
            5 : '@',
            3 : '#', 
            #self.dim_x_singles:'V',
            #-self.dim_x_singles:'^'
        
            }"""
        self.visit = self.visit_first
    
    #make a method swich:
    def set_print_mode(self, mode = None):
        if mode == "all":
            self.visit = self.visit_all 
        else :
            self.visit = self.visit_first 
        
            
            
        
    def setgrid(self, gridcalc):
        self.gridcalc = gridcalc
        xcelldim =  gridcalc.xcelldim
        xdim = gridcalc.xdim      
        #or you can use  self.dirs field
        self.symbol_table = {0 : '-', 
            -xcelldim : '<',
            xcelldim : '>', 
            5 : '@',
            3 : '#', 
            xdim:'V',
            -xdim:'^'
        
            }        
        
        
    def visit_all(self, grid, ptr, xcelldim):
        cell = grid[ptr:ptr+xcelldim]
        self.msg += str(cell)
    

                    

    
    def visit_first(self, grid, ptr, xcelldim):
        #print('PPrint.visit_first : ' , ptr)
        cell = grid[ptr]
        symbol = self.symbol_table[cell] + ' '
        self.msg += symbol
        
        
    def start_visit(self):
        self.msg = '' 
        
    
    def end_of_dimm(self, dim):
        self.msg+= '\n'
        
        
    def __call__(self):
        self.gridcalc.iter_accept(self)
        print(self.msg)
        
        
            
        
           
    #Problem - we go too much "inside" in the private grid fields
    # soluton - move the iteration over elements to gridcalc
    # and make pprint as a visirot, what makes tostring of each element  
      
"""    def __call__(self, gridcalc, new_line = '\n'):
        xcelldim =  gridcalc.xcelldim
        grid = gridcalc.grid 
        xframe = gridcalc.xframe
        yframe = gridcalc.yframe
        xdim = gridcalc.xdim
        #real_xframe = xframe * xcelldim
        pos = gridcalc.framebegin_pos()
        
        
        assert xcelldim > 0       
        assert grid
        s = ''
        
        if self.all_cell:
            cell_to_str = self.all_in_cell_to_str
        else: 
            cell_to_str = self.first_in_cell_to_str
        
        for y in range(yframe):
            ypos = pos
            for x in range(xframe):
                next_pos = ypos+xcelldim
                #cell = grid[ypos:ypos+xcelldim]
                s += cell_to_str(grid, ypos, xcelldim)
                ypos = next_pos
            pos += xdim  
            s += new_line
        return s """
            
        
     