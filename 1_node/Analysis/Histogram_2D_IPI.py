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


pylab.rcParams['xtick.major.pad']='8'
pylab.rcParams['ytick.major.pad']='8'



#path_att=os.getenv('P_Att')
path = os.getenv('P_Dir')
att=os.getenv('Attractor')
nNodes=int(os.getenv('Nodes'))
Input_Attractor=np.loadtxt('Henon_rec.dat', unpack=True)
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
for i,j in All_IPI_input:
	for k,l in All_IPI_output:
		if abs(i-k)<0.01 and abs(j-l)<0.01:
			Coincident_points.append((k,l))
Coin = set(Coincident_points)	

for i,j in Coin:
	print i,j
		