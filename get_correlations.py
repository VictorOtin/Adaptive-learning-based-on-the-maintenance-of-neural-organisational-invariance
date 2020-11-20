import numpy as np
from matplotlib import pyplot as plt
import math


def coth(x):
	return np.cosh(x)/np.sinh(x)

#RED INFINITA
Bc=0.5*np.log(1+2**0.5)
beta=Bc
M=(-1+(np.sinh(2*beta))**(-4))**(1/8)
theta=1/0.5*np.pi
k=2*np.sinh(2*beta)/np.cosh(2*beta)**2
U=np.zeros(1)

U = coth(2*beta)*(1+ (k*np.sinh(2*beta)-1)*np.mean(1/np.sqrt(1-(k*np.sin(theta))**2)))
Bd=0.5*U-M**2

N=20			# lado del cuadrado
ind = np.triu_indices(N, 1)							# Coge los índices del triángulo superior derecho
c_values=np.load("correlations-ising2D-INFINITE.npy")	#carga valores de correlacions
c=np.zeros((N,N))									#Crea la matriz de 400x400
c[ind] = c_values										# asigna el triangulo superior derecho
c = c + c.T												#asigna el triángulo inferior izquierdo como el simétrico
c[range(N),range(N)]=1							# asigna la diagonal a 1


C=np.zeros((20,20))
r1=np.zeros((N,N))
for x in range(0,N):
	for y in range(0,N):
		r1[x,y] = np.sqrt(x**2+y**2)

C1=Bd*r1**(-(1/4))
C1[0,0]=1

#plt.figure()
#plt.scatter(r1,C1,color='blue',label="Infinite_Net")
#plt.xlabel("r",fontsize=20, rotation=0, labelpad=20)
#plt.ylabel("Cij",fontsize=20, rotation=0, labelpad=20)
#plt.legend(loc='upper right')

#%% RED FINITA

L=20			# lado del cuadrado
size=L*L		# número total de neuronas
ind = np.triu_indices(size, 1)							# Coge los índices del triángulo superior derecho
c_values=np.load("correlations-ising2D-size400.npy")	#carga valores de correlacions
#c_values=c_values[:79800]
#correlations-ising2D-INFINITE2.npy    correlations-ising2D-size400.npy
c=np.zeros((size,size))									#Crea la matriz de 400x400
c[ind] = c_values										# asigna el triangulo superior derecho
c = c + c.T												#asigna el triángulo inferior izquierdo como el simétrico
c[range(size),range(size)]=1							# asigna la diagonal a 1

#print(c)

r=np.zeros((size,size))				# matriz de distancias
for i1 in range(L):
	for j1 in range(L):				# posición de neurona 1
		for i2 in range(L):
			for j2 in range(L):		# posición de neurona 2
				ind1 = i1 + j1*L
				ind2 = i2 + j2*L
				dx = min(np.abs(i1-i2),L-np.abs(i1-i2))		# calcula distancia más corta de
				dy = min(np.abs(j1-j2),L-np.abs(j1-j2))		# la red periódica en cada eje
				r[ind1,ind2]=np.sqrt(dx**2+dy**2)			# calcula distancia más corta en red periódica
				
#print(r[:1,:10])
#print(c[:10,:10])

#%% PLOTEAR AMBAS

plt.figure()
plt.scatter(r,c,color='green')
plt.plot(r1[:11,:11],C1[:11,:11],color='blue')
plt.xlabel("r",fontsize=20, rotation=0, labelpad=20)
plt.ylabel("Cij",fontsize=20, rotation=0, labelpad=20)
plt.legend(loc='upper right')
plt.show()

