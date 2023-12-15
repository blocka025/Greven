import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

data_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/VideoTemps/2023-10-10 14-34-51_big.dat'
data_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/VideoTemps/2023-10-10 14-34-51.dat'
all_data = np.genfromtxt(data_path,delimiter='\t',skip_header=1)
#indexes = np.logical_and(all_data2[:,1] >= T1.min(), all_data2[:,1] <= 105)
t1 = np.array(all_data[:,0])
T1 = np.array(all_data[:,1])

dT1 = np.gradient(T1,t1)
thres =400
ind1 = np.logical_and(t1<1100, abs(dT1)<thres)
ind2 = np.logical_and(T1>200, abs(dT1)>=thres)
badinds = np.logical_and(T1>296, t1<1110)
print('There are '+str(len(t1[badinds]))+ ' outliers')
print(str(len(t1[ind2]))+ ' points have been filtered')

t2 = t1[ind2]
T2 = T1[ind2]
dT2 = dT1[ind2]

t1 = t1[ind1]
T1 = T1[ind1]
dT1 = dT1[ind1]

res = 50000
evenly_spaced_time = np.zeros(res,dtype=np.float64)
evenly_spaced_temp = np.zeros(res,dtype=np.float64)
total_time = (t1[-1]-t1[0])
for i in range(res):
    index = np.searchsorted(t1, i/res*total_time)
    evenly_spaced_time[i] = t1[index]
    evenly_spaced_temp[i] = T1[index]


fig = plt.figure(constrained_layout = True)
ax = fig.add_subplot(1, 1, 1)
ax.plot(t1,T1,marker='o')
ax.plot(evenly_spaced_time,evenly_spaced_temp,marker='o')
# ax.plot(t2,T2,marker='o')
# bx = ax.twinx()
# bx.plot(t1,dT1,marker='o',color='red')

ax.set_ylabel('Time (Min)',fontsize = 15)
ax.set_xlabel('Temperature [C]',fontsize = 15)
ax.legend(['Temperature Reading'])


l = len(t1)
time_amps = fft(evenly_spaced_time)[1:l//2]
temp_amps = fft(evenly_spaced_temp)[1:l//2]
total_time = (t1[-1]-t1[0])
freqs = fftfreq(l, total_time/l)[1:l//2]

fig2 = plt.figure(constrained_layout = True)
ex = fig2.add_subplot(1, 1, 1)
ex.scatter(freqs,np.absolute(temp_amps),s=2)
# ex.scatter(freqs,np.absolute(np.real(time_amps)),s=2)
ex.set_yscale('log')


plt.show()