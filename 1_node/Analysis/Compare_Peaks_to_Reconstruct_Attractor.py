#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
import glob
import os


path=os.getenv('P_Dir')
nNodes=3

Matrix=[]
fout=open('%s/Reconstructed_Attractor_from_Network.dat' %path, 'w')
fout2=open('%s/Coinciding_Peaks.dat' %path, 'w')
for i in range(nNodes):
	
	file=loadtxt('%s/Position_Peaks_Poincare_Section_Maxima_Node_%02i.dat' %(path,i),usecols=(0,),unpack=True)
	Matrix.append(file.T)

time_occurrencies=[]
for i in range(nNodes):
	for value in Matrix[i]:
		for j in range(i):
			for k in Matrix[j]:
				if abs(value-k)<0.5:
					time_occurrencies.append(value)
		
time_oc=sorted(time_occurrencies)
for i in time_oc:
	print >> fout2, i
for l in range(len(time_oc)):
	if(time_oc[l]-time_oc[l-1]>0.0):
		time_oc[-2]=0.0
		time_oc[-1]=0.0
		print >> fout,(time_oc[l-1]-time_oc[l-2]),(time_oc[l]-time_oc[l-1])
			