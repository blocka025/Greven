import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
"""WARNING: TAKES A LONG TIME TO RUN"""
#global variabe
steps= 50000000 #Number of time steps
# tstep = 2 *10^(-3)# 2 msec
div = 100 #Consider 40 chunks of the sapphire rod
Tx = np.zeros(div)
L = 1.255*0.0254 #sapphire rod length in m
L_step = L/div
Tend4 = np.zeros(steps) #Simulated temperature at the end of the rod (away from the temp sensor end)
d2T = np.zeros(div-2)
averageTempDiff = np.zeros(14)
r = 0.0015875#radius of the sapphire rod in meters

# #specific Heat Fit data 
# #https://nvlpubs.nist.gov/nistpubs/jres/087/jresv87n2p159_A1b.pdf
# #P1
# a0 = -0.5147e+01
# a1 = 0.34127
# a2 = -0.333446e-01
# a3 = 0.450764e-02
# a4 = -0.51464e-03
# a5 = 0.397864e-04
# a6 = -0.152136e-05

# #P2
# b0 = 0.6966
# b1 = 0.59387e-01
# b2 = 0.40357e-02
# b3 = 0.95173e-04
# b4 = -0.35910e-05
# b5 = -0.6498e-07
# b6 = 0.4089e-08

# #P3
# c0 = 0.21993e02
# c1 = 0.38853
# c2 = 0.13955e-02
# c3 = -0.83967e-04
# c4 = 0.19133e-05
# c5 = -0.31778e-07
# c6 = 0.29562e-09

P1s = [-0.5147e+01, 0.34127,-0.333446e-01/2,0.450764e-02/6,-0.51464e-03/24,0.397864e-04/120,-0.152136e-05/720]
P2s = [0.6966,0.59387e-01,0.40357e-02/2,0.95173e-04/6,-0.35910e-05/24,-0.6498e-07/120,0.4089e-08/720]
P3s = [0.21993e02,0.38853,0.13955e-02/2,-0.83967e-04/6,0.19133e-05/24,-0.31778e-07/120,0.29562e-09/720]

const1 = 2*5.6704e-8*.1019613*0.49/(3970*r) 
const2 = 2*5.6704e-8*.1019613*0.79*77.3**4/(3970*r)
print(const1,const2)
input()
for rampRate in range(10,30,10):
    time = np.linspace(0,3600*195/rampRate,steps)#this gives time in seconds and begins at 78 and ends at 273
    tstep = time[-1]/steps
    Td = 78 + rampRate/3600*time #Temperature of the copper
    Tx[0] = Td[0] #Assume that the rod starts at 78K
    for k in range(div-1):
        Tx[k+1]=Td[0]


    for i in range(steps):
        for j in range(div-2):
            A = Tx[j+2]-Tx[j+1]
            B = Tx[j+1]-Tx[j]
            d2T[j]= (A-B)/(L_step**2)
        
        Tx[0] = Td[i]
        for j in range(1,div-1):
            a = (Tx[j]*2.4667e-10 - 1.1679e-7)*Tx[j] + 1.942e-5
            if Tx[j] < 45 and Tx[j] > 8.61:
                C = math.exp(P1s[0]*(Tx[j] - 8.61)**0 + P1s[1]*(Tx[j] - 8.61)**1 + P1s[2]*(Tx[j] - 8.61)**2 + P1s[3]*(Tx[j] - 8.61)**3 + P1s[4]*(Tx[j] - 8.61)**4 + P1s[5]*(Tx[j] - 8.61)**5 + P1s[6]*(Tx[j] - 8.61)**6)
            elif Tx[j] >= 45 and Tx[j] < 125:
                C = P2s[0]*(Tx[j] - 40)**0 + P2s[1]*(Tx[j] - 40)**1 + P2s[2]*(Tx[j] - 40)**2 + P2s[3]*(Tx[j] - 40)**3 + P2s[4]*(Tx[j] - 40)**4 + P2s[5]*(Tx[j] - 40)**5 + P2s[6]*(Tx[j] - 40)**6
            elif Tx[j] > 125:
                C = P3s[0]*(Tx[j] - 125)**0 + P3s[1]*(Tx[j] - 125)**1 + P3s[2]*(Tx[j] - 125)**2 + P3s[3]*(Tx[j] - 125)**3 + P3s[4]*(Tx[j] - 125)**4 + P3s[5]*(Tx[j] - 125)**5 + P3s[6]*(Tx[j] - 125)**6
            else:
                print('out of temp range')
                input(Tx[j])
            Tx[j] = Tx[j]+(a*d2T[j-1] - (8.990231911138263e-10*Tx[j]**4-0.05175113532175594)/C)*tstep 
            #This equation is T0 + dT/dt*tstep+a*d^2T/dx^2*L_step^2*tstep
            #T0 is prev temp
            #dT/dt is the temp change from radiation which is 
            #the last therm is the thermal conduction term where a is thermal diffusivty.
        Tx[div-1]=Tx[div-2]
        Tend4[i]=Tx[div-2]
    sum = 0

    for k in range(steps):
        # print(Td[k],Tend4[k])
        # input()
        sum += Td[k]-Tend4[k]
    averageTempDiff[rampRate//10-1] = sum/steps
    print(averageTempDiff)
    fig,ax = plt.subplots(1,1,figsize = (8,5))
    ax.plot(time/60,Td-Tend4)
    ax.set_xlabel('Time (min)',fontsize = 15)
    ax.set_ylabel('Temperature Difference (K)',fontsize = 15)
    ax.set_title('Ramp Rate = ' + str(rampRate))
    path = 'C:\\Users\\blake\\Documents\\VSCode\\Python\\Greven\\PNGs\\RampRate=' + str(rampRate) + '.png'
    plt.savefig(path)
    # plt.show()
fig,ax = plt.subplots(1,1,figsize = (8,5))
# ax.plot(time,Td)
# ax.plot(time,Tend4)
ax.scatter(range(10,150,10),averageTempDiff)
ax.set_xlabel('Ramp Rate (K/h)',fontsize = 15)
ax.set_ylabel('Average Temperature Difference (K)',fontsize = 15)
plt.show()