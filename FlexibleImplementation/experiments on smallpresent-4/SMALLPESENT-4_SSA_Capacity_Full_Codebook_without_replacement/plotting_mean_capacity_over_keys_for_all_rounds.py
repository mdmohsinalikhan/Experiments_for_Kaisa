import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#4 to 4 bit trail
mean = [
0.00000000,
0.32192809,
3.53239445,
5.59935704,
7.34741637,
7.94638755,
8.10247633,
8.16520564,
8.18132471,
8.18604582,
8.18638752,
8.18811392,
8.18448227,
8.18719201,
8.18550577,
8.18687441,
8.18356177,
8.18529613,
8.18543329,
8.18679644,
8.18717056,
8.18722791,
8.18670693,
8.18603468,
8.18514342,
8.18638696,
8.18685346,
8.18402746,
8.18498258,
8.18717964,
8.18758036,
8.18546084
]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 4
v = 4
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend(loc = "lower right")
plt.show();
