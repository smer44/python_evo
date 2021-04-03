'''
from 
https://www.udemy.com/course/python-gui-programming-with-tkinter-build-10-gui-projects/learn/lecture/25396424#overview
'''

from tkinter import * 


root = Tk()

root.title('First Gui ')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

xsize = 500
ysize = 500

xcoord = screen_width- xsize-50
ycoord = screen_height- ysize-50

#set size:500x500 position: +0+0
#root.geometry(f'500x500+0+000')

root.geometry(f'{xsize}x{ysize}+{xcoord}+{ycoord}')

#labels:

mylabel = Label(text = f"Resoluton : {screen_width}:{screen_height}", fg = 'cyan', bg = 'gray')

pack_return = mylabel.pack()

mylabel = Label(text = f"mylabel.pack() returned : {pack_return}", fg = 'green', bg ='black')
mylabel.pack()


# how to change label posiitions:

inner_root = Frame(root,
                   width=200, height=200, 
                   background="bisque" )
inner_root.pack()

mylabel = Label(inner_root,text = f"placed label inside a frame is nvisible if frame size is not set")
#mylabel.pack()
mylabel.place(x = 100,y = 100)# 0,0 is top left corner 

Label(inner_root,text = 'second label').place(x= 100, y = 130)


# how to use grid:
3
inner_root = Frame(root,
                   width=200, height=200, 
                   background="yellow" )
inner_root.pack()

#sticky is alignment of a cell:

Label(inner_root,text = '0x1@E', bg = 'cyan').grid(row = 0 , column = 1,sticky = 'E')
Label(inner_root,text = '     1x1       ', bg = 'green').grid(row = 1 , column = 1)
Label(inner_root,text = '     1x0       ', bg = 'red').grid(row = 1 , column = 0)
Label(inner_root,text = '2x1@W', bg = 'cyan').grid(row = 2 , column = 1,sticky = 'W')


#how to add a button nad set colors:

counter = 0
but1 = Button(text = f'Submit:{counter}', fg = 'green', activeforeground='#4444ff', activebackground='black')
but1.pack()

#how to add function to a button:

def click():
    global counter
    global txt
    counter += 1
    but1.configure(text = f'Submit:{counter}')
    Label(text = f'{txt.get()},Submit:{counter}' ,font = 20).pack()

but1.configure(command = click)    

#how to cerate textbox:
#ahh, you can not pack avoe previous, but you can choose inside the 

txt = StringVar(root, value='default text') 



#how to set actions on text change:


def click_enter(event):
    #event has a state,keysym = <Return>, keycode, char , x , y (of mouse, relative to object) 
    global txt 
    Label(text = f'clicked enter: {txt.get()}, event: {event}' ,font = 20, bg='red').pack()
    

#how to create multple guis:
root1 = Tk()


mytext = Entry(root1, textvariable = txt)
mytext.pack(side='right')

mytext.bind('<Return>', click_enter)

root.mainloop()
root1.mainloop()






