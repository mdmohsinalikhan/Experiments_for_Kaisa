import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#6 to 2 bit trail
variance = [
0,
0,
20.000058131307,
17.833234124933,
19.551769395165,
22.587583686711,
23.213248730451,
23.429146747047,
23.436288656293,
23.422455643972,
23.433359881002,
23.434238509692,
23.433625178369,
23.455863258354,
23.433460546676,
23.444342891645,
23.385986129831,
23.433083872080,
23.422983679983,
23.460246489460,
23.423398255296,
23.434489029225,
23.407374531641,
23.426667419032,
23.412511750549,
23.416274399994,
23.459439392123,
23.427029431395,
23.450729147255,
23.452307360986,
23.411988903388,
23.453942761030
]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 2
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
