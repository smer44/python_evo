'''
Created on 12.03.2021
from https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame 
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_window.html

'''
from  tkinter import *   # from x import * is bad practice
#from ttk import *

# http://tkinter.unpythonic.net/wiki/VerticalScrolledFrame

class VerticalScrolledFrame(Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)            

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = Frame(canvas)
        
        #Use window=w where w is the widget you want to place onto the canvas. 
        #If this is omitted initially, you can later call 
        #C.itemconfigure (id, window=w) to place the widget w onto 
        #the canvas, where id is the window's object ID.
        #anchor: The default is anchor=tk.CENTER, meaning that 
        #the window is centered on the (x, y) position
        interior_id = canvas.create_window(0, 0, window=interior,  anchor=NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


if __name__ == "__main__":

    class SampleApp(Tk):
        def __init__(self, *args, **kwargs):
            root = Tk.__init__(self, *args, **kwargs)
            

            self.frame = VerticalScrolledFrame(root)
            self.frame.pack()

            buttons = []
            for i in range(10):
                buttons.append(Button(self.frame.interior, text="Button " + str(i)))
                buttons[-1].pack()
            self.label = Label(self.frame.interior,text="Shrink the window to activate the scrollbar.")
            self.label.pack()            

    app = SampleApp()
    app.mainloop()