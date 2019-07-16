import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#6 to 4 bit trail
mean = [
-0.00000000,
-2.42626475,
-1.85822660,
-1.64004169,
-1.60296911,
-1.59352491,
-1.59207581,
-1.59166630,
-1.59157507,
-1.59155833,
-1.59155685,
-1.59154865,
-1.59155272,
-1.59154918,
-1.59155457,
-1.59154642,
-1.59155251,
-1.59154915,
-1.59154377,
-1.59155416,
-1.59155475,
-1.59155068,
-1.59155692,
-1.59155209,
-1.59154453,
-1.59154738,
-1.59155215,
-1.59155753,
-1.59154942,
-1.59155818,
-1.59155407,
-1.59155461
]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 4
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend(loc = "center right")
plt.show();
