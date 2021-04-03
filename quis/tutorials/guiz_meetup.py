
import tkinter as tk

import tkinter.font as font

class QuizDisplay(tk.Tk):
    
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        self.myFont = font.Font(family='Helvetica', size = 20)
         
        self.question = tk.Label(self, text="--- questions loading ---" , font = self.myFont)
        self.question.pack()
        
        self.answers = tk.Listbox(self, font = self.myFont)
        self.answers.pack()    
        
        self.confirm_button =  tk.Button(self, text = 'Select', command = self.select_variant, font = self.myFont)
        self.confirm_button.pack()    
    
    def set_data(self,data):
        self.data = data 
        self.correct_answers = 0 
        self.current_question = 0
        
        self.set_quesion()
    
    
    def set_quesion(self):
        
        question, answers , self.correct = self.data[self.current_question]
        self.question.config(text=str(question)) 
         
        self.answers.delete(0,tk.END)
        
        for answ in answers:
            #print(answ)
            self.answers.insert(tk.END,answ)       
        



    def  finish_and_show_results(self):
        print("self.correct_answers:" , self.correct_answers) 
        for widget in self.winfo_children():      
            widget.destroy()
    
        msg =  f"""Congratulations !!! 
                question solved : {self.correct_answers}  
                corret answers = {int(self.correct_answers / len(self.data) * 100)}%"""     
            
             
        self.result_label = tk.Label(text=msg , font = self.myFont)        
        self.result_label.pack()    
    
    
    def select_variant(self):
        sel = self.answers.curselection()
        if sel:
            assert len(sel) == 1
            if sel[0] == self.correct:
                self.correct_answers+=1
                #self.counter_lbl.config(text = "Correct answers : " + str(self.correct_answers))   
            self.current_question+=1
            if (self.current_question >= len(self.data)):
                self.finish_and_show_results()
            else:
                self.set_quesion()

data = [ ['what is your cat name?', ['alice' , ' bob' , 'i have no cat' , 'charlie'], 2]  ,
        ['what programming language do you prefer?', ['Python' , ' Jacascript' , 'C++'],0] ,
        ['what mashine learning method i use to train the snake?', ['neural network' , 'ecolutionary algo', ' markov chain' ], 1] , 
        ['on the chess turnier with n participants, each player plays 3 games with each other player. How many games will be played?', 
         ['3/2n!' , '3*n!/(n+1)/2', ' 3*n(n-1)/2' ], 2] ,         
        ]        
         
q= QuizDisplay()

q.set_data(data)

q.mainloop()
        
        




        

        
        