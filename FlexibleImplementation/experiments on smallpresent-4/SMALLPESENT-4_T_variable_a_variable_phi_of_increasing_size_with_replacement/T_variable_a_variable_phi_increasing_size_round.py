import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [17.000000,16.500000,20.000000,19.250000,25.937500,21.187500,14.265625,12.500000]
t_1 = [20.000000,10.000000,20.000000,17.750000,26.750000,32.500000,40.343750,56.687500]
t_2 = [19.000000,13.000000,12.750000,10.750000,17.250000,37.750000,43.625000,58.195312]
t_3 = [13.000000,18.500000,15.750000,11.000000,13.062500,17.468750,28.781250,53.812500]
t_4 = [16.000000,22.000000,16.250000,19.875000,18.000000,36.937500,36.640625,51.515625]
t_5 = [30.000000,29.500000,46.500000,49.750000,31.000000,40.187500,60.203125,89.562500]
t_6 = [8.000000,8.500000,21.000000,17.375000,26.625000,39.062500,80.187500,83.921875]
t_7 = [17.000000,13.500000,19.000000,10.750000,15.312500,22.375000,37.828125,29.867188]
t_8 = [18.000000,19.000000,14.750000,15.875000,16.125000,13.406250,24.031250,34.679688]
t_9 = [9.000000,19.000000,16.500000,19.500000,24.125000,20.187500,27.734375,69.812500]
t_10 = [16.000000,25.000000,31.500000,30.125000,40.125000,56.218750,64.015625,103.679688]
t_11 = [11.000000,9.000000,7.000000,7.375000,10.500000,17.343750,34.000000,48.257812]
t_12 = [11.000000,18.000000,21.250000,14.125000,27.437500,35.531250,30.656250,34.625000]
t_13 = [13.000000,12.000000,15.750000,17.250000,14.625000,24.250000,37.734375,38.945312]
t_14 = [10.000000,13.500000,16.750000,11.500000,9.062500,29.062500,34.953125,46.914062]
t_15 = [12.000000,12.000000,12.250000,24.625000,31.125000,28.156250,40.312500,30.593750]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*0.0084733963
sigma_32 = math.sqrt((2.0/15)*(15+32*0.0084733963)**2)


# sample sizeL 64
mu_64 = 15 + 64*0.0084733963
sigma_64 = math.sqrt((2.0/15)*(15+64*0.0084733963)**2)


# sample sizeL 128
mu_128 = 15 + 128*0.0084733963
sigma_128 = math.sqrt((2.0/15)*(15+128*0.0084733963)**2)


# sample sizeL 256
mu_256 = 15 + 256*0.0084733963
sigma_256 = math.sqrt((2.0/15)*(15+256*0.0084733963)**2)


# sample sizeL 512
mu_512 = 15 + 512*0.0084733963
sigma_512 = math.sqrt((2.0/15)*(15+512*0.0084733963)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*0.0084733963
sigma_1024 = math.sqrt((2.0/15)*(15+1024*0.0084733963)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*0.0084733963
sigma_2048 = math.sqrt((2.0/15)*(15+2048*0.0084733963)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*0.0084733963
sigma_4096 = math.sqrt((2.0/15)*(15+4096*0.0084733963)**2)


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
#plt.plot(t,expected_T_a_3,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_4 = []
expected_T_a_4.append(mu_32-2*sigma_32)
expected_T_a_4.append(mu_64-2*sigma_64)
expected_T_a_4.append(mu_128-2*sigma_128)
expected_T_a_4.append(mu_256-2*sigma_256)
expected_T_a_4.append(mu_512-2*sigma_512)
expected_T_a_4.append(mu_1024-2*sigma_1024)
expected_T_a_4.append(mu_2048-2*sigma_2048)
expected_T_a_4.append(mu_4096-2*sigma_4096)
#plt.plot(t,expected_T_a_4,linewidth=.1, linestyle="-", c="DimGray")

#Plotting the experimental linesplt.plot(t, t_0, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_1, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_2, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_3, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_4, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_5, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_6, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_7, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_8, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_9, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_10, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_11, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_12, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_13, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_14, linewidth=.1, linestyle="-", c="red")
#plt.plot(t, t_15, linewidth=.1, linestyle="-", c="red")



#Shading the theoretical distribution region
plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='DimGray',alpha=.7)
#plt.fill_between(t, expected_T_a_1,expected_T_a_3,color='DimGray',alpha=.35)
#plt.fill_between(t, expected_T_a_2,expected_T_a_4,color='DimGray',alpha=.35)


expected_T_a_0 = []
expected_T_a_0.append(15)
expected_T_a_0.append(15)
expected_T_a_0.append(15)
expected_T_a_0.append(15)
expected_T_a_0.append(15)
expected_T_a_0.append(15)
expected_T_a_0.append(15)
expected_T_a_0.append(15)
plt.plot(t,expected_T_a_0,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_1 = []
expected_T_a_1.append(21)
expected_T_a_1.append(21)
expected_T_a_1.append(21)
expected_T_a_1.append(21)
expected_T_a_1.append(21)
expected_T_a_1.append(21)
expected_T_a_1.append(21)
expected_T_a_1.append(21)
plt.plot(t,expected_T_a_1,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_2 = []
expected_T_a_2.append(9)
expected_T_a_2.append(9)
expected_T_a_2.append(9)
expected_T_a_2.append(9)
expected_T_a_2.append(9)
expected_T_a_2.append(9)
expected_T_a_2.append(9)
expected_T_a_2.append(9)
plt.plot(t,expected_T_a_2,linewidth=.1, linestyle="-", c="DimGray")


#Shading the theoretical distribution region
plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='Blue',alpha=.3)


#Formatting the plot

plt.ylabel('Value of the statistic')
plt.xlabel('Number of plaintext-ciphertext pairs')
plt.text(5.5,70,'Gray Line is the behavior of the cipher')
plt.text(5.5,60,'Blue line is the random behavior')
plt.axis([5, 12, 0, 80])
plt.grid(True)
plt.show()
