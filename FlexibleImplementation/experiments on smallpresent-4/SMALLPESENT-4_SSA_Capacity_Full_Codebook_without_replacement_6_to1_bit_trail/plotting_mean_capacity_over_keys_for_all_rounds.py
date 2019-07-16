import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#6 to 1 bit trail
mean = [
0.00000000,
0.00000000,
4.41503750,
6.77703364,
8.70053273,
9.58974366,
9.87675617,
9.98996059,
10.01497612,
10.02103898,
10.02161420,
10.02147058,
10.02521670,
10.02390105,
10.02469028,
10.01979688,
10.02457101,
10.02560881,
10.02165810,
10.02225718,
10.02234745,
10.02127531,
10.01981914,
10.02199898,
10.02358810,
10.02238454,
10.02693628,
10.02276703,
10.02121390,
10.02179633,
10.02287130,
10.02207680
]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 1
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend(loc = "lower right")
plt.show();
