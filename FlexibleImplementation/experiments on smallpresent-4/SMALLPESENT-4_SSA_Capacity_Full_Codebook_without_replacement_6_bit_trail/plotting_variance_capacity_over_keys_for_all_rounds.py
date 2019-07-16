import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#6 to 6 bit trail
variance = [0, 0 , 12.8360771019, 13.5155364733, 16.3110735174, 18.3446164804, 18.9087105538, 19.0629227703, 19.0425653449, 19.0471834686, 19.0525640572, 19.0622138574, 19.0493746966, 19.0741250334, 19.0147238057, 19.0473040826, 19.0742176794, 19.0526137569, 19.0601887986, 19.0409362898, 19.0306547598, 19.0583430827, 19.051926923, 19.0709663238, 19.0455579284, 19.0354707745, 19.0676477373, 19.048641681, 19.0450009079, 19.0593510412, 19.0608589227, 19.0469382509]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 6
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
