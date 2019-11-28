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
fout = open('%s/Similarity.dat' %path,'w')
Attractor = os.getenv('Attractor')

All_IPI_input=[]
Input_Attractor=np.loadtxt('./Attractors/%s_rec.dat' %Attractor,unpack=False)
Output_Poincare_Section = np.loadtxt('%s/Poincare_Section_Maxima.dat'%path,unpack=False)

Len_Coin_Points = []

d = distance.cdist(Input_Attractor,Output_Poincare_Section)

Len_Coin_Points.append(len(set(np.where(d<0.01)[1])))
	
print >> fout, float(np.sum(Len_Coin_Points))/float(len(Output_Poincare_Section))
