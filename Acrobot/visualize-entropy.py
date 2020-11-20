#!/usr/bin/env python

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
	C=np.zeros(100)
	C1=np.zeros((S,R,len(betas1)-1))
	d=np.zeros((S,Nbetas))
	sizes=[8,12,32]
	for s,size in enumerate(sizes):
		print(size)
		for bind in range(Nbetas):
					
			Nsensors=4
			Nmotors=2

			if mod=='n':
				sizem=N
			if mod=='s':
				sizem=4
			if mod=='i':
				sizem=4
			
			filename='H2/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(bind)+'.npz'
			data=np.load(filename)
			H[s,:,bind]=data['Emean'] #data['H'+mod]
		Hu[s,:,:]=H[s,:,:]/sizem

mods=['Emean'] 

for mod in mods:

	for s,size in enumerate(sizes):
		print(size)
		for bind in range(Nbetas):
			Nsensors=4 #4
			Nmotors=2 #2
			sizem=1
			filename='H2/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(bind)+'.npz'
			data=np.load(filename)
			H[s,:,bind]=data[mod]
			Hu[s,:,bind]=H[s,:,bind]/sizem

	fig, ax = plt.subplots(1,1,figsize=(4,3))
	for s,N in reversed(list(enumerate(sizes))):
		ax.set_xscale("log", nonposx='clip')
		plt.semilogx(betas,np.mean(Hu[s,:,:],axis=0),'k',color=color[s],label=labels[s])
		plt.fill_between(betas,np.percentile(Hu[s,:,:],0,axis=0), np.percentile(Hu[s,:,:],100,axis=0),color=[b,b,b])
		plt.ylabel('$H$',fontsize=20, rotation=0, labelpad=20)
		plt.xlabel(r'$\beta$',fontsize=18)
		ax.set_xticks([0.5,0.5, 1, 2])
		plt.xlim(0.4,2)
		ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
		plt.legend(bbox_to_anchor=(1.05, 1.15), fancybox=True, shadow=True)

plt.show()