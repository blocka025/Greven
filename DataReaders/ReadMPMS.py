import numpy as np
import matplotlib.pyplot as plt

data_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/BW60_ZFC_FCC_FCW_rpt.dc.dat'
all_data = np.genfromtxt(data_path,delimiter=',')
# t1 = np.array(all_data[1:,0])
# field = np.array(all_data1[1:,2])

T1 = np.array(all_data[:,3])
ind1 = np.logical_and(T1 >= 50, T1 <= 120)
T1 = T1[ind1]
moment = np.array(all_data[0:,4])
moment = (moment[ind1] - moment[ind1].max())/-moment[ind1].min()

fig = plt.figure(constrained_layout = True)
ax = fig.add_subplot(1, 1, 1)
indie = 65
ax.scatter(T1[:indie],moment[:indie],color='blue')
ax.set_ylabel(r'Magnetic Susceptibility $\chi_{DC}$',fontsize = 15)
ax.set_xlabel('Temperature [K]',fontsize = 15)
ax.set_title(r'SQUID Measurement of $\chi_{DC}$',fontsize = 18)
plt.show()