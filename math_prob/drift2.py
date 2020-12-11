

from math_prob.population import *
from math_prob.pop_utils import *

import matplotlib.pyplot as plt

#pip3 install --user http://bit.ly/csc161graphics

psize = 20





drift_pop = Population(psize,
                 simple_unit,
                 2,
                 mate_any_of_two,
                 no_mutate,
                 (),
                 #(0.5,1),
                 survive_all,
                 ())


#pop.print_info()

drift_pop.popsteps(40)

plt.plot(drift_pop.count_log)

plt.show() 
