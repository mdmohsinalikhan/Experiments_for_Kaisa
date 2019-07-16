import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#6 to 4 bit trail
variance = [
0,
0,
17.887197496796, 
12.529721055678,
14.686743478761,
18.075298048699,
18.917900361827,
19.121013884920,
19.170802541114,
19.176230348162,
19.195098490957,
19.173684723446,
19.187547498198,
19.184546610659,
19.204034249994,
19.187953413250,
19.152534770410,
19.187380896033,
19.174316536732,
19.193441316367,
19.191925249814,
19.194908547381,
19.180378882624,
19.194470546922,
19.181006087563,
19.200395248583,
19.203933499058,
19.180575117027,
19.169879955604,
19.190829779307,
19.166117109636,
19.174018434843
]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 4
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
