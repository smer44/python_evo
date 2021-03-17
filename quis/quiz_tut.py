import tkinter as tk
import tkinter.font as font

class  Quis:    
    
    
    def __init__(self, data):
        
        self.window = tk.Tk() 
        self.data= data      
        self.correct_answers = 0 
          
        self.myFont = font.Font(family='Helvetica', size = 20)
        
        
        self.question = tk.Label(text="--- questions loading ---" , font = self.myFont)
        self.question.pack()
        
        self.answers = tk.Listbox( font = self.myFont)
        self.answers.pack()               

        self.confirm_button =  tk.Button(text = 'Select', command = self.select_variant, font = self.myFont)
        self.confirm_button.pack()
        
        self.counter_lbl = tk.Label(text="Correct answers : 0 " ,  font = self.myFont)
        self.counter_lbl.pack()
    
    def finish_and_show_results(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        
        self.result_label = tk.Label(text=
                                     f"""Congratulations !!! 
                                     question solved : {self.correct_answers}  
                                     corret answers = {int(self.correct_answers / len(self.data) * 100)}%"""  
                                     , font = self.myFont) 
        self.result_label.pack()
        
    def select_variant_show(self):
       
        
        sel = self.answers.curselection()
        
        print(f'sel = {sel}')
        
        if sel:
            print(f'answer: { self.answers.get(sel)}')        
        
    
    def select_variant(self):
        #Listbox.curselection =(0)
        sel = self.answers.curselection()
        if sel:
            
            if sel[0] == self.correct:
                self.correct_answers+=1              
                self.counter_lbl.config(text = "Correct answers : " + str(self.correct_answers))

            self.current_question+=1
            if (self.current_question >= len(self.data)):
                self.finish_and_show_results()
            else:            
                self.update_question()                

    def start(self):
        self.current_question = 0
        self.update_question()
        self.window.mainloop()
    
    def update_question(self):
        question, answers , self.correct = self.data[self.current_question ]
        self.question.config(text=str(question))   

        #self.answers.destroy() # deletes all elements   
        self.answers.delete(0,tk.END)
        for answ in answers:
            self.answers.insert(tk.END,answ)
 
data = [ ['what is your cat name?', ['alice' , ' bob' , 'i have no cat' , 'charlie'], 2]  ,
        ['what programming language do you prefer?', ['Python' , ' Jacascript' , 'C++'],0] ,
        ['what mashine learning method i use to train the snake?', ['neural network' , 'ecolutionary algo', ' markov chain' ], 1] , 
        ['on the chess turnier with n participants, each player plays 3 games with each other player. How many games will be played?', 
         ['3/2n!' , '3*n!/(n+1)/2', ' 3*n(n-1)/2' ], 2] ,         
        ]
  
q = Quis(data)

q.start()
