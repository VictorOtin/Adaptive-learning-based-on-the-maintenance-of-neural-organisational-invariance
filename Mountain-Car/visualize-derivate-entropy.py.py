#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:49:59 2020

@author: victor
"""


#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from scipy.interpolate import splev, splrep

#plt.rc('text', usetex=True)
#font = {'size':15}
#plt.rc('font',**font)
#plt.rc('legend',**{'fontsize':14})


R=10

Iterations=1000 #1000
T=1000 #5000
save=False
save=True


Nbetas=100
betas=10**np.linspace(-1,1,Nbetas)


b=0.8
#size=64

mods=['n','s','i']
modlabels=[r'h',r's',r'{in}']



for im,mod in enumerate(mods[0:1]):
	
	sizes=[16,32,64]
	S=len(sizes)
	lines=[':','-.','-.','--','-']
	dashes=[(1,2),(2,2),(4,2),(6,2,2,2),(None,None)]
	labels=[]
	for s in sizes:
		labels+=[r'$N_h='+str(s)+'$']
	H=np.zeros((S,R,Nbetas))
	Hu=np.zeros((S,R,Nbetas))
	dB=0.02
	betas1 = np.arange(0, 2, dB)
	betas2=0.5*(betas1[0:-1]+betas1[1:])
	H1=np.zeros((S,R,len(betas1)))
#	C=np.zeros((S,R,len(betas1)))
	C=np.zeros((3,100))
	C1=np.zeros((S,R,len(betas1)-1))
	d=np.zeros((S,Nbetas))
	for s,N in enumerate(sizes):
		print(N)
		for bind in range(Nbetas):
			Nsensors=4
			Nmotors=2
#			size=64 #N+Nsensors+Nmotors

			if mod=='n':
				sizem=N
			if mod=='s':
				sizem=4
			if mod=='i':
				sizem=4
			
			filename='Hheight/network-size_'+str(N)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(bind)+'.npz'
			data=np.load(filename)
			C[s,bind]=data['C']

lines=[':','-.','-.','--','-']
fig, ax = plt.subplots(1,1,figsize=(4,3))
#ax.set_xscale("log", nonposx='clip')
plt.plot(betas1,C[2,:],'k',color='g',label='$N_h$ 64')
plt.plot(betas1,C[1,:],'k',color='r',label='$N_h$ 32')
plt.plot(betas1,C[0,:],'k',color='b',label='$N_h$ 16')
#plt.fill_between(betas2,np.percentile(C[s,:,:],0,axis=0), np.percentile(C[s,:,:],100,axis=0),color=[b,b,b])
plt.ylabel(r'$C$',fontsize=20, rotation=0, labelpad=20)
plt.xlabel(r'$\beta$',fontsize=18)
ax.set_xticks([0.5,1, 2, 4])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.legend(loc='upper left',bbox_to_anchor=(1.05, 1.15), fancybox=True, shadow=True)

plt.axis([0,2,0,100])

plt.show()



