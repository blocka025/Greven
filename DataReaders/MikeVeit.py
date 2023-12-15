import numpy as np
import matplotlib.pyplot as plt
data_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/MikeVeitResistivityasgrown.csv'
data = np.loadtxt(data_path,delimiter=",", dtype=np.float64)
print(data)
temp = data[:,0] # kelvin
res = data[:,1] #mohm cm = 1000 micro ohm cm

fig = plt.figure(constrained_layout = True)
ax = fig.add_subplot(1, 1, 1)
ax.scatter(temp,res)
plt.show()