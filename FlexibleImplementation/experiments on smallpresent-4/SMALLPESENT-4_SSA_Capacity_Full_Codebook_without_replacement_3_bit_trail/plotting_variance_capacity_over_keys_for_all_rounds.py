import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#3 to 3 bit trail
variance = [
0,
0,
0,
17.672467223514,
19.814501647132,
23.221884970834,
24.757526837801,
25.247551844783,
25.368352056840,
25.383630911561,
25.361371242190,
25.361129076780,
25.412758616779,
25.388749931526,
25.377455410738,
25.390065193933,
25.395826208067,
25.391314297445,
25.387393107291,
25.376644834113,
25.398795962788,
25.371694562659,
25.357988765007,
25.390739851390,
25.374487418192,
25.398664506630,
25.345103134122,
25.378101176241,
25.378724856425,
25.361489422646,
25.391011925927,
25.381387030969
]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 3
v = 3
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
