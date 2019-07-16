import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#6 to 2 bit trail
mean = [
-0.00000000,
1.00000000,
3.34187919,
5.88762243,
7.50609352,
8.14191456,
8.35522148,
8.41823351,
8.43334637,
8.43822766,
8.43768905,
8.43848128,
8.43932986,
8.43769212,
8.43981595,
8.43645868,
8.43835108,
8.43899333,
8.43848755,
8.43832585,
8.43975680,
8.43841112,
8.43462857,
8.43722165,
8.43920889,
8.43676641,
8.44021115,
8.43776392,
8.43732174,
8.43780282,
8.43816331,
8.43769966
]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 2
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend(loc = "lower right")
plt.show();
