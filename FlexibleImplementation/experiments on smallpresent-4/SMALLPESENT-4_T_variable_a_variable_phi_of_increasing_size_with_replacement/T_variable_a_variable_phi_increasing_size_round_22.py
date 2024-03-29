import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [13.000000,11.500000,9.250000,21.625000,18.250000,10.750000,15.312500,21.429688]
t_1 = [13.000000,8.000000,12.250000,12.250000,14.937500,28.750000,23.062500,19.500000]
t_2 = [15.000000,9.500000,9.000000,18.250000,21.687500,21.000000,19.890625,24.726562]
t_3 = [13.000000,21.500000,18.250000,21.625000,27.625000,34.406250,34.828125,26.859375]
t_4 = [9.000000,8.500000,20.250000,16.125000,18.000000,14.500000,14.296875,17.796875]
t_5 = [6.000000,12.000000,5.000000,12.875000,7.812500,16.000000,10.078125,19.984375]
t_6 = [15.000000,16.000000,12.000000,15.375000,16.750000,14.093750,18.468750,16.179688]
t_7 = [11.000000,19.500000,25.750000,16.625000,11.687500,9.406250,24.531250,33.476562]
t_8 = [9.000000,19.000000,12.750000,18.125000,15.375000,7.656250,15.015625,28.804688]
t_9 = [13.000000,17.000000,18.000000,19.875000,31.812500,26.968750,24.578125,26.750000]
t_10 = [15.000000,8.000000,16.000000,21.375000,10.937500,7.375000,17.500000,25.218750]
t_11 = [20.000000,13.000000,13.750000,10.500000,8.687500,9.031250,15.234375,12.914062]
t_12 = [11.000000,5.000000,15.750000,20.625000,15.687500,18.406250,10.781250,12.898438]
t_13 = [11.000000,19.500000,9.500000,7.750000,17.437500,19.625000,34.640625,31.250000]
t_14 = [20.000000,22.000000,17.500000,15.750000,19.812500,27.062500,25.906250,42.054688]
t_15 = [7.000000,9.000000,23.250000,13.375000,18.250000,28.281250,23.468750,39.359375]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*0.0035172700
sigma_32 = math.sqrt((2.0/15)*(15+32*0.0035172700)**2)


# sample sizeL 64
mu_64 = 15 + 64*0.0035172700
sigma_64 = math.sqrt((2.0/15)*(15+64*0.0035172700)**2)


# sample sizeL 128
mu_128 = 15 + 128*0.0035172700
sigma_128 = math.sqrt((2.0/15)*(15+128*0.0035172700)**2)


# sample sizeL 256
mu_256 = 15 + 256*0.0035172700
sigma_256 = math.sqrt((2.0/15)*(15+256*0.0035172700)**2)


# sample sizeL 512
mu_512 = 15 + 512*0.0035172700
sigma_512 = math.sqrt((2.0/15)*(15+512*0.0035172700)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*0.0035172700
sigma_1024 = math.sqrt((2.0/15)*(15+1024*0.0035172700)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*0.0035172700
sigma_2048 = math.sqrt((2.0/15)*(15+2048*0.0035172700)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*0.0035172700
sigma_4096 = math.sqrt((2.0/15)*(15+4096*0.0035172700)**2)


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
plt.xlabel('$log_2|\phi|$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-[$4$] with all zero key upto 22 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
