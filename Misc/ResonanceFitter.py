import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import optimize

path_prefix = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/'
path_suffix = '.dat'

# filenames = [
#              'double1nf',
#             #  'double.47nf',
#             #  'double3.9nf',
#             #  '.5nfseries1nfparallel',
#             #  '2nfserise1nfparallel2',
#             #  '1nfseries3.9nfparallel'
#               ]


path_prefix = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/QFactorTesting/'
filenames = os.listdir(path_prefix)
path_suffix = ''

data_paths = []
for f in filenames:
    data_paths.append(path_prefix + f + path_suffix)

datas = []
for i, data in enumerate(data_paths):
    all_data = np.genfromtxt(data, delimiter='\t')
    datas.append({})
    datas[i]['time'] = np.array(all_data[2:,0])
    datas[i]['vx'] = 100-np.array(all_data[2:,1])*1000
    datas[i]['vy'] = -np.array(all_data[2:,2])*1000
    datas[i]['vmag'] = np.array(all_data[2:,3])*1000/100
    datas[i]['freq'] = np.array(all_data[2:,4])/1000

def ParCapmodel(fs, f0,Q,A,B):#Va across resistor with capacitor in parallel and capacitance of inductor
    return A/np.sqrt(1+4*(Q*(fs/f0-1))**2)+B

# fig1 = plt.figure(constrained_layout = True)
# ax = fig1.add_subplot(1, 1, 1)
l = []

for i in range(len(datas)):
    guesses1 = [750,10,-.3,.26]
    pbounds1 = np.array([[max(min(datas[i]['freq']),500),1,-1,-1],[min(max(datas[i]['freq']),2500),1e4,1,1]]) # [[Lower bounds],[upper bounds]]
    bestfit = optimize.curve_fit(ParCapmodel,datas[i]['freq'],datas[i]['vmag'],guesses1, bounds=pbounds1)
    bestpars1 = bestfit[0]
    inds = np.logical_not(abs(datas[i]['freq']-bestpars1[0])/bestpars1[0]>.05)
    bestfit = optimize.curve_fit(ParCapmodel,datas[i]['freq'][inds],datas[i]['vmag'][inds],bestpars1, bounds=pbounds1)
    bestpars2 = bestfit[0]
    fig1 = plt.figure(constrained_layout = True)
    ax = fig1.add_subplot(1, 1, 1)
    ax.scatter(datas[i]['freq'],datas[i]['vmag'],color='green')
    ax.plot(datas[i]['freq'],bestpars1[2]/np.sqrt(1+4*(bestpars1[1]*(datas[i]['freq']/bestpars1[0]-1))**2)+bestpars1[3])
    ax.plot(datas[i]['freq'],bestpars2[2]/np.sqrt(1+4*(bestpars2[1]*(datas[i]['freq']/bestpars2[0]-1))**2)+bestpars2[3])

    print(bestpars1,bestpars2)
    # l.append(filenames[i])
    # l.append('Fit')
    # l.append('Fit2')
    ax.legend([filenames[i],'Full Data Range Fit','Refined Fit'])
    ax.set_xlabel('Frequency (kHz)')
    ax.set_ylabel('Voltage Magnitude (mV)')
    ax.set_title('Lorenzian Fit for '+filenames[i])

# ax.set_xlabel('Frequency (kHz)')
# ax.set_ylabel('Voltage Magnitude (mV)')    
# ax.legend(l)
# ax.set_title('Lorenzian Fit')
plt.show()