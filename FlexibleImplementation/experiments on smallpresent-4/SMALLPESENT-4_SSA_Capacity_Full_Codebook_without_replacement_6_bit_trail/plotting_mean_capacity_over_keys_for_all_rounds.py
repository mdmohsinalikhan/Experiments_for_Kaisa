import numpy as np
import matplotlib.pyplot as plt
import math

rounds = np.array(range(0,32))


#6 to 6 bit trail
mean = [0, -2.39231742, 0.11791846, 2.187934, 3.46083842, 3.90023654, 4.01272146, 4.03895749, 4.04374938, 4.04486715, 4.04567159, 4.0456105, 4.04524905, 4.04565331, 4.04552596, 4.04520703, 4.04532599, 4.04504033, 4.04511708, 4.04529942, 
4.04535248, 4.0452445, 4.04489345, 4.04544971, 4.04526084, 4.04554623, 4.04529207, 4.04558312, 4.04517422, 4.04543671,
4.04503873, 4.04511229]


#Plotting the experimental lines
plt.plot(rounds, mean, label='experimental', linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 6
conjectured_mean = -1*math.log((1.0/2**n)*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)
plt.plot(rounds, conjectured_mean, label='theoretical', linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\mu_{C})$')
plt.legend(loc = "lower right")
plt.show();
