import tkinter as tk
import tkinter.font as font
from tkinter import messagebox

"""
how to make multple windows :
window = tk.Tk() 
window2 = tk.Tk()

window.mainloop()
window2.mainloop()

https://www.python-kurs.eu/tkinter_textfelder.php

"""


class  QuisCreator(tk.Tk):
    
    basic_rows =  3
    def __init__(self):
        super().__init__() 
        self.title("QuisCreator")
        self.data_path = ".\quiz_data"
        
        self.myFont = font.Font(family='Comic Sans MS', size = 14)
        
        tk.Label(text="Question:" , font = self.myFont).grid(row=0,column=0)   
        
        current_question = tk.Text(self, height=5, width=60)
        current_question.insert(tk.END, "")
        #current_question.pack()
        current_question.grid(row=0,column=1)  
        self.current_question= current_question
        
        
        tk.Label(text="Correct variant:" , font = self.myFont).grid(row=1,column=0)  
        correct_variant = tk.Text(self, height=1, width=60)
        correct_variant.grid(row=1,column=1)  
        self.correct_variant =  correct_variant
        
        
        add_variant_button =  tk.Button(text = 'Add variant', command = self.add_variant, font = self.myFont)
        #add_variant_button.pack()      
        add_variant_button.grid(row=2,column=1) 
        self.add_variant_button= add_variant_button  
        
        remove_variant_button =  tk.Button(text = 'Save question', command = self.save_question, font = self.myFont)
        #remove_variant_button.pack()  
        remove_variant_button.grid(row=2,column=0)     
        self.remove_variant_button= remove_variant_button        
          
        self.answers = []
        self.remove_buttons= []
        self.variants= []
        
        self.add_del_log = []
        self.data = []
        self.load_data()
        self.load_question()
    # i have done log to debug it 
    def add_variant(self):
        
        pos = len(self.answers)
        self.add_del_log.append(('add', pos)) 
        print(f'add_del_log : {self.add_del_log}')
        #print(f"len(self.variant_texts) , {len(self.variant_texts)}")
        new_answer = tk.Text(self, height=2, width=60)
        
        #new_variant.pack()  
        
        row_pos = self.basic_rows + pos
        new_answer.insert(tk.END, str(pos))
        new_answer.grid(row=row_pos, column=1)  
        #print(f"gridsize: " , self.grid_size() ) 
        
        remove_button = tk.Button(text = 'Remove ', 
                                  command = lambda : self.remove_variant(pos), font = self.myFont)
        remove_button.grid(row=row_pos, column=0)  
           
        
        self.answers.append(new_answer)
        self.remove_buttons.append(remove_button)
        self.variants.append((remove_button, new_answer))
        
        
    def remove_variant_wrong(self, pos):
        #aha, i must always delete the last remove button !!!!
        self.add_del_log.append(('del', pos)) 
        print(f'add_del_log : {self.add_del_log}')  
        #new_variant.destroy()
        remove_button,new_variant = self.variant_texts.pop(pos)
        #print(f'remove_variant; len after destroy: {len(self.variant_texts)} ')
        remove_button.destroy()
        new_variant.destroy()
        #print(f"remove_variant after: , {len(self.variant_texts)}")
        #update further variants: 
        for i , (next_button, next_variant) in enumerate(self.variant_texts[pos:]):
            pp = 3+ pos+i
            #print(f'remove_variant; set to the position , {pp}')
            next_button.grid(row=3+ pos+i,column=0) 
            next_variant.grid(row=3+ pos+i,column=1) 
           
    def remove_variant(self, pos):   
        self.add_del_log.append(('del', pos)) 
        print(f'add_del_log : {self.add_del_log}')  
        
        remove_button = self.remove_buttons.pop()
        answer_to_remove = self.answers.pop(pos)
        
        answer_to_remove.destroy()
        remove_button.destroy()
        
        for i , answer in enumerate(self.answers[pos:]):
            row_ptr = 3+ pos+i
            #print(f'remove_variant; set to the position , {pp}')
            #and do not update buttons:
            #next_button.grid(row=3+ pos+i,column=0) 
            answer.grid(row=row_ptr,column=1)         
        
    def load_question(self):
        image, txt, answers, correct_answer_nr = self.data[self.current_quesion]
        
        #ignore image first 
        self.current_question.delete('1.0', tk.END)
        self.current_question.insert(tk.END, txt)
        for answer in answers:
            self.add_variant()
            answer_field = self.answers[-1]
            answer_field.delete('1.0', tk.END)
            answer_field.insert('1.0', answer)
            
        self.correct_variant.delete('1.0', tk.END)    
        self.correct_variant.insert('1.0', correct_answer_nr)
             

    def save_question(self):
        '''
        creates a array - question with fields :
        [image, queston text , [variants] , correct variant] 
        
        '''
        image = None 
        
        #also, new line and other symbols escape:
        
        txt = self.current_question.get('1.0',tk.END).strip()
       
        if not txt:
            messagebox.showerror("Wrong question", "Question text field must not be empty")
            return 
            
        
        answers = [answer.get('1.0',tk.END).strip()  for answer in self.answers  ]
        if not answers or len(answers) < 2:
            messagebox.showerror("Wrong question", "there must be  at least 2 answers ")
            return         
        
        correct_answer_nr = self.correct_variant.get('1.0',tk.END).strip()
        
        if not correct_answer_nr:
            messagebox.showerror("Wrong question", "Correct answer number must not be empty")
            return 
            
        #correct_answer_nr = int(correct_answer_nr)    
        try:
            correct_answer_nr = int(correct_answer_nr)
        except ValueError:
            messagebox.showerror("Wrong question", "Correct answer number must be a integer digit")
            return 
        
        if (correct_answer_nr < 0 or correct_answer_nr >= len(answers)):
            messagebox.showerror("Wrong question", f"Correct answer number ut of bounds, mut be between 0 and {len(answers)}")
            return 
    
        
        #print(f'Quesion : {txt} \n answers : {answers} , correct_answer_nr : {correct_answer_nr}')
        question = [image, txt, answers, correct_answer_nr]
        #return queston
        print(f'save_question : {question}')
        self.data[self.current_quesion] = question
        print(f'save_question :  data: {self.data}')
        
    def save_data(self):
        pass
        
          
    def load_data(self):
        try: 
            f = open(self.data_path, "r+")
            print(f"load_data : opened existing data file {self.data_path}")
            line = f.readline()
            while line:
                image = line.strip()
                line = f.readline()
                
                txt = line.strip()
                line = f.readline()
                
                answers = line.strip().split()
                line = f.readline()
                
                correct_answer_nr = line.strip()
                correct_answer_nr = int(correct_answer_nr)
                line = f.readline()
                
                self.data.append( (image, txt, answers, correct_answer_nr))
        except FileNotFoundError:
            f = open(self.data_path, "x")        
            print(f"load_data : create new data file {self.data_path}")
        
        if not self.data:
            empty_quesion = ['', 'empty quesion', ['boo'].copy(), '42'  ]
            self.data = [empty_quesion]
            print(f"load_data : self.data  is empty, create new empty question ")
            
        self.current_quesion = 0
        print(f'load_data :  self.data loaded : {self.data}')    
            
        

q = QuisCreator()

q.mainloop()