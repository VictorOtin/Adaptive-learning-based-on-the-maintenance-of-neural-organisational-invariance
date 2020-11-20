#!/usr/bin/env python

import numpy as np
import math
import matplotlib.pyplot as plt

#Solo la usamos para 
data20x20 = np.load('correlations-ising2D-size400.npy')

def coth(x):
	return np.cosh(x)/np.sinh(x)


Bc=0.5*np.log(1+2**0.5)
beta=Bc
M=(-1+(np.sinh(2*beta))**(-4))**(1/8)
theta=1/0.5*np.pi
k=2*np.sinh(2*beta)/np.cosh(2*beta)**2
U=np.zeros(1)

U = coth(2*beta)*(1+ (k*np.sinh(2*beta)-1)*np.mean(1/np.sqrt(1-(k*np.sin(theta))**2)))
Bd=0.5*U-M**2
print(Bd)
N=20
C=np.zeros((20,20))
r=np.zeros((N,N))
for x in range(-N//2,N//2):
	for y in range(-N//2,N//2):
		r[x,y] = np.sqrt(x**2+y**2)

C=Bd*r**(-(1/4))
C[0,0]=1

ind=np.triu_indices(N,1)
new_C2=C[ind]
new_C2[0]=1
filename = ('correlations-ising2D-INFINITE2.npy')
np.save(filename, new_C2)
#plt.hist(new_C,color='blue', label=['Infinite_Net'])
#plt.legend(loc='upper right')
#plt.show()
#
#plt.hist(data,color='green', label=['20x20 Net'])
#plt.legend(loc='upper right')
#plt.show()
c_inf=np.arange(20)
print(c_inf)
plt.style.use('seaborn-deep')
plt.hist([new_C2, data20x20],color=['blue','green'], label=['Infinite_Net', '20x20 Net'],density=True,bins=25)
plt.legend(loc='upper right')
plt.xlabel("Cij",fontsize=20, rotation=0, labelpad=20)
plt.ylabel("Pij",fontsize=20, rotation=0, labelpad=20)
plt.show()
#print(r)
#print(np.shape(c_inf), np.shape(new_C2[:20]))
#plt.scatter(r[:20,0],new_C2[:20],color='blue',label='Infinite_Net')
#plt.scatter(r[:20,0],data20x20[:20],color='green',label='20x20 Net')
#plt.xlabel("r")
#plt.ylabel("Cij")
#plt.legend()

plt.show()