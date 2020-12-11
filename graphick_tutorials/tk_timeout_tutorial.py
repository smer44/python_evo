#https://www.python-kurs.eu/tkinter_labels.php
#Unter Python3 muss man Tkinter klein schreiben, also "from tkinter import *":


#from https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter

import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.counter = 0
        self.label = tk.Label(text="" + str(self.counter))
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        self.counter += 1
        now = time.strftime("%H:%M:%S") + " " + str(self.counter)
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()