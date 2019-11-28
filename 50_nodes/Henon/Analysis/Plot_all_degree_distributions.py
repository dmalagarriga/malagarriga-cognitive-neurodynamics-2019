#!/usr/bin/python

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pylab
import glob
import os
import numpy as np
from matplotlib import rc
import matplotlib.mlab as mlab
import matplotlib.cm as cm
import spectrum


infiles=sorted(glob.glob('./Input/Degree_distribution_BARABASI_*.dat'))
#color=['crimson', 'burlywood', 'chartreuse','black','blue','red','green','magenta','gray','yellow']
C=0.0
i=0.0
fig = plt.figure()
ax = fig.add_axes([.1,.1,.8,.8]) # main axes
colors1 = iter(cm.rainbow(np.linspace(0, 1, len(infiles))))
for infile in infiles:
	i+=1
	if(i==2):
		C=0.2
	if(i>2):
		C+=0.1	
	file=np.loadtxt(infile,unpack=True)
	ax.loglog(file,'o-',label=['C=%03.2f' %C],alpha=0.5,color=next(colors1))
	ax.set_xlabel('Node',fontsize=20,labelpad=5)
	ax.set_ylabel('Degree', fontsize=20)
	ax.tick_params(axis='both', which='major', labelsize=15)
	#ax.legend()
	plt.savefig('Degree_Sequences.pdf',alpha=0.5)

