#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:49:59 2020

@author: victor
"""


#!/usr/bin/env python

import matplotlib.ticker as ticker
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
from scipy.interpolate import splev, splrep

R=10

Iterations=1000 #1000
T=100 #5000
save=False
save=True


Nbetas=100
betas=10**np.linspace(-1,1,Nbetas)


b=0.8


mods=['n','s','i']
modlabels=[r'h',r's',r'{in}']


for im,mod in enumerate(mods[0:1]):

	sizes=[12,22,32]
	color=['b','r','g']
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
	for s,size in enumerate(sizes):
		print(s)
		for bind in range(Nbetas):
					
			Nsensors=4
			Nmotors=2
			filename='H2/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(bind)+'.npz'
			data=np.load(filename)
#			print(data['C'])
			C[s,bind]=data['C']
			H[s,:,bind]=data['Emean'] #data['H'+mod]


lines=[':','-.','-.','--','-']
fig, ax = plt.subplots(1,1,figsize=(4,3))
ax.set_xscale("log", nonposx='clip')
plt.semilogx(betas1,C[2,:],'k',color='g',label='$N_h$ 32')
plt.semilogx(betas1,C[1,:],'k',color='r',label='$N_h$ 22')
plt.semilogx(betas1,C[0,:],'k',color='b',label='$N_h$ 12')
ax.set_xticks([0.5,1, 2, 2])
plt.xlim(0.4,2)
ax.xaxis.set_minor_formatter(ticker.ScalarFormatter())
plt.ylabel(r'$C$',fontsize=20, rotation=0, labelpad=20)
plt.xlabel(r'$\beta$',fontsize=18)
plt.legend(loc='upper left',bbox_to_anchor=(1.05, 1.15), fancybox=True, shadow=True)
tickpos = [0.5,1.0,2.0]
plt.xticks(tickpos,tickpos)

plt.show()

