# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:36:59 2019

@author: feiyuxiao
"""

import numpy as np
import math
import matplotlib.pylab as plt
import random

# set parameters
m = 380
g = 9.8
r = 0.325

I = 1.7
v0 = 20
w0 = v0/r
#desiredSlip = 0.075
#flag = 1 # flag 1 low mu  flag 0 high mu

K = 8000

# gravity force
FN = m*g

time = 8
# step size
h = 0.0001
size = int(time/h)

v = np.zeros(size)
w = np.zeros(size)
T = np.linspace(0,time,size)
a = np.zeros(size)
aa = np.zeros(size) # aa is the dereviate of a
slipratio = np.zeros(size)
slipError = np.zeros(size)

Mb = np.zeros(size)

v[0] = v0
w[0] = w0


i = 0

for i in range(size-1):
  
    if i < 10000:
        flag = 0
        desiredSlip = 0.15
    elif i >= 10000:
        flag = 1
        desiredSlip = 0.075
    
    slipratio[i] = (v[i]-w[i]*r)/v[i] #calculate the slip ratio

    slipError[i] = slipratio[i] - desiredSlip# e
    
    if flag == 0:
        if slipratio[i] < 0.15:
            u_lambda = slipratio[i]/0.15
        elif slipratio[i] >= 0.15:
            u_lambda = 1.0 - 0.1*(slipratio[i]-0.15)/(1-0.15)
    elif flag == 1:
         if slipratio[i] < 0.075:
            u_lambda = 0.5 * slipratio[i]/0.075
         elif slipratio[i] >= 0.075:
            u_lambda = 0.5 - 0.1*(slipratio[i]-0.075)/(1-0.075)
            
          
    if i%100 == 0:
        '''
        K = 400
        theta = 0.5
        Mb[i] = I*u_lambda*g*(1-slipratio[i])/r + u_lambda*m*g*r - K*sat(slipError[i],theta)
        '''
        Mb[i] = I*u_lambda*g*(1-slipratio[i])/r + u_lambda*m*g*r - K*slipError[i]
        print("u",u_lambda,slipratio[i])
    else:
        Mb[i] = Mb[i-1]
            
    
    if flag == 0:    
        u = math.sin(1.9*math.atan(10*slipratio[i]-0.97*(10*slipratio[i]-math.atan(10*slipratio[i])))) 
        u = (1 + 0.01*random.randint(5,10))*u
    elif flag == 1:
        u = 0.5*math.sin(1.9*math.atan(10*2*slipratio[i]-0.97*(10*2*slipratio[i]-math.atan(10*2*slipratio[i]))))
        u = (1 + 0.01*random.randint(5,10))*u
    #u = 1.28*(1-math.exp(-23.99*slipratio[i]) - 0.52*slipratio[i]);
    
    dw = (r*u*FN - Mb[i])/I*h
    w[i+1] = w[i]+dw
    
    dv = -u*FN/m*h
    v[i+1] = v[i] + dv
    
    if v[i+1] < 0.05:
        v[i+1] = 0
        t_pos = i+1
        break

v_w = w*r
    
plt.figure()
plt.plot(T[0:t_pos],v_w[0:t_pos],label = "V of wheel")
plt.plot(T[0:t_pos],v[0:t_pos],label = "V of vehicle")
plt.legend(loc = 'best')
plt.title('Velocity change in ABS')
plt.show()
plt.savefig('velocity_slidemode.png',dpi = 200)

plt.figure()
plt.plot(T[0:t_pos],slipratio[0:t_pos], label = "slipratio")
plt.legend(loc = 'best')
plt.title("Slipratio change in ABS")
plt.show()
plt.savefig("slipratio_slidemode.png",dpi = 200)

plt.figure()
plt.plot(T[0:t_pos],Mb[0:t_pos], label = "Mb")
plt.title("Mb_slidemode")
plt.show()
plt.savefig("Mb_slidemode.png",dpi = 200)


x = np.arange(0,1,0.01)
y = np.zeros(100)
yy = np.zeros(100)
z = np.zeros(100)
zz = np.zeros(100)
for i in range(100):
    y[i] = math.sin(1.9*math.atan(10*x[i]-0.97*(10*x[i]-math.atan(10*x[i]))))
    yy[i] = 0.5*math.sin(1.9*math.atan(10*2*x[i]-0.97*(10*2*x[i]-math.atan(10*2*x[i]))))
    if x[i] <= 0.15:
        z[i] = x[i]/0.15

    elif x[i] > 0.15:
        z[i] = 1.0 - 0.1*(x[i]-0.15)/(1-0.15)
     
    if x[i] <= 0.075:
        zz[i] = 0.5*x[i]/0.075
    elif x[i] > 0.075:
        zz[i] = 0.5 - 0.1*(x[i]-0.075)/(1-0.075)

plt.figure()
plt.plot(x,y)
plt.plot(x,yy)
plt.plot(x,z)
plt.plot(x,zz)
plt.title("The equation of tile")
plt.savefig("mu-slip.png",dpi = 200)
