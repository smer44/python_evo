
from csmodel.any import *      
    
    
# some basic elements:


action = Any(None, "Action" , action = True, active = bool , info = bool, discrete = bool)

object = Any(None, "Object", object = True, active = bool, info = bool, discrete = bool)

aliveobj = object("Alive", info = False, discrete= True, alive = True)




# an active object can make any action and passive object can make only passive action
# an info object can do only info action, a physical object can do both
# a discrete object can only do discrete action, 

# an non alive objet can not do alive action
#action.active -> subject.active
#TODO rule evaluator

can_relation = Any(None, "can_rel",
                subject = object, 
                action = action, 
                rules = [lambda me: not me.action.active or me.subject.active , 
                         lambda me: not me.subject.info or me.action.info , 
                         lambda me: me.subject.discrete == me.action.discrete,
                         lambda me: not me.action.alive or me.subject.alive, 
                          ],               
                fs = lambda me : f'{me.subject} can {["not", ""][me.check()]} {me.action} '
                )


