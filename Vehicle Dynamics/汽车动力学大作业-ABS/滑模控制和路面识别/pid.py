# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:40:14 2019

@author: feiyuxiao
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 14:25:15 2018

@author: feiyuxiao
"""

import numpy as np
import math
import matplotlib.pylab as plt



# set parameters
m = 450
g = 9.8
r = 0.32
I = 1
v0 = 25
w0 = 100
desiredSlip = 0.2

epsilon = 0.05

# gravity force
FN = m*g

Mb = 1500

time = 10
# step size
h = 0.01
size = int(time/h)

v = np.zeros(size)
w = np.zeros(size)
T = np.linspace(0,time,size)
slipratio = np.zeros(size)
slipError = np.zeros(size)

v[0] = v0
w[0] = w0

#PID controller
Kp = 1000
P0 = -50
#counter for vectors
i = 0

for i in range(size-1):
    slipratio[i] = (v[i]-w[i]*r)/max(v[i],w[i]*r,epsilon) #calculate the slip ratio
    if slipratio[i] > 1:
        slipratio[i] = 1
    elif slipratio[i] < 0:
        slipratio[i] = 0  # adjust the limits if exceeds
        
    slipError[i] = abs(slipratio[i]-desiredSlip)
    
    if slipratio[i] > desiredSlip:
        Mb = Mb - Kp*slipError[i]+ P0
    elif slipratio[i] < desiredSlip:
        Mb = Mb + Kp*slipError[i] + P0
        
    # magic equation
    u = math.sin(1.9*math.atan(10*slipratio[i]
    -0.97*(10*slipratio[i]-math.atan(10*slipratio[i]))))
    #u = 1.28*(1-math.exp(-23.99*slipratio[i]) - 0.52*slipratio[i]);
    
    dw = (r*u*FN - Mb)/I*h
    w[i+1] = w[i]+dw
    
    dv = -u*FN/m*h
    v[i+1] = v[i] + dv
    
    if v[i+1] < 0:
        v[i+1] = 0
        t_pos = i+1
        break

v_w = w*r
    
plt.figure()

#plt.plot(T,v)
plt.plot(T[0:t_pos],v_w[0:t_pos],label = "V of wheel")
plt.plot(T[0:t_pos],v[0:t_pos],label = "V of vehicle")
plt.legend(loc = 'best')
plt.title('Velocity change in ABS')
plt.savefig('velocity',dpi = 200)

plt.figure()
plt.plot(T[0:t_pos],slipratio[0:t_pos], label = "slipratio")
plt.legend(loc = 'best')
plt.title("Slipratio change in ABS")
plt.savefig("slipratio",dpi = 200)



