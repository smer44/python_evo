

from tkinter import Tk, Label
root=Tk()
w=Label(root,text="Key Waiting:")
w.place(x=70,y=90)

'''
#not very good example:
def key_pressed(event):
    w=Label(root,text="Key Pressed:"+ repr(event.char))
    w.place(x=70,y=90)
'''
    
def key_pressed_up(event):
    w.configure(text="key_pressed_up")
    
def key_pressed(event):
    w.configure(text="key_pressed:" + str(event.char))

    
def key_pressed_down(event):
    w.configure(text="key_pressed_down")
    
def key_pressed_left(event):
    w.configure(text="key_pressed_left")
    
def key_pressed_right(event):
    w.configure(text="key_pressed_right")
    
    
    
root.bind("<Key>",key_pressed)

root.bind("<Up>",key_pressed_up)
root.bind("<Down>",key_pressed_down)
root.bind("<Left>",key_pressed_left)
root.bind("<Right>",key_pressed_right)


root.mainloop()

