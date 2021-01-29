
import matplotlib.pyplot as plt

 

prod_per_day = 1000.0

konsum_per_day = 950.0

lager_size =  200.0

lager_on = 100.0

#guess - i want to keep the lager_on as middle of the lager
#therefore i increase production by 
# (konsum_per_day - prod_per_day) + konsum_per_day*(lager_size/2 - lager_on)


# Lieferschwierigkeiten Lagerschaden
# plusLieferzeit

days = 20


lager_ons = []
prods = []
for d in range(days):
    change = (konsum_per_day - prod_per_day)*(1/2 - lager_on/lager_size)
    #print(change)
    prod_per_day = prod_per_day + change
    assert prod_per_day > 0
    #print(prod_per_day)
    lager_on += prod_per_day - konsum_per_day
    assert lager_on > 0 and lager_on < lager_size
    #print(lager_on)
    lager_ons.append(lager_on)
    prods.append(prod_per_day)
    
xx = [x for x in range(days)]

print(len(xx))

print(len(prods))

plt.plot(xx, lager_ons,xx,prods)
#plt.plot(prod_per_day)
plt.show()