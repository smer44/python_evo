from tkinter import * 
import tkinter.messagebox

root = Tk()

root.title('Nemu tutorial')

menu = Menu()

root.config(menu = menu)

#root menu items:
cascades = [('File', ['new' , 'open', 'save' , 'close']), ('Edit', ['copy' , 'paste' , 'select']),  ('Tools', ['Show' , 'Calc'])  ]

def gui():
    gu = Tk()
    gu.title('New project')
    gu.mainloop()
    
def  save():
    Label(text = 'saved').pack()
    
    
def mbox():
    tkinter.messagebox.showinfo('mbox', 'tkinter.messagebox.showinfo')
    
def mclose():    
    result = tkinter.messagebox.askquestion('mclose', 'Want to close?')
    #result is either 'yes or 'no'
    Label(text = f' tkinter.messagebox.askquestion returned {result}').pack()
    if result =='yes':
        print('ended with root.destroy()')
        root.destroy()
    
menu_map = {'new': gui ,'save' : save, 'Show' : mbox, 'close' : mclose}

for cas, coms in cascades:
    
    #how to add inner items: 
    inner_menu = Menu()
    menu.add_cascade(label = cas, menu = inner_menu)
    print(coms)
    for com in coms:
        inner_menu.add_command(label = com, command = menu_map.get(com, None))





root.mainloop()