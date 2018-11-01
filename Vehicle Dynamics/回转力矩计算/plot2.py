# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:34:08 2018

@author: feiyuxiao
"""
import sympy
from sympy import Symbol
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

pi = 3.1416
sns.set(style="darkgrid", palette="muted", color_codes=True)

x=Symbol('x')


k = 81000/(0.8*8000)
Ey = 0.1
l = 0.3
def g(rad):
    theta = k * math.tan(rad)
    return math.exp(-(theta+Ey*theta**3))

size = 100

kk1 = 0.8*8000/(2*l**3)
kk2 = 0.8*0.01*0.36*8000/0.3
kk3 = -0.8*pi*0.01*8000*0.36/(12*l*l)
def M(x):
    return kk1*(x**4 - 10*l*x**3 -4.5*l**2*x**2 + 2.5*l**3*x + 17*l**4/16) \
+ kk2*(-0.5*l + l*math.sin(2*pi*x/l)/(2*pi)+x*math.cos(2*pi*x/l)) \
+kk3*(8*x**2 -2*l*x -l*l)*math.sin(2*pi*x/l)


angle = np.zeros(size)
angle_theta = np.zeros(size)
x0 = np.zeros(size)
M0 = np.zeros(size)

for i in range(size):
    angle[i] = i*(pi/(3*size))
    angle_theta[i] = 60*i/size

F1 = -8*0.01*0.36*l*l
F2 = -4*pi*0.01*0.36*l
F0 = 2*pi/l

   
for i in range(size):    
    f =  8 * x**3 - 12*l*x**2 + 6*l*l*x + l*l*l*(8*g(angle[i])-1) \
    + F1*(1+sympy.cos(F0*x))  + F2*(2*x-l)*sympy.sin(F0*x)
    ffunc = sympy.diff(f, x)

    begin = 1
    end = 2
    
    MAXSTEP = 100
    
    step_count = 0
    
    xx0 = random.uniform(begin, end)
    temp = f.subs(x, xx0)
    
    while step_count < MAXSTEP and abs(temp) > 1e-10:
        xx0 = xx0 - (temp / (ffunc.subs(x, xx0)))
        temp = f.subs(x, xx0)
        step_count += 1
    x0[i] = xx0
    #print(step_count)
    M0[i] = M(x0[i])
    
plt.figure()
plt.plot(angle_theta,x0)
plt.xlabel("angel")
plt.title("Position of x0")
plt.savefig("2-1.png",dpi=200)

plt.figure()
plt.plot(angle_theta,M0)
plt.xlabel("angel")
plt.title("alignment torque")
plt.savefig("2-2.png",dpi=200)

    