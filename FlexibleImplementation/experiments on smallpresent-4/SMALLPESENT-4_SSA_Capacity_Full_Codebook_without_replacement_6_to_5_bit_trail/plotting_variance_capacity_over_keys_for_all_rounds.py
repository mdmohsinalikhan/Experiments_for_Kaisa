import numpy as np
import matplotlib.pyplot as plt
import math



rounds = np.array(range(0,32))

#6 to 5 bit trail
variance = [
0,
0,
14.652187124971,
13.749371444216,
15.989930998547,
18.396399385991,
18.943255897121,
19.071623316931,
19.097506685811,
19.055681585025,
19.084489745246,
19.055107428525,
19.108270329151,
19.095056686848,
19.073234898785,
19.091563507338,
19.101684301892,
19.104418484928,
19.078831442377,
19.085927133120,
19.072423671967,
19.102232729649,
19.090287305408,
19.102200281536,
19.082077392981,
19.082980048708,
19.097181905978,
19.115148610345,
19.088309114878,
19.117639490301,
19.094562151824,
19.042436875113]


#Plotting the experimental lines
plt.plot(rounds, variance, label = "experimental", linewidth=1.0, linestyle="--", c="black", alpha = 1.0)


#Plotting the theoretical lines
n = 16
u = 6
v = 5
conjectured_variance = -1*math.log((2**(1-2*n))*(2**(u+v) - 2**u - 2**v + 1),2)*(rounds**0)


plt.plot(rounds, conjectured_variance, label = "theoretical", linewidth=1.0, linestyle="-", c="black", alpha = 1.0)


#Formatting the plot
plt.xlabel(r'$r = \#$Rounds')
plt.ylabel(r'$R = -\log_2(\sigma^{2}_{C})$')
plt.legend(loc = "lower right")
plt.show();
