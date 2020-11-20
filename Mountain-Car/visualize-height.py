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


R=100

Iterations=1000 #1000
T=1000 #5000
save=False
save=True
N=20

Nbetas=100
betas=10**np.linspace(-1,1,Nbetas)


b=0.8


mods=['n','s','i']
modlabels=[r'h',r's',r'{in}']



for im,mod in enumerate(mods[0:1]):
	
	sizes=[16,32,64]
	S=len(sizes)
	lines=[':','-.','-.','--','-']
#	dashes=['blue','red','green']
#	dashes=[(1,2),(2,2),(4,2),(6,2,2,2),(None,None)]
	color=['b','r','g']
	labels=[]
	for s in sizes:
		labels+=[r'$N_h='+str(s)+'$']
	H=np.zeros((S,R,Nbetas))
	Hu=np.zeros((S,R,Nbetas))
	dB=0.02
	betas1 = np.arange(0, 2, dB)
	betas2=0.5*(betas1[0:-1]+betas1[1:])
	H1=np.zeros((S,R,len(betas1)))
	C=np.zeros((S,R,len(betas2)))
#	C=np.zeros(100)
	C1=np.zeros((S,R,len(betas1)-1))
	d=np.zeros((S,Nbetas))

mods=['ymean'] 

for mod in mods:
	print(mod)
	for s,size in enumerate(sizes):

		print(s,'######',N)
		for bind in range(Nbetas):

			Nsensors=4 #4
			Nmotors=2 #2
#			size=64 #N+Nsensors+Nmotors
			sizem=1
			filename='Hheight/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(bind)+'.npz'
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
		ax.set_xticks([0.5,1, 2, 2])
		plt.xlim(0.4,2)
		ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
		plt.legend(bbox_to_anchor=(1.05, 1.15), fancybox=True, shadow=True)

#	plt.axis([-5,30**0.8,np.min(Hu),np.max(Hu)*1.05])
	if save:
		if mod=='y':
			plt.savefig('img2/INFfig7a.eps',bbox_inches='tight')

	for s,N in enumerate(sizes):

		Nsensors=4 #4
		Nmotors=2 #2
#		size=64 #N+Nsensors+Nmotors
		sizem=1

		for ind in range(R):
			smoothness=0.1
			tck = splrep(np.log(betas), H[s,ind,:],s=smoothness)#,w=1/d[s,:])
			H1[s,ind,:] = splev(np.log(betas1), tck)/sizem
			C[s,ind,:] = np.diff(H1[s,ind,:])/dB*betas2

	fig, ax = plt.subplots(1,1,figsize=(4,3))
	for s,N in reversed(list(enumerate(sizes))):
		ax.set_xscale("log", nonposx='clip')
		plt.semilogx(betas1,np.mean(H1[s,:,:],axis=0),'k',color=color[s],label=labels[s])
		plt.fill_between(betas1,np.percentile(H1[s,:,:],0,axis=0), np.percentile(H1[s,:,:],100,axis=0),color=[b,b,b])
		plt.ylabel('$y$',fontsize=20, rotation=0, labelpad=20)
		plt.xlabel(r'$\beta$',fontsize=18)
		ax.set_xticks([0.5,1, 2, 4])
		ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
		plt.legend(bbox_to_anchor=(1.05, 1.15), fancybox=True, shadow=True)
	plt.axis([0.2,2,-1.5,1.5])

	fig, ax = plt.subplots(1,1,figsize=(4,3))
	for s,N in reversed(list(enumerate(sizes))):
		ax.set_xscale("log", nonposx='clip')
		plt.semilogx(betas2,np.mean(C[s,:,:],axis=0),'k',color=color[s],label=labels[s])
		plt.fill_between(betas2,np.percentile(C[s,:,:],0,axis=0), np.percentile(C[s,:,:],100,axis=0),color=[b,b,b])
		plt.ylabel(r'$\chi_y'+'$',fontsize=20, rotation=0, labelpad=20)
		plt.xlabel(r'$\beta$',fontsize=18)
		ax.set_xticks([0.5,1, 2, 4])
		ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
		plt.legend(bbox_to_anchor=(1.05, 1.15), fancybox=True, shadow=True)
#	plt.axis([1,2,-3,np.max(C[-1,:,100:-100])*1.05])
	plt.xlim(0.19,2)
	if save:
		if mod=='y':
			plt.savefig('img2/fig7c.eps',bbox_inches='tight')
plt.show()