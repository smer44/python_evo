#12: neuro network example 
#from https://habr.com/ru/post/271563/
import numpy as np
import pprint as pp

input = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
expected = np.array([[0,1,1,0]]).T#[[0],[1],[1],[0]]
#create linear random weights
weights0 = 2*np.random.random((3,4)) - 1
weights1 = 2*np.random.random((4,1)) - 1
#xrange function is deprecated in Python 3 since range is behavin like xrange generator
for j in range(60000):
    #forward pass - we do that 
    layer1 = 1/(1+np.exp(-(np.dot(input,weights0)))) #sigmoid (-inf, inf)~(0,1)
    layer2 = 1/(1+np.exp(-(np.dot(layer1,weights1))))
    #backpropagation - we do not do that 
    #update layers:
    l2_delta = (expected - layer2)*(layer2*(1-layer2))# difference * derivative of activation function
    l1_delta = l2_delta.dot(weights1.T) * (layer1 * (1-layer1))
    #update weights:
    weights1 += layer1.T.dot(l2_delta)
    weights0 += input.T.dot(l1_delta)
    
# test output 

layer1 = 1/(1+np.exp(-(np.dot(input,weights0)))) #sigmoid
layer2 = 1/(1+np.exp(-(np.dot(layer1,weights1))))    

pp.pprint(layer2)
    

    