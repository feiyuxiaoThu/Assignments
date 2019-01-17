ng # -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:36:59 2019

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
flag = 1

Mb_base = 4000 #2000 #5000
step = 1000 #500 #1000
dM = Mb_base/step # 0.02s

# gravity force
FN = m*g

time = 10
# step size
h = 0.0001
size = int(time/h)

v = np.zeros(size)
w = np.zeros(size)
T = np.linspace(0,time,size)
w_a = np.zeros(size)
w_aa = np.zeros(size) # aa is the dereviate of a
slipratio = np.zeros(size)
slipError = np.zeros(size)
slip_a = np.zeros(size)
slip_aa = np.zeros(size)
Mb = np.zeros(size)
a = np.zeros(size)

sym = np.zeros(size)

v[0] = v0
w[0] = w0
a[0] = 0


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
    slipratio[i] = (v[i]-w[i]*r)/max(v[i],w[i]*r) #calculate the slip ratio
    
    if slipratio[i] > 1:
        #print(slipratio[i],">1")
        slipratio[i] = 1
    elif slipratio[i] < 0:
        slipratio[i] = slipratio[i]  # adjust the limits if exceeds
  
    if i > 0:
        w_a[i] = (w[i] - w[i-1])/h
        a[i] = (v[i] - v[i-1])/h
        w_aa[i] = (w_a[i] - w_a[i-1])/h
        slip_a[i] = (slipratio[i] - slipratio[i-1])/h
        slip_aa[i] = (slip_a[i] - slip_a[i-1])/h
    
    #u = 1.28*(1-math.exp(-23.99*slipratio[i]) - 0.52*slipratio[i]);  
    
    if i<step:
        
        Mb[i] = Mb[i-1] + dM
    else:
        
        Mb[i] = Mb[i-1]
                
  
    
    if flag == 0:    
        u = math.sin(1.9*math.atan(10*slipratio[i]-0.97*(10*slipratio[i]-math.atan(10*slipratio[i]))))
    else:
        u = 0.5*math.sin(1.9*math.atan(10*2*slipratio[i]-0.97*(10*2*slipratio[i]-math.atan(10*2*slipratio[i]))))
    #u = 1.28*(1-math.exp(-23.99*slipratio[i]) - 0.52*slipratio[i]);
    
    if i > 0:
        sym[i] = (I*w_aa[i]+((Mb[i]-Mb[i-1])/h))/(w[i]*r*a[i]-v[i]*r*w_a[i])
    if sym[i] < 0:
        sign_i = i-1
        t_pos = sign_i
        break
    
    dw = (r*u*FN - Mb[i])/I*h
    w[i+1] = w[i]+dw
    
    dv = -u*FN/m*h
    v[i+1] = v[i] + dv
    
    if w[i]*r < 0:
        t_pos = i+1
        break
    
    if v[i+1] < 0.2:
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
plt.plot(T[0:t_pos],Mb[0:t_pos], label = "Mb")
plt.title("Mb")


plt.figure()
plt.plot(T[0:t_pos],sym[0:t_pos], label = "du/dlambda")
plt.title("du/dlambda")

print('lambda',slipratio[sign_i])
x = np.arange(0,1,0.01)
y = np.zeros(100)
yy = np.zeros(100)

for i in range(100):
    y[i] = math.sin(1.9*math.atan(10*x[i]-0.97*(10*x[i]-math.atan(10*x[i]))))
    yy[i] = 0.5*math.sin(1.9*math.atan(10*2*x[i]-0.97*(10*2*x[i]-math.atan(10*2*x[i]))))

plt.figure()
plt.plot(x,y)
plt.plot(x,yy)