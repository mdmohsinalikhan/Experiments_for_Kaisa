import numpy as np
import matplotlib.pyplot as plt
import math

keys = np.array(range(0,2**14))


#4 to 4 bit trail
filename = "capacity_for_different_keys_at_20th_round.txt"

with open(filename) as f:
    capacity = [float(x) for x in f.read().splitlines()]

#print(type(capacity))
print(capacity)

num_bins = 100

#Plotting the experimental lines
#plt.plot(keys, capacity, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)
plt.hist(capacity, num_bins, label='experimental', facecolor='grey', normed = 1.0, alpha=0.1)


df = 63
support = np.array(range(0,100))
y = [1 / (2*math.gamma(df/2)) * (z/2)**(df/2-1) * math.exp(-z/2) for z in support]
plt.plot(support, y, label='$\chi^2(63)$', linewidth=1.0, c = "black", linestyle="-", alpha = 1.0)


#Plotting the theoretical lines
#n = 16
#u = 3
#v = 3
#conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
#plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$C*2^{16}$')
plt.ylabel(r'$p(C)$')
plt.legend(loc = "upper right")
plt.show();
