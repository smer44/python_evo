import tkinter as tk
import tkinter.font as tkfont

# TOFO - ok, there is a bug:
from gameobjs import *

fontname = 'Consolas' # "Segoi UI" # 'Times New Roman'



class GameDisplayer():
    def __init__(self, gc):
#
        
        self.root = tk.Tk()#
        
        myFont = tkfont.Font(family=fontname, size= 20)#family=fontname,
        self.score_label = tk.Label(text="score", font=myFont)        
        self.score_label.pack()           
        
        
        self.label = tk.Label(text="Start", font=myFont)        
        self.label.pack()   
        
        
        
        self.setgc(gc)     
        #self.counter = 0
        self.update_clock()
        self.root.mainloop()

        

    def update_clock(self):
        #self.counter +=1
        #print(self.counter, self.gc.snakes[0])
        
        self.gc.move_all()
        self.score_label.configure(text= "Fitness : " + str(self.gc.fintesses[0]))
        #11: change totextarea
        #self.label.configure(text=str(self.gc.toTextArea()))
        self.label.configure(text=str(self.gc.toTextAreaHead(10,10)))
        self.root.after(500, self.update_clock)
        
    #key binding must be executed before tk loop    
    def setgc(self,gc):
        self.gc = gc 
        self.root.bind("<Up>",lambda event : gc.turn_first_up(), self.label.configure(text=str(self.gc.toTextArea())))
        self.root.bind("<Down>",lambda event : gc.turn_first_down())
        self.root.bind("<Left>",lambda event : gc.turn_first_left())
        self.root.bind("<Right>",lambda event : gc.turn_first_right())
        
        #TypeError: turn_first_right() takes 1 positional argument but 2 were given
        # if self.root.bind("<Right>",gc.turn_first_right)
        
        
    
#10: change game size 
gc = GameController(20,20)

GameController.reset_session(gc)
#gc.reset_session()

        
gd = GameDisplayer(gc)

#wrong, session is already destroyed:
'''
gd.root.bind("<Up>",gc.turn_first_up)
gd.root.bind("<Down>",gc.turn_first_down)
gd.root.bind("<Left>",gc.turn_first_left)
gd.root.bind("<Right>",gc.turn_first_right)
'''

