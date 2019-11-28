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
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
all_alpha_beta=open('./Output/1_variable/Ikeda/Output_0001/OrderParameter/Distance_map.dat','a')
#att=os.getenv('Attractor')
nNodes=int(os.getenv('Nodes'))
Input_Attractor=np.loadtxt('./Attractors/Ikeda_rec.dat', unpack=True)
fout = open('%s/Coincident_Points.dat' %path, 'w')
#fout2 = open('%s/Coincident_Points_Ratio.dat' %path,'w')
#A = np.loadtxt('%s/Converted_Attractor_Sequence_%s.dat' %(path_att,att),unpack=True)
All_IPI_1=[]
All_IPI_2=[]
for i in range(0,nNodes):

	B = np.loadtxt('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),unpack=True)
	All_IPI_1.extend(B[0])
	All_IPI_2.extend(B[1])

'''	
xedges = [0, 0.5]
yedges = [0, 0.5]

H, xedges, yedges = np.histogram2d(All_IPI_2,All_IPI_1, bins=(250, 250),normed=True)
for i in range(len(H)):
	for j in range(len(H)):
		if H[i,j] <=0:
			H[i,j] = 0

im = plt.imshow(H/H.sum(), interpolation='nearest', origin='low',
                extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], cmap='Greys')
plt.colorbar()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8.5,8.5)
plt.xlim([0,0.45])
plt.ylim([0,0.45])
#plt.xlabel(r'$IPI$',fontsize=30,labelpad=15)
#plt.ylabel(r'$\mathrm{Probability}$')
#plt.ylabel('Probability',fontsize=20,labelpad=15)
plt.title(r'$\mathrm{Histogram\ of\ IPIs\ of\ %s}$' %att)
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15,labelbottom=5)
plt.savefig('Histogram_2D_%s_output.pdf' %(att))
plt.close()




G, xedges, yedges = np.histogram2d(Input_Attractor[1], Input_Attractor[0], bins=(250,250), normed=True)
im_2=plt.imshow(G/G.sum(), interpolation='nearest', origin='low',
				extent=[xedges[0],xedges[-1],yedges[0],yedges[-1]],cmap='Greys')
plt.colorbar()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8.5,8.5)

#plt.xlabel(r'$IPI$',fontsize=30,labelpad=15)
#plt.ylabel(r'$\mathrm{Probability}$')
#plt.ylabel('Probability',fontsize=20,labelpad=15)
plt.title(r'$\mathrm{Histogram\ of\ IPIs\ of\ %s}$' %att)
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
plt.xlim([0,0.45])
plt.ylim([0,0.45])
plt.tick_params(axis='both', which='major', labelsize=15,labelbottom=5)
plt.savefig('Histogram_2D_%s_input.pdf' %(att))
plt.close()
'''
# Substraction
All_IPI_input = []
All_IPI_output = []

for i in range(len(Input_Attractor[1])):
	All_IPI_input.append((Input_Attractor[0][i],Input_Attractor[1][i]))

for i in range(len(All_IPI_1)):
	All_IPI_output.append((All_IPI_1[i],All_IPI_2[i]))

 
Coincident_points=[]
Non_Coincident_points=[]
A = distance.cdist(All_IPI_input, All_IPI_output)
#for i in range(len(A)):
#	for j in A[i]:
#		if j<0.01:
#			Coincident_points.append((All_IPI_output[list(A[i]).index(j)]))
#print len(set(Coincident_points))

#for i in np.where(A<0.005)[1]:
#	Non_Coincident_points.append(All_IPI_output[i])
#print len(set(Non_Coincident_points))

print >> all_alpha_beta,alpha, beta, float(len(set(np.where(A<0.01)[1])))/float(len(All_IPI_output))
for i in set(np.where(A<0.01)[1]):
	print >>fout, str(All_IPI_output[i]).strip('()')

#print >> fout2, float(len(Coin))/float(len(All_IPI_input)), float(len(Coin))/float(len(All_IPI_output)),1-float()
		
