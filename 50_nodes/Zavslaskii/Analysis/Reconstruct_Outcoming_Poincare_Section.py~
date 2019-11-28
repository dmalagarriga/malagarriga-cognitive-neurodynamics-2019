#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os
from os.path import join as pjoin




Ikeda_function=loadtxt('Distances_Ikeda.dat',unpack=True)
Henon_function=loadtxt('Distances_Henon.dat',unpack=True)
Chen_function=loadtxt('Distances_Chen.dat',unpack=True)

Ikeda_attractor=loadtxt('Attractors/Converted_Attractor_Sequence_Ikeda.dat',unpack=True)
Henon_attractor=loadtxt('Attractors/Converted_Attractor_Sequence_Henon.dat',unpack=True)
Chen_attractor=loadtxt('Attractors/Converted_Attractor_Sequence_Chen.dat',unpack=True)

Reconstructed_Ikeda=open('Reconstructed_Ikeda.dat','w')
Reconstructed_Henon=open('Reconstructed_Henon.dat','w')
Reconstructed_Chen=open('Reconstructed_Chen.dat','w')


Total_function=[]
#for i in range(len(Chen_function[0])):
	
	#Total_function.append((Ikeda_function[1][i]/3+Henon_function[1][i]/3+Chen_function[1][i]/3,Ikeda_function[2][i]/3+Henon_function[2][i]/3+Chen_function[2][i]/3))


for i in range(len(Chen_function[0])):
	#print >> Reconstructed_Ikeda,Ikeda_attractor[0][i]+Total_function[i][0],Ikeda_attractor[1][i]+Total_function[i][1]
	#print >> Reconstructed_Henon,Henon_attractor[0][i]+Total_function[i][0],Henon_attractor[1][i]+Total_function[i][1]
	#print >> Reconstructed_Chen,Chen_attractor[0][i]+Total_function[i][0],Chen_attractor[1][i]+Total_function[i][1]
	#print >> Reconstructed_Chen,Chen_attractor[0][i]-Chen_function[0][i],Chen_attractor[1][i]-Chen_function[1][i]
	print >> Reconstructed_Ikeda,Ikeda_attractor[0][i]-Ikeda_function[0][i],Ikeda_attractor[1][i]-Ikeda_function[1][i]
	#print >> Reconstructed_Henon,Henon_attractor[0][i]-Henon_function[0][i],Henon_attractor[1][i]-Henon_function[1][i]

	



