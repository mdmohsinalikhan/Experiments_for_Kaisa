import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#6 to 3 bit trail
variance = [
0,
0,
0,
12.007220350823,
13.310985199141,
17.440746081393,
18.904858363090,
19.271077822450,
19.356124916777,
19.382407372523,
19.373859309977,
19.400288761068,
19.376521340535,
19.396814726960,
19.396773922843,
19.386991448129,
19.373338175917,
19.359170121531,
19.379818569262,
19.398133074364,
19.399197789365,
19.389826358591,
19.377454404470,
19.386006823004,
19.386522281877,
19.377322123718,
19.410153245773,
19.398604619632,
19.393721123392,
19.409261379126,
19.384087528110,
19.416526971983
]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 3
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
