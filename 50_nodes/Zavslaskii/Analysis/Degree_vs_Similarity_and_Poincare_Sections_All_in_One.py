#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import os
import glob
import numpy as np
from matplotlib import rc
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.mlab as mlab
from scipy.stats import norm
from scipy.spatial import distance
import spectrum

#rc('font',**{'family':'sans-serif','size':18,'sans-serif':['Helvetica']})
#rc('text', usetex=True)



fig,ax = plt.subplots(1)

nNodes=int(os.getenv('Nodes'))
path = os.getenv('P_Dir')
fout = open('%s/Degree_vs_Similarity.dat' %path,'w')
fout2 = open('%s/Poincare_Section.dat' %path,'w')
All_IPI_input=[]
Input_Attractor=np.loadtxt('zavs_rec.dat', unpack=True)
#Input_Attractor=np.loadtxt('./Attractors/Chen_rec.dat',unpack=True)
Adj_Matrix = np.loadtxt('./Input/Kex.dat',skiprows=1,unpack=True)
infiles=sorted(glob.glob('%s/Data_0155.dat' %path))
for infile in infiles:
	Trans=0
	iterator =[]
	for i in range(1,nNodes+1):
		iterator.append(i)
	s = np.loadtxt(infile,usecols=(iterator), unpack=True)
indexmax=0
posmax=0
indexmax1=[]
posmax1=[]

indexin=0
posmin=0
indexmin1=[]
posmin1=[]
for i in range(len(Input_Attractor[1])):
	All_IPI_input.append((Input_Attractor[0][i]*1.41,Input_Attractor[1][i]*1.41))

#G=nx.barabasi_albert_graph(nNodes,initial_nodes,seed=1)
G = nx.from_numpy_matrix(Adj_Matrix)
Degree_and_Similarity=[]
for i in range(0,nNodes):
	Len_Coin_Points=[]
	#B = np.loadtxt('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),unpack=False)
	B = []
	MaxTab,MinTab= spectrum.peakdet(s[i][:len(s[i])],0.001)
	

	Val_Max=[]
	Pos_Max=[]
	Real_Spikes1=[]
	Real_Spikes2=[]

	for j in range(len(MaxTab)):
	
		Val_Max.append(MaxTab[j][1]) # Amplitude of the signal
		Pos_Max.append(MaxTab[j][0]) # Position of the maxima
	
	# average ISI = 0.294367311072

	for k in range(0,len(Pos_Max)):
		#if(Val_Max[k]>2.0*std(Val_Max)):
		#if(Val_Max[k]>12.0):
		if (Val_Max[k]>1.2*np.average(Val_Max) and Val_Max[k]<max(Val_Max)):
		
			Real_Spikes2.append(Val_Max[k])
			Real_Spikes1.append(Pos_Max[k]*0.005)
			#print >>fout2,Pos_Max[k]*0.005,Val_Max[k]
	#for k in range(0,len(Pos_Max)):
	#	if(Val_Max[k]>1.0*std(Val_Max)):
	#		if(Val_Max[k]>Val_Max[k-1]):
	#			Real_Spikes2.append(Val_Max[k])
	#			Real_Spikes1.append(Pos_Max[k]*0.005)
	#			print >>fout2,Pos_Max[k]*0.001,Val_Max[k]
				#Real_Spikes2.append((Pos_Max[k+1]-Pos_Max[k])*0.001)
				#print average(Real_Spikes)
	for l in range(len(Real_Spikes1)):
		if(Real_Spikes1[l]-Real_Spikes1[l-1]>0.0):
			Real_Spikes1[-2]=0.0
			Real_Spikes1[-1]=0.0
			#print >> fout,Real_Spikes1[l-1]-Real_Spikes1[l-2],Real_Spikes1[l]-Real_Spikes1[l-1]
			#print >> fout,(Real_Spikes1[l-1]-Real_Spikes1[l-2]),(Real_Spikes1[l]-Real_Spikes1[l-1])
			
			#ax.plot((Real_Spikes1[l-1]-Real_Spikes1[l-2]),(Real_Spikes1[l]-Real_Spikes1[l-1]),'.',markersize =0.5,c=random.rand(3,1))
			ax.plot((Real_Spikes1[l-1]-Real_Spikes1[l-2]),(Real_Spikes1[l]-Real_Spikes1[l-1]),'.',markersize =0.5,c='k')
			B.append((Real_Spikes1[l-1]-Real_Spikes1[l-2],Real_Spikes1[l]-Real_Spikes1[l-1]))
	
	
			print >> fout2,Real_Spikes1[l-1]-Real_Spikes1[l-2],Real_Spikes1[l]-Real_Spikes1[l-1]
	
	
	
	for j in range(len(B)):
		#print B[j]
		d = distance.cdist(All_IPI_input,[B[j]])
		Len_Coin_Points.append(len(set(np.where(d<0.01)[1])))
	
	Degree_and_Similarity.append(( G.degree(i),float(np.sum(Len_Coin_Points))/float(len(B)),i ))
ax.set_aspect(1)
plt.xlim([0.0,0.6])
plt.ylim([0.0,0.6])
plt.ylabel('i+1-th IPI')
plt.xlabel('i-th IPI')
#plt.savefig('%s/Poincare_Sections_2.ps' %path)
plt.savefig('%s/Poincare_Sections.png' %path)	
D_and_S = sorted(Degree_and_Similarity)
D_and_S = np.array(zip(*D_and_S))

counter = 0

for i in sorted(set(D_and_S[0])):
	L = [] # appending similarity measure d
	L.append(D_and_S[1][counter:counter+list(D_and_S[0]).count(i)])
	counter+=list(D_and_S[0]).count(i)
	print >> fout, i, np.average(L),np.std(L)
#for i,j,k in D_and_S:
#	print >> fout,  i,j,k