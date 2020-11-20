#!/usr/bin/env python

from embodied_ising2 import ising,bool2int
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from swimmer import SwimmerEnv
import random

N=64

ind=0

#beta=1.2
beta=2
visualize=True
# visualize=False

size = 4 #int(argv[1])
Nsensors = 8 #int(argv[2])
Nmotors = 2 #int(argv[3])
T = 1000 #int(argv[4])
Iterations = 100 #int(argv[5])
repetitions = 100 #int(argv[6])

I=ising(size,Nsensors,Nmotors)
I.Beta=beta



filename='files/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-ind_'+str(ind)+'.npz'
print(filename)
data=np.load(filename)

I.h=data['h']
I.J=data['J']

T=8000*2
if beta>1:
	T*=5
p=np.zeros(T)
s=np.zeros(T)
m=np.zeros(T)
h=np.zeros(T)
a=np.zeros(T)
n=np.zeros(T,int)
spins=np.zeros((size,T))
spd_x=np.zeros(T)
spd_y=np.zeros(T)

pos_x=np.zeros(T)
pos_y=np.zeros(T)
Index_pos_x=np.zeros(T)
Index_pos_y=np.zeros(T)
height=np.zeros(T)

nsize=size
I.env.reset()
#print(I.env.sim.data.qpos[0,])
#print(I.env.sim.data.qpos[1,])
T0=10000

for t in range(T0):
	I.SequentialUpdate()
T=500
for t in range(T):
	I.SequentialUpdate()
	s[t]=I.get_state_index('input')
	a[t]=I.get_state_index('non-sensors')
	h[t]=I.get_state_index('hidden')
	m[t]=I.get_state_index('motors')
	spd_x[t]=I.speed_x
	spd_y[t]=I.speed_y
	pos_x[t]=I.env.sim.data.qpos[0,]
	pos_y[t]=I.env.sim.data.qpos[1,]
	Index_pos_x[t]=I.body_pos_x
	Index_pos_y[t]=I.body_pos_y
print(pos_x[:5])
print(pos_y[:5])

fig, ax = plt.subplots(1,1,figsize=(4.6,3.8))
plt.plot(pos_x,pos_y,'k')
plt.ylabel(r'$y$',fontsize=18, rotation=0)
plt.xlabel(r'$x$',fontsize=18)
plt.axis([-10,10,-10,10])
np.save('00',(pos_x,pos_y))

plt.show()