import numpy as np
import pprint as pp
import os

def mate_choose(arr1,arr2):
    randints = np.random.randint(0,2,arr1.shape)
    #print(randints)
    child = np.where(randints, arr1,arr2)
    return child

def mate_interpolate(arr,arr2):
    randfloats = np.random.uniform(0,1,arr.shape) 
    print(randfloats)
    child = arr + (arr2 - arr) * randfloats
    return child

def mutate_uniform(arr,scale):
    arr = arr + np.random.uniform(-scale,scale,arr.shape)
    return arr

def manhattan(a,b):
    return np.abs(a-b).sum(-1)


class EvoController:
    # 20, 30, 40
    #layer_dimms = (30,40)
    def __init__(self, pop_size, *layer_dimms):
        
        self.pop_size = pop_size 
        
        self.errors = np.zeros(pop_size)
        self.mate_fn = mate_choose
        #self.mate_fn = mate_interpolate
        self.mutate_fn = mutate_uniform
        self.mutate_scale = 0.2 
        self.survive_rate = 0.25
                
        self.survive_count = int (pop_size * self.survive_rate)
        
        self.mate_times = 8
        self.w_init_scale = 1
        
        self.mate_indexes = np.arange(self.survive_count)
        self.layer_dimms = layer_dimms
        
        self.layers = self.init_layers(pop_size, *layer_dimms)
        self.weights = self.init_weights(pop_size, *layer_dimms)
        self.save_dir = "test_evo"
        
    def info(self):
        return f"survive rate {self.survive_rate}"
    
    def clone(self):
        
        other = EvoController(self.pop_size, *self.layer_dimms)
        
        other_layers = other.layers
        for n,layer in enumerate(self.layers):
            other_layers[n] = np.copy(layer)
        
        other_weights = other.weights
        for n,weight in enumerate(self.weights):
            other_weights[n] = np.copy(weight)      
            
    def eq(self, other):
        if self.pop_size != other.pop_size:
            return False 
        
        if self.layer_dimms != other.layer_dimms:
            return False         
        
        for n,weight in enumerate(self.weights):
            if not np.array_equal(weight, other.weights[n]):
                return False 
            
        for n, layer in enumerate(self.layers):
            if not np.array_equal(layer, other.layers[n]):
                return False      
        return True
                  
    
    def save(self):
        save_dir = self.save_dir
        path = os.getcwd() + '/' + save_dir 
        
        if not os.path.isdir(path):            
            try:
                os.mkdir(path)
            except OSError:
                print ("EvoController.save : Creation of the directory %s failed" % path)
            else:
                print ("EvoController.save : Successfully created the directory %s " % path)
        else:
            print ("EvoController.save : Saving to existing directory %s " % path)
            
        for n, layer in enumerate(self.layers):
            filepath = path + '/' + "layer" + str(n)
            np.save(filepath, layer)
        
        for n, weight in enumerate(self.weights):
            filepath = path + '/' + "weight" + str(n)
            np.save(filepath, weight)        
              
              
    def load(self):
        save_dir = self.save_dir
        path = os.getcwd() + '/' + save_dir 
        if not os.path.isdir(path):
            print ("EvoController.load : Trying to load from non existing directory %s " % path) 
            
        layers = self.layers
        for n in range(len(layers)):
            filepath = path + '/' + "layer" + str(n) + '.npy'
            layers[n] =  np.load(filepath)
            
        weights = self.weights    
        
        for n, weight in enumerate(weights):
            filepath = path + '/' + "weight" + str(n)  + '.npy'             
            weights[n] =  np.load(filepath)         
             
                                  
        
        
    def init_weights(self,pop_size,*layer_dimms):
        weighs = []
        #[level, unit_number, this_layer_size, next_layer_size]
        
        # len(layer_dimms) = 3 levels
        # pop_size = 20 units
        # layer_dimms = 3, 50, 4 
        # weights : (20,3, 50) (20, 50, 4)
        for x in range(len(layer_dimms)-1):
            dims= (pop_size,layer_dimms[x],layer_dimms[x+1] )
            print("init_weights : level " , x, ", shape:", dims )
            weight = np.random.uniform(-self.w_init_scale ,self.w_init_scale ,dims)
            weighs.append(weight)
        return weighs
    
    
    def init_layers(self,pop_size,*layer_dimms):
        layers= []
        for d in layer_dimms:
            dim = (pop_size, d)
            print("init_layers : shape:", dim )
            layer = np.zeros(dim)
            layers.append(layer)
        return layers    
        
    # - unit number     
    def forward(self,n ,input):
        self.layers[0][n] = input   
        for x in range(len(self.weights)):
            #do not need to assign 
            layer = self.layers[x][n]
            weigt = self.weights[x][n]
            mult = np.dot( layer,weigt)
            out = self.af(mult)
            self.layers[x+1][n] = out
            
        return self.layers[-1][n]
    
    def af(self,layer):
        return 1/(1+np.exp(layer))    
    
    
    def next_gen(self):
        self.survive()
        self.mate_all()
        self.mutate_all()
        
    def survive(self):
        indexes =  np.argsort(self.errors)[0:self.survive_count]
        
        #self.weights = level0[indexes], level1[indexes], level2[indexes] 
        self.weights = [weight[indexes] for weight in self.weights]
        #print("survive: ", len(self.weights[0]))
        
        #not nessasary
        self.errors = self.errors[indexes]
        
    def mate_all(self):   
        np.random.shuffle(self.mate_indexes)  
        children = []
        
        for weights_level in self.weights:
            new_shape = (self.pop_size, *weights_level.shape[1:])
            chilren_level = np.zeros(new_shape)
            #print("mate_all : new_shape : " , new_shape)
            #index=0
            # short to say, something wrong was mit indexes here 
            # if you index for 0 to self.survive_count
            count = 0
            # for unit_nr in range(0,self.survive_count,2):
            #    father = weights_level[self.mate_indexes[unit_nr]]
            #    mother = weights_level[self.mate_indexes[(unit_nr+1)%self.survive_count]]
            #    child = self.mate_fn(father, mother)
            #    chilren_level[count] = child
            #    count +=1 
          
            for child_index in range(0,self.pop_size):
                father_index = self.mate_indexes[child_index % self.survive_count]
                mother_index = self.mate_indexes[(child_index+1)%self.survive_count]
                #print("father_index : " , father_index , "mother_index : ", mother_index )
                father = weights_level[father_index]
                mother = weights_level[mother_index]
                child = self.mate_fn(father, mother)
                chilren_level[child_index] = child
                count +=1 # count = 20
            #print("count : ",count)
                #index +=1
            children.append(chilren_level)
        self.weights = children
        #nullify fitness?
        self.errors = np.zeros(self.pop_size)
        return children
        
    def mutate_all(self):
        #self.mutate_fn(self.layers, self.mutate_scale)
        for n in range(len(self.weights)):
            self.weights[n] = self.mutate_fn(self.weights[n],self.mutate_scale)          
             
            
         
    
        



