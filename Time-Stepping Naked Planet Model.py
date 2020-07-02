#!/usr/bin/env python
# coding: utf-8

# import numpy
# import matplotlib.pyplot


# dHeatContent/dt = L*(1-alpha)/4 - epsilon * sigma * T^4
# T[K] = HeatContent [J/m2] / HeatCapacity [J/m2 K]
# HeatContent(t+1) = HeatContent(t) + dHeatContent/dT * TimeStep

nSteps = int(input(""))  # years
waterDepth = 4000  # meters
L = 1350  # Watts/m2
albedo = 0.3
epsilon = 1  # blackbody
sigma = 5.67E-8  # W/m2 K4
HeatCapacity = 4180000*waterDepth  # J/(m2*K)
en_in = 236.25  # energy in(not change through the simulation) W/m2

HeatContent = 0
time_list = [0]
temp_list = [0]
time = 0
temp = 0
while time_list[-1]<1500:
    T = pow(temp_list[-1], 4)
    en_out = epsilon * sigma * T
    HeatFlux = en_in - en_out
    HeatContent = HeatContent + HeatFlux * nSteps * 365 *86400
    temp = HeatContent/HeatCapacity
    temp_list.append(temp)
    time = time + nSteps
    time_list.append(time)


# matplotlib.pyplot.plot(time_list, temp_list)
# matplotlib.pyplot.show()





