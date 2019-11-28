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


Attractor=os.getenv('Attractor')
'''
if Attractor == 'Chen':
	Thresh = 1.909589 #2.0
elif Attractor == 'Henon':
	Thresh = 2.635233 # 2.5
elif Attractor == 'Zavslaskii':
	Thresh = 2.940767 #2.75
'''

nNodes=int(os.getenv('Nodes'))
path = os.getenv('P_Dir')
fout = open('%s/Similarity_vs_Threshold_Poincare_Detection.dat' %path,'w')

All_IPI_input=[]

Input_Attractor=np.loadtxt('./Attractors/%s_rec.dat' %Attractor,unpack=False)
Output_Poincare_Section = np.loadtxt('%s/Poincare_Section_Maxima.dat'%path,unpack=False)

infiles=sorted(glob.glob('%s/Data_0155.dat' %path))
for infile in infiles:
	Trans=50
	iterator =[]
	for i in range(1,nNodes+1):
		iterator.append(i)
	
	s = np.loadtxt(infile,usecols=(1), unpack=True)
indexmax=0
posmax=0
indexmax1=[]
posmax1=[]

indexin=0
posmin=0
indexmin1=[]
posmin1=[]



for Thresh in np.arange(1.5,3.1,0.1):
	for i in range(0,nNodes):
		Len_Coin_Points=[]
		#B = np.loadtxt('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),unpack=False)
		B = []
		MaxTab,MinTab= spectrum.peakdet(s[:len(s)],0.001)


		Val_Max=[]
		Pos_Max=[]
		Real_Spikes1=[]
		Real_Spikes2=[]

		for j in range(len(MaxTab)):

			Val_Max.append(MaxTab[j][1]) # Amplitude of the signal
			Pos_Max.append(MaxTab[j][0]) # Position of the maxima

		# average ISI = 0.294367311072

		for k in range(0,len(Pos_Max)):
		
			if(Val_Max[k]>Thresh*np.std(Val_Max)): 
				Real_Spikes2.append(Val_Max[k])
				Real_Spikes1.append(Pos_Max[k]*0.005)
				if Thresh % 1.9 == 0:
					fout2 = open('%s/Poincare_Section_Threshold_%s.dat' %(path,Thresh),'w')
					print >>fout2,Pos_Max[k]*0.005,Val_Max[k]
	
		for l in range(len(Real_Spikes1)):
			if(Real_Spikes1[l]-Real_Spikes1[l-1]>0.0):
				Real_Spikes1[-2]=0.0
				Real_Spikes1[-1]=0.0
			
				B.append((Real_Spikes1[l-1]-Real_Spikes1[l-2],Real_Spikes1[l]-Real_Spikes1[l-1]))

				if Thresh % 1.9 == 0:
					print >> fout2,Real_Spikes1[l-1]-Real_Spikes1[l-2],Real_Spikes1[l]-Real_Spikes1[l-1]



		d = distance.cdist(Input_Attractor[:][:len(Input_Attractor)],B)
		Len_Coin_Points.append(len(set(np.where(d<0.01)[1])))
	
	print >> fout, Thresh,float(np.sum(Len_Coin_Points))/float(len(B))

