#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import os
import numpy as np
from matplotlib import rc
import matplotlib.mlab as mlab
import spectrum
from scipy.spatial import distance


pylab.rcParams['xtick.major.pad']='8'
pylab.rcParams['ytick.major.pad']='8'


#path_att=os.getenv('P_Att')
path = os.getenv('P_Dir')
p_op=os.getenv('P_OP')
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
all_alpha_beta=open('%s/Distance_map_4.dat' %p_op,'a')
#att=os.getenv('Attractor')
nNodes=int(os.getenv('Nodes'))
Input_Attractor=np.loadtxt('./Attractors/zavs_rec.dat', unpack=True)
#fout = open('%s/Coincident_Points.dat' %path, 'w')
#fout2 = open('%s/Coincident_Points_Ratio.dat' %path,'w')
#A = np.loadtxt('%s/Converted_Attractor_Sequence_%s.dat' %(path_att,att),unpack=True)
All_IPI_1=[]
All_IPI_2=[]
for i in range(0,nNodes):

	B = np.loadtxt('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),unpack=True)
	All_IPI_1.extend(B[0])
	All_IPI_2.extend(B[1])

# Substraction
All_IPI_input = []
All_IPI_output = []

for i in range(len(Input_Attractor[1])):
	All_IPI_input.append((Input_Attractor[0][i]*1.4,Input_Attractor[1][i]*1.4))

for i in range(len(All_IPI_1)):
	All_IPI_output.append((All_IPI_1[i],All_IPI_2[i]))

 
Len_Coin_Points=[]
Non_Coincident_points=[]
Average=[]


for i in range(len(All_IPI_output)):
	d = distance.cdist(All_IPI_input,[All_IPI_output[i]])
	Average.append(np.average(d))
	Len_Coin_Points.append(len(set(np.where(d<0.01)[1])))

print >> all_alpha_beta,alpha, beta,float(np.sum(Len_Coin_Points))/float(len(All_IPI_output)),1-float(np.sum(Len_Coin_Points))/float(len(All_IPI_output)),np.average(Average)
#for i in range(len(A)):
#	for j in A[i]:
#		if j<0.01:
#			Coincident_points.append((All_IPI_output[list(A[i]).index(j)]))
#print len(set(Coincident_points))

#for i in np.where(A<0.005)[1]:
#	Non_Coincident_points.append(All_IPI_output[i])
#print len(set(Non_Coincident_points))
#print len(set(np.where(A<0.01)[1]))
#print len(All_IPI_output),len(set(np.where(A<0.005)[1])),len(All_IPI_output)-len(set(np.where(A<0.005)[1])) 
#print >> all_alpha_beta,alpha, beta,float(abs(len(set(np.where(A<0.005)[1]))-(len(All_IPI_output)-len(set(np.where(A<0.005)[1])))))/float(len(All_IPI_output))
#print >> all_alpha_beta,alpha, beta, float(len(set(np.where(A<0.01)[1])))/float(len(All_IPI_output))
#for i in set(np.where(A<0.01)[1]):
#	print >>fout, str(All_IPI_output[i]).strip('()')

#print >> fout2, float(len(Coin))/float(len(All_IPI_input)), float(len(Coin))/float(len(All_IPI_output)),1-float()
		
