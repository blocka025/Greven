import math
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
"""WARNING: TAKES A LONG TIME TO RUN"""
#global variabe
steps= 500000 #Number of time steps
# tstep = 2 *10^(-3)# 2 msec
div = 40 #Consider 40 chunks of the sapphire rod
Tx = np.zeros(div)
L = 1.255*0.0254 #sapphire rod length in m
L_step = L/div
Tend4 = np.zeros(steps) #Simulated temperature at the end of the rod (away from the temp sensor end)
d2T = np.zeros(div-2)
rampRate = 100
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
    # dT = 2*0.49*5.6704e-8*0.1013*(Td[i]**4-77.3**4)/(3*3930*1.3806*L*6.022)*tstep #Radiation
    Tx[0] = Td[i]
    for j in range(1,div-1):
        a = (Tx[j]*2.4667e-10 - 1.1679e-7)*Tx[j] + 1.942e-5
        dT = 2*0.49*5.6704e-8*0.1013*(Tx[j]**4-77.3**4)/(3*3930*1.3806*L*6.022)*tstep #Radiation
        # if abs(log10(a))>10:
            # print(Tx,Tx[j],a)
            # input()
        Tx[j] = Tx[j]+a*d2T[j-1]*tstep - dT #Excluding the dT term, this change is due to thermal conduction. 
    Tx[div-1]=Tx[div-2]
    Tend4[i]=Tx[div-2]
sum = 0
for k in range(steps):
    # print(Td[k],Tend4[k])
    # input()
    sum += Td[k]-Tend4[k]
print(sum/steps)
fig,ax = plt.subplots(1,1,figsize = (8,5))
ax.plot(time/60,Td)
ax.plot(time/60,Tend4)
ax.set_ylabel('Temperature (K)',fontsize = 15)
ax.set_xlabel('Time (min)',fontsize = 15)
plt.show()
fig2,bx = plt.subplots(1,1,figsize = (8,5))
bx.plot(time/60,Td - Tend4)


bx.set_ylabel('Temperature Difference (K)',fontsize = 15)
bx.set_xlabel('Time (min)',fontsize = 15)
plt.show()