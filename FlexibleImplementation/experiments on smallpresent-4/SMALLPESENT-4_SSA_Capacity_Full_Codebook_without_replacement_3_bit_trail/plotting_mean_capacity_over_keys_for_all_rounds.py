import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#3 to 3 bit trail
mean = [
0.00000000,
1.00000000,
3.35434157,
5.96104599,
8.16642846,
9.50982964,
10.12299372,
10.33005074,
10.37324325,
10.38068410,
10.38391831,
10.38354822,
10.38409997,
10.38834233,
10.38516462,
10.38896807,
10.38320640,
10.38733112,
10.38333350,
10.38400617,
10.38460473,
10.38250027,
10.38355658,
10.38234186,
10.38338472,
10.38651791,
10.38803434,
10.38680297,
10.38191987,
10.38390615,
10.38344342,
10.38569129
]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 3
v = 3
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend()
plt.show();
