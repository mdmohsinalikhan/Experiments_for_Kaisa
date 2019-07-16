import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#4 to 4 bit trail
variance = [
0,
0,
0,
16.863410258497,
20.195714480735,
22.347879393638,
22.974351606163,
23.125242549483,
23.192618109086,
23.178003235263,
23.165354153340,
23.155339081696,
23.191743542716,
23.199148646298,
23.188032982693,
23.199106858465,
23.195842943298,
23.171763106078,
23.165366518304,
23.177757146066,
23.181627442588,
23.182885170384,
23.214490903596,
23.183826929565,
23.163324312088,
23.196973294621,
23.190071291700,
23.176140726187,
23.173010906496,
23.192609111638,
23.216543422555,
23.204157025805 
]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 4
v = 4
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
