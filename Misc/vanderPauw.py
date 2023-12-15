import numpy as np
from scipy.optimize import fsolve
def get_vanderPauw_resisivitiy(R1,R2,thickness):
    R_ratio = R1/R2
    if R_ratio < 1:
        R_ratio = 1/R_ratio

    VDP_func = lambda f: (np.cosh(((R_ratio-1)/(R_ratio+1))*((np.log(2))/f))-0.5*np.exp((np.log(2))/f))
    f = fsolve(VDP_func,0.5)[0]
    return (R1+R2)*f*np.pi/(2*np.log(2)*thickness) #return resisivity


print(get_vanderPauw_resisivitiy(10,1,1))