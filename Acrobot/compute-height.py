#!/usr/bin/env python

from embodied_ising import ising
import numpy as np
import matplotlib.pyplot as plt
from info_theory import Entropy
from sys import argv
from sympy import *
from numpy import diff



#if len(argv) < 3:
 #   print("Usage: " + argv[0] + " <N> + <bind>")
  #  exit(1)

N=10 #int(argv[1])
#bind=100 #int(argv[2])
size=22 #6*N
Nsensors=4 #2*N
Nmotors=2 #N

R=100

Nbetas=100
betas=10**np.linspace(-1,1,Nbetas)
Ha=np.zeros(R)
Hn=np.zeros(R)
Hs=np.zeros(R)
Hp=np.zeros(R)

Iterations=1000 #1000
T=100 #5000
T1=100000*size

for bind in range(100):
    print()
    print(betas[bind],size)
    ymean=[]
    Energy=[]
    Energy2=[]
    Esquare=np.zeros(T1)
    I=ising(size,Nsensors,Nmotors)
    filename='files/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_1000-Iterations_'+str(Iterations)+'-ind_'+str(bind)+'.npz'
    
    data=np.load(filename)
    I.h=data['h']
    I.J=data['J']
    I.randomize_state()
    beta=betas[bind]
    I.Beta=betas[bind]
    T1=100000*size
#    ypos=np.zeros(T1)
    E=np.zeros(T1)

    t=0
    I.randomize_position()
    T0=int(T1/10)
    for t0 in range(T0):
        I.SequentialUpdate()
    
    F=0
    for t in range(T1):
        I.SequentialUpdate()
#        ypos[t]=I.height
#        function= ypos[t]
        E[t]= - np.dot(I.h, I.s) -  np.dot(I.s, np.dot(I.J, I.s))
        Esquare[t]=E[t]**2
#    ymean+=[np.mean(ypos)]
    Emean=np.mean(E)
    Emean2=Emean**2
    E2=np.mean(Esquare)
    C=((I.Beta)**2)*(E2-Emean2)
    #C=beta**2*(Energy2-Energy**2)
    print('Emean',Emean,'C',C)
    
    filename='H2/network-size_'+str(size)+'-sensors_'+str(Nsensors)+'-motors_'+str(Nmotors)+'-T_'+str(T)+'-Iterations_'+str(Iterations)+'-bind_'+str(bind)+'.npz'
    np.savez(filename,betas=betas,Nbetas=Nbetas,ymean=ymean,Emean=Emean,C=C)