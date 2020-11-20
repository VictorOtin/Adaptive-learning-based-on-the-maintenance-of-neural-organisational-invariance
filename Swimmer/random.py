# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from swimmer import SwimmerEnv
import random
T = 100

env=SwimmerEnv()

pos_x=np.zeros((T))
pos_y=np.zeros((T))
for t in range(T):
    print(env.action_space.sample())
    env.step(env.action_space.sample())
    pos_x[t]=env.sim.data.qpos[0,]
    pos_y[t]=env.sim.data.qpos[1,]
#    print(pos_x[t])
    #plt.rc('text', usetex=True)
print(pos_x[:5])
print(pos_y[:5])
np.save('1',(pos_x,pos_y))

fig, ax = plt.subplots(1,1,figsize=(4.6,3.8))
plt.plot(pos_x,pos_y,'k')
plt.ylabel(r'$y$',fontsize=18, rotation=0)
plt.xlabel(r'$x$',fontsize=18)
#plt.title(r'$\beta='+str(beta)+'$',fontsize=36)
plt.axis([-10,10,-10,10])
pos_x=np.zeros((T))
pos_y=np.zeros((T))
plt.show()