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
p_op=os.getenv('P_OP')
path = os.getenv('P_Dir')
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
att=os.getenv('Attractor')
nNodes=int(os.getenv('Nodes'))
Input_Attractor=np.loadtxt('./Output_Scale_Free/Output_No_Noise/Output_Clustering_0.0/Output_Time_Scale_1/Henon_rec.dat', unpack=True)
#fout = open('%s/Coincident_Points.dat' %path, 'w')
#fout2 = open('%s/Coincident_Points_Ratio.dat' %path,'w')
#A = np.loadtxt('%s/Converted_Attractor_Sequence_%s.dat' %(path_att,att),unpack=True)
All_IPI_1=[]
All_IPI_2=[]
for i in range(0,nNodes):

	B = np.loadtxt('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),unpack=True)
	All_IPI_1.extend(B[0])
	All_IPI_2.extend(B[1])


xedges = [0, 0.5]
yedges = [0, 0.5]

H, xedges, yedges = np.histogram2d(All_IPI_2,All_IPI_1, bins=(500, 500),range=[[0.0, 0.4044189], [0.0, 0.4044189]],normed=True)
H_2, xedges_2, yedges_2 = np.histogram2d(Input_Attractor[1],Input_Attractor[0], bins=(500, 500),normed=True)

count=0
i_old=0
Number_of_nonzero_elements=0
count_histogram_bins=0
for i in range(len(H)):
	for j in range(len(H)):
		if H[j,i]!=0:
			Number_of_nonzero_elements+=1
		if H[j,i]!=0.0 and H_2[j,i]!=0.0:
			count+=1
			count_histogram_bins+=float(H[j,i])/float(H.max())
			#print i,j, H[j,i],H_2[j,i]

all_alpha_beta=open('%s/Distance_between_histograms.dat' %p_op,'a')

print >> all_alpha_beta,alpha,beta,float(count_histogram_bins)/float(count)

'''
for i in range(len(H)):
	for j in range(len(H)):
		print i,j,H[j,i]
		
	if i_old!=i:
		print " "
	i_old=i

for i in range(len(H)):
	for j in range(len(H)):
		if H[i,j] <=10:
			H[i,j] = 0
		#if H[i,j] > 30:
		#	H[i,j] = 0
'''

'''
im = plt.imshow(H_2/H_2.sum(), interpolation='nearest', origin='low',
                extent=[xedges_2[0], xedges_2[-1], yedges_2[0], yedges_2[-1]], cmap='Greys')
plt.colorbar()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8.5,8.5)
plt.xlim([0,1.0])
plt.ylim([0,1.0])
#plt.xlabel(r'$IPI$',fontsize=30,labelpad=15)
#plt.ylabel(r'$\mathrm{Probability}$')
#plt.ylabel('Probability',fontsize=20,labelpad=15)
plt.title(r'$\mathrm{Histogram\ of\ IPIs\ of\ %s}$' %att)
#plt.axis([40, 160, 0, 0.03])
#plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15,labelbottom=5)
plt.savefig('Histogram_2D_%s_input.eps' %(att))
plt.close()
'''


'''
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

		
