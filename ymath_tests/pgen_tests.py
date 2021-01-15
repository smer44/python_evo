from  ymath.pgen import * 





# amount of genes :       
n = 2000#60


# amount of mutations in first parent:
x = 80

# amount of mutations in the second parent:
y = 120
        
    
popsize =  2000

mutations_per_unit = 3

survival_rate = 0.75

"""xx,yy = distr(n,x,y,popsize)


plt.plot(xx,yy, color = "orange")

plt.show()"""


pop = new_pop(n,x,y,popsize)

mutations_per_gen = mutations_per_unit*popsize

run_gen_mut(pop,1000, mutations_per_gen,survival_rate)