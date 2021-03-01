
import numpy as np
import pprint as pp


def mate_choose(arr1,arr2):
    randints = np.random.randint(0,2,arr1.shape)
    child = np.where(randints, arr1,arr2)
    return child

def mate_interpolate(arr,arr2):
    randfloats = np.random.uniform(0,1,arr.shape) 
    child = arr + (arr2 - arr) * randfloats
    return child


def mutate_uniform(arr,scale):
    arr = arr + np.random.uniform(-scale,scale,arr.shape)
    return arr 


def manhattan(a,b):
    return np.abs(a-b).sum(-1)
    



#13: modify to numpy neural network
class EvoController_Old:
    
    def __init__(self, pop_size, *layer_dimms):
        
        self.pop_size = pop_size 
        self.layers = self.init_layers(pop_size, *layer_dimms)
        
        #indexes of this arrays: [level, unit_index,this layers size, next layer size]
        
        self.weights = self.init_weights(pop_size, *layer_dimms)
        self.fitnesses = np.zeros(pop_size)
        self.mate_fn = mate_choose
        self.mutate_fn = mutate_uniform
        self.mutate_scale = 0.2 # increase mutate rate ?
        self.survive_rate = 0.5
        self.survive_count = int (pop_size * self.survive_rate)
        
        self.mate_indexes = np.arange(self.survive_count)
        self.mate_times = 4
        
        
    def init_layers(self,pop_size,*layer_dimms):
        layers= []
        for d in layer_dimms:
            dim = (pop_size, d)
            #layer = np.random.normal(0.5,0.2,dim)
            layer = np.zeros(dim)
            layers.append(layer)
        
        #return np.random.normal(0.5,0.2,(pop_size,*layer_dimms))
        return layers

    
    def init_weights(self,pop_size,*layer_dimms):
        weighs = []
        for x in range(len(layer_dimms)-1):
            dims= (pop_size,layer_dimms[x],layer_dimms[x+1] )
            print("init_weights : level " , x, ", shape:", dims )
            #because the initial difference will be too low
            # = the result will be from the begin not as sharp as if 
            # we use uniform with big weights
            #weight = np.random.normal(0.5,0.2,dims)
            weight = np.random.uniform(-1,1,dims)
            weighs.append(weight)
            
        
        return weighs # np.array(weighs)
        
        
    def forward_all(self):
        
        for nn_index in range(len(self.layers)):                
            layers = self.layers[nn_index]                             
            weights = self.weights[nn_index]
        return self.forward(layers, weights )
    
    def af(self,layer):
        return 1/(1+np.exp(layer))#sigmoid activation function
    
    def baf (self,layer):
        return layer*(1-layer)#derivative of sigmoid af 
        
    def forward(self,n ,input):
        self.layers[0][n] = input
        for x in range(len(self.weights)):
            self.layers[x+1][n] = self.af( np.dot( self.layers[x][n],self. weights[x][n]) )
        
        return self.layers[-1][n]#values of the last layer
            
            
    def mate(self,a,b):
        #assert a!= b
        
        #child_layer = self.mate_fn(self.layers[a],self.layers[b])
        child_weight = self.mate_fn(a,b)
        return child_weight
    
    def mutate_all(self):
        #self.mutate_fn(self.layers, self.mutate_scale)
        for n in range(len(self.weights)):
            self.weights[n] = self.mutate_fn(self.weights[n],self.mutate_scale)
            #self.mutate_fn(self.weights[n],self.mutate_scale)
        
    def survive(self):
        #get indexes of sorting, does not change  
        indexes =  np.argsort(self.fitnesses)[0:self.survive_count]
        #sows = []
        #weights between specific layers:
        #for weight in self.weights:
        #    sow = weight[pos]
        #   sows.append(sow)
        sows = [weight[indexes] for weight in self.weights]
        self.weights = sows 
        #just for tests:
        self.fitnesses = self.fitnesses[indexes]
        
    
    #n  children per each pair
    def mate_all(self):    
        np.random.shuffle(self.mate_indexes)   
        #print(" self.pop_size " ,  self.pop_size )
        #print(" self.mate_times " , self.mate_times )
        
        #self.survive()
        children = []
        for weights_level in self.weights:
            new_ws = np.zeros((self.pop_size, *weights_level.shape[1:]))
           # print("new_ws.shape", new_ws.shape)
            count=0
            #print("len(weights_level)", len(weights_level))
            #print("self.survive_count:" , self.survive_count)
            for unit_nr in range(0,self.survive_count,2):
                for _ in range(self.mate_times):
                    #print("mate_all:", unit_nr, unit_nr+1, "count : " , count)
                    new_ws[count]= self.mate(weights_level[unit_nr],weights_level[unit_nr+1])
                    count +=1
                    
            children.append(new_ws)
        
        #print("mate_all : len(children)", len(children))
        #print("mate_all : children[0].shape", children[0].shape)
        self.weights = children
        self.fitnesses = np.zeros(self.pop_size)
        return children
            
            
    def next_gen(self):
        self.survive()
        self.mate_all()
        self.mutate_all()
        
    def printsizes(self):
        print("---printsizes---")
        print("popsizes: ",  self.pop_size )
        print("len(self.layers): ",  len(self.layers) )
        print("self.layers[0].shape): ",  self.layers[0].shape )
        print("len(self.weights): ",  len(self.weights) )
        
        print("self.weights[0].shape): ",  self.weights[0].shape )        
        
        
        print("--- --- --- ---")
        
    
     