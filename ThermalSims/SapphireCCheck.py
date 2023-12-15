import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

P1s = [-0.5147e+01, 0.34127,-0.333446e-01/2,0.450764e-02/6,-0.51464e-03/24,0.397864e-04/120,-0.152136e-05/720]
P2s = [0.6966,0.59387e-01,0.40357e-02/2,0.95173e-04/6,-0.35910e-05/24,-0.6498e-07/120,0.4089e-08/720]
P3s = [0.21993e02,0.38853,0.13955e-02/2,-0.83967e-04/6,0.19133e-05/24,-0.31778e-07/120,0.29562e-09/720]


filepath = '/Users/blake/Documents/ContactlessProbeData/SapphireCData.csv'
probe_dat = pd.read_csv(filepath) #Retrieve data
data = probe_dat.to_numpy()

T = np.arange(272., 320., 1.)
C = []
for i in range(T.size):
    if T[i] < 45 and T[i] > 8.610:
        C.append(1000/101.9613*(math.exp(P1s[0]*(T[i] - 8.61)**0 + P1s[1]*(T[i] - 8.61)**1 + P1s[2]*(T[i] - 8.61)**2 + P1s[3]*(T[i] - 8.61)**3 + P1s[4]*(T[i] - 8.61)**4 + P1s[5]*(T[i] - 8.61)**5 + P1s[6]*(T[i] - 8.61)**6)))
    elif T[i] >= 45 and T[i] < 125:
        C.append(1000/101.9613*(P2s[0]*(T[i] - 40)**0 + P2s[1]*(T[i] - 40)**1 + P2s[2]*(T[i] - 40)**2 + P2s[3]*(T[i] - 40)**3 + P2s[4]*(T[i] - 40)**4 + P2s[5]*(T[i] - 40)**5 + P2s[6]*(T[i] - 40)**6))
    elif T[i] > 125:
        C.append(1000/101.9613*(P3s[0]*(T[i] - 125)**0 + P3s[1]*(T[i] - 125)**1 + P3s[2]*(T[i] - 125)**2 + P3s[3]*(T[i] - 125)**3 + P3s[4]*(T[i] - 125)**4 + P3s[5]*(T[i] - 125)**5 + P3s[6]*(T[i] - 125)**6))
# C.append(1000/101.9613*(P3s[0]*(273 - 125)**0 + P3s[1]*(273 - 125)**1 + P3s[2]*(273 - 125)**2 + P3s[3]*(273 - 125)**3 + P3s[4]*(273 - 125)**4 + P3s[5]*(273 - 125)**5 + P3s[6]*(273 - 125)**6))
plt.title('Specific Heat Data and Fit')
plt.plot(data[20:26,0],data[20:26,2],T,C)
plt.ylabel('Sapphire Specific Heat (J/[Kg*K])')
plt.xlabel('Temperature (K)')
plt.show()