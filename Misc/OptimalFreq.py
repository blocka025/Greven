import math
radius = 0.096/2*25.4#radius in mm
s = radius*(math.pi**.5)
print(s,radius**2 * math.pi,s**2)
rho = float(input('Resistivity (ohm m) = '))
side = float(input('Side Length (mm) = '))
mu = 4e-7*math.pi
ratio = 0.34035954520036005
freq = rho/((ratio*side*1e-3)**2*math.pi*mu)
if freq/1e6>=1:
    print(freq/1e6,' MHz')
else:
    print(freq/1e3,' kHz')

#equation is skin depth = [2*rho/(mu* angluar frequency)]^(.5)
#the optimal skin depth to side length ratio is 0.34035954520036005

#Sapphire rod is .1205in in diamter

#this is all incorrect