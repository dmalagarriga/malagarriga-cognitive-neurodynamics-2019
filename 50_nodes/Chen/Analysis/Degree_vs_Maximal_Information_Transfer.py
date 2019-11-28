#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import os
import numpy as np
from matplotlib import rc
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.mlab as mlab
from scipy.stats import norm
from scipy.spatial import distance
rc('font',**{'family':'sans-serif','size':18,'sans-serif':['Helvetica']})
rc('text', usetex=True)

nNodes=int(os.getenv('Nodes'))
initial_nodes=12
path = os.getenv('P_Dir')
fout = open('%s/Degree_vs_Similarity.dat' %path,'w')
All_IPI_input=[]
Input_Attractor=np.loadtxt('./Output_Scale_Free/Output_No_Noise/Output_Clustering_0.0/Output_Time_Scale_1/Chen_rec.dat', unpack=True)
for i in range(len(Input_Attractor[1])):
	All_IPI_input.append((Input_Attractor[0][i],Input_Attractor[1][i]))

G=nx.barabasi_albert_graph(nNodes,initial_nodes,seed=1)

Degree_and_Similarity=[]
for i in range(0,nNodes):
	Len_Coin_Points=[]
	B = np.loadtxt('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),unpack=False)
	
	for j in range(len(B)):
		#print B[j]
		d = distance.cdist(All_IPI_input,[B[j]])
		Len_Coin_Points.append(len(set(np.where(d<0.01)[1])))
	
	Degree_and_Similarity.append(( G.degree(i),float(np.sum(Len_Coin_Points))/float(len(B)),i ))
	
D_and_S = sorted(Degree_and_Similarity)

for i,j,k in D_and_S:
	print >> fout,  i,j,k