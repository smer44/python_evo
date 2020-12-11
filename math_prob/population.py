
import random as r

import matplotlib.pyplot as plt





class Population:
    
    def __init__(self, 
                 population_size, 
                 new_unit_fn, 
                 new_unit_fn_args, 
                 mate_fn,  
                 mutate_fn, 
                 mutate_args, 
                 survive_all_fn, 
                 survive_args):    
            
        self.mate_fn = mate_fn
        
        self.population_size = population_size
        
        self.death_log = []
        self.death_rate_log = []
        self.count_log = []
        
        self.new_unit_fn = new_unit_fn
        self.new_unit_fn_args = new_unit_fn_args
        
        self.mutate_fn = mutate_fn
        self.mutate_args = mutate_args
        
        self.survive_all_fn = survive_all_fn
        self.survive_args = survive_args
        
        self.reset()
        
    def print_info(self):
        print('new_unit_fn :' , self.new_unit_fn.__name__)

        
    def reset(self):
        # list comprehension
        self.population = [self.new_unit_fn(self.new_unit_fn_args) for _ in range(self.population_size)]
        print( self.population )

    def mate_all(self):
        #print(self.population)
        
        r.shuffle(self.population)    
        p1 = [self.mate_fn (self.population[x], self.population[x+1]  )  for x in range(0, len(self.population) -1, 2) ]    
        p2 = [self.mate_fn (self.population[x], self.population[x+1]  )  for x in range(0, len(self.population) -1, 2) ]
    
        self.population = p1 + p2
        
    def next_gen(self):
        r.shuffle(self.population) 
        lim = len(self.population)
        new_gen = []
        n = 0
        #print("self.population_size", self.population_size)
        for _ in range(self.population_size):
            
            new_unit = self.mate_fn(self.population[n] , self.population[ (n+1) % lim])
            n =  (n+ 2) % lim 
            new_gen.append(new_unit)
        #print(new_gen)
        self.population = new_gen
            
    
    def popstep(self):
        #self.printf()
        self.mutate_all()
        survivers = self.survive_all_fn(self.population, *self.survive_args)
        self.population = survivers
        count = self.count()
        self.count_log.append(count)
        #self.select_thrashhold(2)
        self.next_gen()
        
    def popsteps(self, steps):
        for _ in range(steps):
            self.popstep()
        
    
    
    def select_thrashhold(self):
        saved = self.survive_all_fn(self.population, self.survive_args)
        
        pop_was = len(self.population )
        deaths = len(self.population )  - len(saved)
        death_rate = int(100*deaths / pop_was)
        
        self.death_log.append ( deaths)
        self.death_rate_log.append (death_rate)
        
        self.population = saved
        
    def mutate_all(self):
        for n in  range(len(self.population)):
            unit = self.population[n] 
            self.population[n]  = self.mutate_fn(unit, self.mutate_args)

                
    def printf(self):
        for unit in self.population:
            print("-- unit :" , self.unit_tostr(unit))
        
        print("-- death_log : " , self.death_log, ", death_rates: " , self.death_rate_log )
 
 
    def unit_tostr(self, unit):
        return ''.join(chr(x) for x in unit)
    
    
    def count(self):
        return sum(self.population)
    



    def drift(self):
        self.mate_all(self.any_of_two)
    
    def isfinal(self):
        s = sum(self.population)
        return s == 0 or s == len(self.population)
    
    def new_vector_unit(self, unit_size, mutations_amount ):
        indexes = r.sample( range(unit_size), mutations_amount)
    
        unit = [ 0 for _ in range(unit_size)]
    
        for i in indexes:
            unit[i] = 1
            return unit 
        
    def count_same_mutations(self, a, b):
        count = 0
        for x in range(len(a)):
            if a[x] and b[x]:
                count += 1
        return count        
    
    def manhattan(self, a,b):
        dist = 0
        for x in range(len(a)):
            dist += abs(a[x] - b[x])
        return dist
            
        
    
        
    
    def run(self):

        #self.last_development = [sum(self.population)]
        self.last_development = []
        while( not self.isfinal()):
            self.last_development.append(sum(self.population))
            self.drift()  
            
            
    def run_mult_calculate_lengths(self, max_population_size, repeats):
        
        self.last_mult_log = []
        for population_size in range(max_population_size):
            repeat_results = []
            for r in range(repeats):
                self.reset(population_size)
                self.run()
                repeat_results.append(len(self.last_development))
            
            average = 1.0 * sum(repeat_results) / repeats
                
            self.last_mult_log.append(average)

     
   
    def show(self):
        plt.plot(self.last_development )

        plt.show()  
        
    def showm(self):
        plt.plot(self.last_mult_log )

        plt.show()  