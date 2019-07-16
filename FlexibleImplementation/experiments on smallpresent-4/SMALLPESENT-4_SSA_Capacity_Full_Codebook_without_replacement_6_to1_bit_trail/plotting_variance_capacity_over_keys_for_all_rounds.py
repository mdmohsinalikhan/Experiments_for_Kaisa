import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#6 to 1 bit trail
variance = [
0,
0,
0,
18.631904578859,
20.514467070406,
24.060276840479,
24.677633356679,
24.992654670123,
25.034673803172,
25.021570845143,
25.003813445962,
25.045334070241,
25.035572367777,
25.032812527751,
25.011954211207,
25.021608055631,
25.018393776097,
25.036875208510,
25.015630747566,
25.025108214454,
25.027802517790,
25.022328805432,
25.001275021783,
25.024498257463,
25.017623912935,
25.045510006383,
25.007884954967,
25.052187506768,
25.035144658513,
25.070255984697,
25.031859434877,
25.016548355217
]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 1
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
