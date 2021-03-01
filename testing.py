import numpy as np
from scipy.integrate import quad

def f(x, s):
    return(1/(x**2)) #put your function to integrate here

print(quad(lambda x: f(x, 1),1,np.Infinity))