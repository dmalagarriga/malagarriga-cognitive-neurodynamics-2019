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



path_att=os.getenv('P_Att')
path = os.getenv('P_Dir')
att=os.getenv('Attractor')

A = np.loadtxt('%s/Converted_Attractor_Sequence_%s.dat' %(path_att,att),unpack=True)
All_IPI=[]
for i in range(0,10):

	B = np.loadtxt('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),unpack=True)
	All_IPI.append(B[0])
	
	


n, bins,patches = plt.hist(All_IPI[0], 150, facecolor='grey',  normed=False, alpha=0.75)
n, bins,patches = plt.hist(A[0], 150, facecolor='red',  normed=False, alpha=0.75)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8.5,8.5)

plt.xlabel(r'$IPI$',fontsize=30,labelpad=15)
#plt.ylabel(r'$\mathrm{Probability}$')
plt.ylabel('Probability',fontsize=20,labelpad=15)
plt.title(r'$\mathrm{Histogram\ of\ IPIs\ of\ %s}$' %att)
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15,labelbottom=5)
plt.savefig('Histogram_%s_input_output.pdf' %(att))
plt.close()