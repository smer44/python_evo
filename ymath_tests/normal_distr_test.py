import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 90,1.3*4


#x,y = distr(95,90,40000) corresponds mu, sigma = 90,1.5

#x,y = distr(95*2,90,50000)  corresponds mu, sigma = 90,5.2


s = np.random.normal(mu, sigma, 1000)

# Create the bins and histogram
#count, bins, ignored = plt.hist(s, 20)

bins = np.arange(70,110,0.1)
print(bins)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()
