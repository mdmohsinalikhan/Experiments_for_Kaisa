import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [19.000000,14.500000,17.500000,14.875000,15.500000,12.875000,9.328125,10.765625]
t_1 = [13.000000,16.500000,11.750000,11.750000,12.375000,12.218750,9.609375,9.539062]
t_2 = [15.000000,13.500000,11.750000,7.500000,9.687500,12.218750,10.500000,14.679688]
t_3 = [8.000000,7.000000,13.750000,10.250000,10.437500,13.156250,11.921875,20.710938]
t_4 = [20.000000,18.000000,14.250000,18.250000,12.125000,11.531250,9.718750,16.164062]
t_5 = [10.000000,12.000000,11.000000,14.625000,17.687500,23.093750,16.953125,18.531250]
t_6 = [11.000000,19.000000,21.500000,14.250000,6.875000,7.656250,10.187500,15.250000]
t_7 = [12.000000,10.000000,12.000000,12.750000,13.312500,7.906250,15.171875,9.828125]
t_8 = [11.000000,8.500000,12.000000,22.750000,21.687500,21.312500,9.937500,12.000000]
t_9 = [10.000000,11.500000,11.500000,13.375000,15.937500,14.343750,16.437500,6.757812]
t_10 = [16.000000,22.000000,26.750000,22.375000,23.625000,18.437500,7.593750,6.531250]
t_11 = [17.000000,12.500000,14.000000,20.000000,22.625000,19.875000,7.734375,12.250000]
t_12 = [13.000000,9.500000,14.250000,8.875000,9.187500,10.250000,13.718750,11.171875]
t_13 = [16.000000,21.500000,16.250000,11.125000,17.500000,12.093750,14.375000,14.757812]
t_14 = [6.000000,12.000000,14.000000,13.000000,10.062500,16.343750,22.703125,23.867188]
t_15 = [7.000000,9.000000,15.500000,12.750000,14.062500,11.781250,18.375000,9.281250]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*xxxx
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*xxxx)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*xxxx
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*xxxx)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*xxxx
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*xxxx)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*xxxx
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*xxxx)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*xxxx
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*xxxx)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*xxxx
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*xxxx)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*xxxx
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*xxxx)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*xxxx
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*xxxx)**2)


#Plotting 5 different lines to present the theoretical distirbution of T

expected_T_a_0 = []
expected_T_a_0.append(mu_32)
expected_T_a_0.append(mu_64)
expected_T_a_0.append(mu_128)
expected_T_a_0.append(mu_256)
expected_T_a_0.append(mu_512)
expected_T_a_0.append(mu_1024)
expected_T_a_0.append(mu_2048)
expected_T_a_0.append(mu_4096)
plt.plot(t,expected_T_a_0,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_1 = []
expected_T_a_1.append(mu_32+sigma_32)
expected_T_a_1.append(mu_64+sigma_64)
expected_T_a_1.append(mu_128+sigma_128)
expected_T_a_1.append(mu_256+sigma_256)
expected_T_a_1.append(mu_512+sigma_512)
expected_T_a_1.append(mu_1024+sigma_1024)
expected_T_a_1.append(mu_2048+sigma_2048)
expected_T_a_1.append(mu_4096+sigma_4096)
plt.plot(t,expected_T_a_1,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_2 = []
expected_T_a_2.append(mu_32-sigma_32)
expected_T_a_2.append(mu_64-sigma_64)
expected_T_a_2.append(mu_128-sigma_128)
expected_T_a_2.append(mu_256-sigma_256)
expected_T_a_2.append(mu_512-sigma_512)
expected_T_a_2.append(mu_1024-sigma_1024)
expected_T_a_2.append(mu_2048-sigma_2048)
expected_T_a_2.append(mu_4096-sigma_4096)
plt.plot(t,expected_T_a_2,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_3 = []
expected_T_a_3.append(mu_32+2*sigma_32)
expected_T_a_3.append(mu_64+2*sigma_64)
expected_T_a_3.append(mu_128+2*sigma_128)
expected_T_a_3.append(mu_256+2*sigma_256)
expected_T_a_3.append(mu_512+2*sigma_512)
expected_T_a_3.append(mu_1024+2*sigma_1024)
expected_T_a_3.append(mu_2048+2*sigma_2048)
expected_T_a_3.append(mu_4096+2*sigma_4096)
plt.plot(t,expected_T_a_3,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_4 = []
expected_T_a_4.append(mu_32-2*sigma_32)
expected_T_a_4.append(mu_64-2*sigma_64)
expected_T_a_4.append(mu_128-2*sigma_128)
expected_T_a_4.append(mu_256-2*sigma_256)
expected_T_a_4.append(mu_512-2*sigma_512)
expected_T_a_4.append(mu_1024-2*sigma_1024)
expected_T_a_4.append(mu_2048-2*sigma_2048)
expected_T_a_4.append(mu_4096-2*sigma_4096)
plt.plot(t,expected_T_a_4,linewidth=.1, linestyle="-", c="DimGray")

#Plotting the experimental linesplt.plot(t, t_0, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_1, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_2, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_3, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_4, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_5, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_6, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_7, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_8, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_9, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_10, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_11, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_12, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_13, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_14, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_15, linewidth=.1, linestyle="-", c="red")



#Shading the theoretical distribution region
plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='DimGray',alpha=.7)
plt.fill_between(t, expected_T_a_1,expected_T_a_3,color='DimGray',alpha=.35)
plt.fill_between(t, expected_T_a_2,expected_T_a_4,color='DimGray',alpha=.35)


#Formatting the plot

plt.ylabel('$T(\phi,a)$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-15 with all zero key upto 4 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
