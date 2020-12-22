import numpy as np
import pprint as pp


#13: modify to numpy neural network
class SnakeMLController:
    
    def __init__(self, pop_size, *layer_dimms):
        
        self.pop_size = pop_size 
        self.layers = self.init_layers(pop_size, *layer_dimms)
        self.weights = self.init_weights(pop_size, *layer_dimms)
        
        
    def init_layers(self,pop_size,*layer_dimms):
        
        return np.random.normal(0.5,0.2,(pop_size,*layer_dimms))

    
    def init_weights(self,pop_size,*layer_dimms):
        weighs = []
        for x in range(len(layer_dimms)-1):
            dims= (pop_size,layer_dimms[x],layer_dimms[x+1] )
            print("weights " , x, "dims:", dims )
            weight = np.random.normal(0.5,0.2,dims)
            weighs.append(weight)
            
        
        return weighs
        
        
    def forward_all(self):
        
        for nn_index in range(len(self.layers)):                
            layers = self.layers[nn_index]                             
            weights = self.weights[nn_index]
        return self.forward(layers, weights )
    
    def af(self,layer):
        return 1/(1+np.exp(layer))#sigmoid activation function
    
    def baf (self,layer):
        return layer*(1-layer)#derivative of sigmoid af 
        
    def forward(self,layers, weights ):
        for x in range(len(layers)-1):
            layers[x+1] = self.af( np.dot(layers[x], weights[x]) )
            
            
        
        
    
    
    

sc = SnakeMLController(2, 3,4,1)

pp.pprint(sc.layers)
pp.pprint(sc.weights)        