import math
rho = float(input('Resistivity (ohm m) = '))
frequency = float(input('Frequency (kHz) = '))
mu = 4e-7*math.pi
depth = math.sqrt(rho/(math.pi*frequency*1000*mu))
if depth >10e-3:
    print(depth, ' m')
else:
    print(depth*1e3, ' mm')
#equation is [2*rho/(mu* angluar frequency)]^(.5)