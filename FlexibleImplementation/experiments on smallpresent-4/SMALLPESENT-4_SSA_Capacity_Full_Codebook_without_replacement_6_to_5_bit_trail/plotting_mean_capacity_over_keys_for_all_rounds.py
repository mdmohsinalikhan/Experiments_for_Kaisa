import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#6 to 5 bit trail
mean = [0, -2.20945337, -0.68091829, -0.15998899, -0.06986397, -0.04730238, -0.0431201, -0.04201832, -0.04176896, -0.04173499, -0.04169319, -0.04167466, -0.04170643, -0.04168865, -0.04171542,
-0.04170142, -0.04170774, -0.04169445, -0.0417054, -0.04172332, -0.04171743, -0.04170443, -0.04173824, -0.04169505, -0.04168688, -0.04167789, -0.04170519, -0.04169106, -0.04168987, -0.04171203, -0.04170348, -0.04170973
]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 5
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend(loc = "center right")
plt.show();
