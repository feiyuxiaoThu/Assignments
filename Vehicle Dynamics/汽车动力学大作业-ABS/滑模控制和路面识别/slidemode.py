# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:40:14 2019

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
w0 = v0/r
desiredSlip = 0.12
eta = 10
theta = 0.02
wID = 90

epsilon = 0.001

# gravity force
FN = m*g

Mb = 1500

time = 10
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
slip_a = np.zeros(size)
slip_aa = np.zeros(size)
Mb = np.zeros(size)
Mb_record = np.zeros(size)

v[0] = v0
w[0] = w0
a[0] = 0
aa[0] = 0 

#PID controller
Kp = 1000
P0 = -50
#counter for vectors
i = 0

def sign(x):
    if x > 0:
        return 1
    elif x == 0 :
        return 0
    elif x <0 :
        return -1

def sat(y):
    if abs(y) <= 1:
        return y
    elif abs(y) > 1:
        return sign(y)

for i in range(size-1):
    slipratio[i] = (v[i]-w[i]*r)/max(v[i],w[i]*r,epsilon) #calculate the slip ratio
  
    if slipratio[i] > 1:
        #print(slipratio[i],">1")
        slipratio[i] = 1
    elif slipratio[i] < 0:
        slipratio[i] = -slipratio[i]  # adjust the limits if exceeds
    
    #print(slipratio[i],i)   
    slipError[i] = abs(slipratio[i]-desiredSlip)
  
    if i > 0:
        a[i] = (v[i] - v[i-1])/h
        aa[i] = (a[i] - a[i-1])/h
        slip_a[i] = (slipratio[i] - slipratio[i-1])/h
        slip_aa[i] = (slip_a[i] - slip_a[i-1])/h
        
    if slipratio[i] < 0.2:
        u_lambda = 5 * slipratio[i]
    elif slipratio[i] > 0.2:
        u_lambda = 1.0 - 0.01*(slipratio[i]-0.2)
	
    if i < 100:
        Mb[i] = 1500
    else:         
        if i%100 == 0:
           # if i > 0:	
           Mb[i] = max(r*u_lambda*FN,100) + u_lambda*FN*I*w[i]/(m*v[i]) + I*w[i]*aa[i]/(2*v[i]*a[i])- eta*I*v[i]/(2*a[i])*sat(wID-w[i]/theta) #- I*v[i]*v[i]*slip_aa[i]/(2*r*a[i]) 
           #print("i",i,r*u_lambda*FN)
           Mb[i] = max(Mb[i],1200)
            #elif i == 0:
            #    Mb[i] = r*u_lambda*FN
        else:
            Mb[i] = Mb[i-1]
                
    # magic equation
    Mb_record[i] = Mb[i]
    #print(Mb,"Mb")
    
    u = math.sin(1.9*math.atan(10*slipratio[i]-0.97*(10*slipratio[i]-math.atan(10*slipratio[i]))))
    #u = 1.28*(1-math.exp(-23.99*slipratio[i]) - 0.52*slipratio[i]);
    
    dw = (r*u*FN - Mb[i])/I*h
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
#plt.savefig('velocity',dpi = 200)

plt.figure()
plt.plot(T[0:t_pos],slipratio[0:t_pos], label = "slipratio")
plt.legend(loc = 'best')
plt.title("Slipratio change in ABS")
#plt.savefig("slipratio",dpi = 200)

plt.figure()
plt.plot(T[0:t_pos],Mb_record[0:t_pos], label = "slipratio")

