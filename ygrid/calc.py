def is_in_rechtangle(xpoint,ypoint,xbegin,ybegin,xend,yend):
    return xbegin <= xpoint and xpoint < xend and ybegin <= ypoint and ypoint < yend


class Calc:
    '''
    Provides dimentions and other parameter calculation
    for a grid with some cells,
    also can initialize a grid 
    and calculate a frame in a grid
    the size of a cell over y is 1 (i do not see the reason to have it > 1)
    
    '''
    
    
    def __init__(self,xcells, ycells, xcelldim, border = 1):
        
        self.border = border 
        self.xcells_input = xcells
        self.ycells_input = ycells
        
        self.xcelldim = xcelldim
        #self.ycelldim = ycelldim
        self.grid = None
        self.recalc2d()
        self.dir_str = ["up", "left", "down", "right"]
        
        
     

    def recalc2d(self):
        self.xcells =  self.xcells_input + self.border*2
        self.ycells =  self.ycells_input + self.border*2
        
        self.xdim = self.xcells * self.xcelldim
        self.ydim = self.ycells #* self.ycelldim 
        self.size = self.xdim * self.ydim
        
        self.xhalf = (self.xcells//2 + self.xcells%2) * self.xcelldim
        self.yhalf = (self.ycells//2 + self.ycells%2)# * self.ycelldim
        
        down = self.xdim
        right = self.xcelldim
        
        self.dirs = [ - down, - right, down, right]
        #making a frame to entire window
        self.framedimm(self.xcells, self.ycells)
        
    def ptr(self,xcell,ycell):
        return xcell*self.xcelldim + ycell* self.xdim#*self.ycelldim
    
    def real_1d_to_xy_cell(self, real_pos):
        assert (real_pos % self.xcelldim) == 0
        real_pos = real_pos // self.xcelldim
        return (real_pos % self.xcells) , real_pos//self.xcells
    
    def framedimm(self,xframe, yframe):
        self.xframe = xframe
        self.yframe = yframe
        
        self.xframe_half = self.xframe//2 + self.xframe%2
        self.yframe_half = self.yframe//2 + self.yframe%2
        self.xframe_begin , self.yframe_begin = 0, 0
        self.xframe_end , self.yframe_end = self.xframe , self.yframe
        self.xframe_real_len =  xframe*self.xcelldim
        
    def framebegin_pos(self):
        return self.ptr(self.xframe_begin, self.yframe_begin)

    def frame_end_pos(self):
        return self.ptr(self.xframe_end-1, self.yframe_end-1)
    
    def set_xy(self, x,y, cell_pos, value):
        #assert self.xcelldim == 1 
        assert cell_pos < self.xcelldim , f"set_xy: cell position {cell_pos} is bigger then cell dimention : {self.xcelldim} "
        pos = self.ptr(x,y) + cell_pos
        
        self.grid[pos] = value
        
        
    def focus_xy(self, xcell, ycell):   
        '''
        focuses the frame on the specific position, trying to center it,
        xcell , ycell - position in cell
        
        returns none 
        '''        
        #align frame to max borders:           
        x1 = min(xcell + self.xframe_half, self.xcells ) - self.xframe
        y1 = min(ycell + self.yframe_half, self.ycells ) - self.yframe
        
        #align the frame to minimum borders 
        self.xframe_begin = max(x1,0)
        self.yframe_begin = max(y1,0)  
        
        self.xframe_end = self.xframe_begin + self.xframe     
        self.yframe_end = self.yframe_begin + self.yframe        
          
        
    
    def focus_pos(self, real_pos):
        '''
        focuses the frame on the specific position, trying to center it,
        real_pos - real position in 1d array        
        returns none 
        '''    
        xy = self.real_1d_to_xy_cell(real_pos)
        #align frame to max borders:
        self.focus_xy(*xy)  
        
    
    def newgrid(self, bordercell, emptycell):
        assert len(bordercell) == self.xcelldim , \
        f"GridCalc.newgrid : bordercell  length {len(bordercell)} does not mach the grid cell x-dimention {self.xcelldim}"
        assert len(emptycell) == self.xcelldim , \
        f"GridCalc.newgrid : emptycell  length {len(emptycell)} does not mach the grid cell x-dimention {self.xcelldim}"
       
        
        top_bottom_row = bordercell * self.xcells
        #print("newgrid.top_bottom_row : " , top_bottom_row)
        
        inner_row = bordercell + emptycell * self.xcells_input + bordercell
        
        #print("newgrid.inner_row : " , inner_row)
        
        self.grid =  top_bottom_row + inner_row * self.ycells_input + top_bottom_row
        
        #print("newgrid.self.grid : " , self.grid)


    def backup(self):
        self.grid_backup = self.grid.copy()
        
    def restore(self):
        self.grid = self.grid_backup.copy()            
                

        
    def __str__(self):
        return f"""GridCalc[c_input = {self.xcells_input}, {self.ycells_input} 
            b = {self.border }, 
            cells = {self.xcells}, {self.ycells}
            dim = {self.xdim}, {self.ydim}
            halfs = {self.xhalf}, {self.yhalf}
            frame = {self.xframe}, {self.yframe}
            xframe_real_len = {self.xframe_real_len}
            frame_half = {self.xframe_half}, {self.yframe_half}
            frame_begin = {self.xframe_begin}, {self.yframe_begin}
            frame_end = {self.xframe_end}, {self.yframe_end}
            grid created= {not not self.grid}
            dir_str = {self.dir_str}
            dirs = {self.dirs}
            """    
    def info_focus(self):
            return f"""
            frame_begin = {self.xframe_begin}, {self.yframe_begin}
            frame_end = {self.xframe_end}, {self.yframe_end}
            xframe_real_len = {self.xframe_real_len}
            """
            
    def check_line(self, xstart, ystart,  dir, sn_len): 
        return self.check_line_in(xstart, ystart,0,0,self.xcells, self.ycells, dir,sn_len)
     
        
            
    def check_line_in(self, xstart, ystart, x0,y0, x1, y1,  dir, sn_len): 
        border = self.border 
        xcells = self.xcells
        ycells = self.ycells
        
        x0 = max(x0, border)    
        y0 = max(y0, border)     
        
        x1 = min(x1, xcells - border)
        y1 = min(y1, ycells - border)
        
        if not is_in_rechtangle(xstart, ystart, x0,y0, x1, y1):
            print("Calc.check_line : wrong start point is out of bounds : " ,  xstart, ystart)
            return False
        
        
        if (dir < 0 or dir > 3):
            print("Calc.check_line : wrong direction, must be 0..3 : " , dir)
            return False    
            
        if (sn_len <1):# snake length of  and less has no sence:
            print("check_new_snake : snake length too low and has no sence: " , sn_len)
            return False   
        
        sn_len -=1
        
        good = True
        
        if dir < 2:
            if dir == 0:#up
                yend = ystart-sn_len
                good =  y0 <= yend 
            else:  #left
                xend = xstart-sn_len
                good =  x0 <= xend 
        else: 
            if dir == 2:#down
                yend = ystart+sn_len
                good =  yend < y1
            else :#right :
                xend = xstart+sn_len
                good =   xend < x1                    
        if not good:
            print("check_new_snake : length in direction: ", self.dir_str[dir] , ", too big, end point out of bounds"  )   
        return good         



    def iter_accept(self, visitor):
        visitor.start_visit()
        xcelldim =  self.xcelldim
        grid = self.grid 
        xframe = self.xframe
        yframe = self.yframe
        xdim = self.xdim
        #real_xframe = xframe * xcelldim
        ptr_begin = self.framebegin_pos()            
        ptr_end = self.frame_end_pos()
        row_len = self.xframe_real_len
               
        assert xcelldim > 0       
        assert grid
        
        for row_begin in range(ptr_begin, ptr_end, xdim):
            #print('Calc.iter_accept : row_begin : ' , row_begin, ' ptr_end :  ' , ptr_end)
            for ptr in range(row_begin, row_begin+row_len, xcelldim):
                visitor.visit(grid, ptr, xcelldim)
            visitor.end_of_dimm(0)
            
            
            
    