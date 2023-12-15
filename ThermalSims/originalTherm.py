import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
# %matplotlib inline
"""WARNING: TAKES A LONG TIME TO RUN"""
steps= 500000 #Number of time steps
time = np.linspace(-150,2000,steps)
tstep = 2000/steps
Td = -3.3476*10**(-8)*time**3+1.67*10**(-4)*time**2-0.28945*time+257.38 #Temperature of the copper (read from the temperature sensor)
a = 2.4667*10**(-10)*Td**2 - 1.1679*10**(-7)*Td + 1.942*10**(-5) #Sapphire Thermal diffusivity 
#https://www.researchgate.net/figure/Calibrated-thermal-diffusivity-of-Al2O3-sapphire-with-temperature-using-Parker-4_fig3_338658084
div = 40 #Consider 40 chunks of the sapphire rod
Tx = np.zeros(div) 
Tx[0] = Td[0] #Assume that the rod starts at room temperature 
for k in range(div-1):
    Tx[k+1]=Td[0]
L = 1.255*0.0254 #sapphire rod length in m
L_step = L/div
Tend4 = np.zeros(steps) #Simulated temperature at the end of the rod (away from the temp sensor end)
for i in range(steps):
    d2T = np.zeros(div-2)
    for j in range(div-2):
        A = (Tx[j+2]-Tx[j+1])/L_step
        B = (Tx[j+1]-Tx[j])/L_step
        d2T[j]= (A-B)/(L_step)
    dT = 2*0.49*5.6704*10**(-8)*0.1013*(Td[i]**4-77.3**4)/(3*3930*1.3806*L*6.022)*tstep #Radiation
    for j in range(div):
        a=2.4667*10**(-10)*Tx**2 - 1.1679*10**(-7)*Tx + 1.942*10**(-5)
        # if abs(math.log10(a[j])+5) > 5:
        #     print(Tx,Tx[j],a)
        #     input()
        if j == 0:
            Tx[j] = Td[i]
        elif ((j>0)and(j<(div-1))):
            Tx[j] = Tx[j]+a[j]*d2T[j-1]*tstep - dT #Excluding the dT term, this change is due to thermal conduction. 
        elif (j==(div-1)):
            Tx[j]=Tx[j-1]
            Tend4[i]=Tx[j-1]
fig,ax = plt.subplots(1,1,figsize = (8,5))
ax.plot(time/60,Td)
ax.plot(time/60,Tend4)
ax.legend(['Copper block','End of sapphire'])
plt.show()