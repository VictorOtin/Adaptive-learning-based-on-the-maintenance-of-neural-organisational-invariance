#!/usr/bin/env python

from embodied_ising import ising
import numpy as np
from sys import argv

size = 32 #int(argv[1])
Nsensors = 4 #int(argv[2])
Nmotors = 2 #int(argv[3])
T = 5000 #int(argv[4])
Iterations = 1000 #int(argv[5])
repetitions = 100 #int(argv[6])

filename = 'correlations-ising2D-INFINITE.npy'
Cdist = np.load(filename)

for rep in range(100):
    I = ising(size, Nsensors, Nmotors)
    I.m1 = np.zeros(size)
    I.Cint = np.zeros((size, size - 1))
    for i in range(size):
        c = []
        for j in range(size - 1):
            ind = np.random.randint(len(Cdist))
            c += [Cdist[ind]]
        I.Cint[i, :] = -np.sort(-np.array(c))

    I.CriticalLearning(Iterations, T)

    filename = 'files_prueba/network-size_' + str(size) + '-sensors_' + str(Nsensors) + '-motors_' + str(
            Nmotors) + '-T_1000' + '-Iterations_' + str(Iterations) + '-ind_' + str(rep) + '.npz'
    np.savez(filename, J=I.J, h=I.h, m1=I.m1, Cint=I.Cint)
