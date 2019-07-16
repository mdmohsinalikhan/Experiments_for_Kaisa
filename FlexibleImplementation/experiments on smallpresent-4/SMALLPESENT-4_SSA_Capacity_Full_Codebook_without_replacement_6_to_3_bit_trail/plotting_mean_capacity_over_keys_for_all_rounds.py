import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#6 to 3 bit trail
mean = [
-0.00000000,
-3.45943162,
-2.96018298,
-2.82887685,
-2.81368270,
-2.80942531,
-2.80877545,
-2.80862751,
-2.80859678,
-2.80858832,
-2.80858958,
-2.80858705,
-2.80858789,
-2.80858623,
-2.80858865,
-2.80858621,
-2.80858862,
-2.80858898,
-2.80858798,
-2.80858758,
-2.80858604,
-2.80858598,
-2.80858915,
-2.80859004,
-2.80858551,
-2.80858737,
-2.80858678,
-2.80858804,
-2.80858640,
-2.80859026,
-2.80858448,
-2.80858507
]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 3
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend(loc = "center right")
plt.show();
