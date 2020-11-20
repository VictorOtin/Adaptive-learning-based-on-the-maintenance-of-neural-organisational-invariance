#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:53:42 2020

@author: victor
"""


import numpy as np
import matplotlib.pyplot as plt

matrix1=np.load('1_0.npy'); pos_x1=matrix1[0,:]; pos_y1=matrix1[1,:]
matrix2=np.load('2_0.npy'); pos_x2=matrix2[0,:]; pos_y2=matrix2[1,:]
matrix3=np.load('3_0.npy'); pos_x3=matrix3[0,:]; pos_y3=matrix3[1,:]
matrix4=np.load('4_0.npy'); pos_x4=matrix4[0,:]; pos_y4=matrix4[1,:]
matrix5=np.load('5_0.npy'); pos_x5=matrix5[0,:]; pos_y5=matrix5[1,:]
matrix6=np.load('6_0.npy'); pos_x6=matrix6[0,:]; pos_y6=matrix6[1,:]
matrix7=np.load('7_0.npy'); pos_x7=matrix7[0,:]; pos_y7=matrix7[1,:]
matrix8=np.load('8_0.npy'); pos_x8=matrix8[0,:]; pos_y8=matrix8[1,:]
matrix9=np.load('9_0.npy'); pos_x9=matrix9[0,:]; pos_y9=matrix9[1,:]

fig, ax = plt.subplots(1,1,figsize=(4.6,3.8))
plt.plot(pos_x1,pos_y1,'k',color='blue')
plt.plot(pos_x2,pos_y2,'k',color='green')
plt.plot(pos_x3,pos_y3,'k',color='red')
plt.plot(pos_x4,pos_y4,'k',color='cyan')
plt.plot(pos_x5,pos_y5,'k',color='magenta')
plt.plot(pos_x6,pos_y6,'k',color='yellow')
plt.plot(pos_x7,pos_y7,'k',color='black')
plt.plot(pos_x8,pos_y8,'k',color='pink')
plt.plot(pos_x9,pos_y9,'k',color='orange')

plt.ylabel(r'$y$',fontsize=18, rotation=0)
plt.xlabel(r'$x$',fontsize=18)
#plt.title(r'$\beta='+str(beta)+'$',fontsize=36)
plt.axis([-0.5,2,-0.5,1.75])
pos_x=np.zeros((T,10))
pos_y=np.zeros((T,10))
plt.show()