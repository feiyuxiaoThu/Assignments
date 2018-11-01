# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:34:08 2018

@author: feiyuxiao
"""
from sympy.solvers import solve
from sympy import Symbol
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid", palette="muted", color_codes=True)

x=Symbol('x')


k = 81000/(0.8*8000)
Ey = 0.1
l = 0.3
def g(rad):
    theta = k * math.tan(rad)
    return math.exp(-(theta+Ey*theta**3))

size = 100

kk = 0.8*8000/(2*l**3)
def M(x):
    return kk*(x**4 - 10*l*x**3 -4.5*l**2*x**2 + 2.5*l**3*x + 17*l**4/16)


angle = np.zeros(size)
angle_theta = np.zeros(size)
x0 = np.zeros(size)
M0 = np.zeros(size)

for i in range(size):
    angle[i] = i*(math.pi/(3*size))
    angle_theta[i] = 60*i/size

for i in range(size):    
    f =  8 * x**3 - 12*l*x**2 + 6*l*l*x + l*l*l*(8*g(angle[i])-1)
    s=solve(f, x)
    x0[i] = s[0]
    M0[i] = M(x0[i])
    
plt.figure()
plt.plot(angle_theta,x0)
plt.xlabel("angel")
plt.title("Position of x0")
plt.savefig("1-1.png",dpi=200)

plt.figure()
plt.plot(angle_theta,M0)
plt.xlabel("angel")
plt.title("alignment torque")
plt.savefig("1-2.png",dpi=200)

    