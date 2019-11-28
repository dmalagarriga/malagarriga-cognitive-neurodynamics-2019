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


infiles=sorted(glob.glob('./Input/Weight_distribution_BARABASI_*.dat'))
color=['crimson', 'burlywood', 'chartreuse','black','blue','red','green','magenta','gray','yellow']
C=0.0
i=0.0
fig = plt.figure()
ax = fig.add_axes([.1,.1,.8,.8]) # main axes
colors1 = iter(cm.rainbow(np.linspace(0, 1, len(infiles))))
colors2 = iter(cm.rainbow(np.linspace(0, 1, len(infiles))))
for infile in infiles:
	i+=1
	if(i==2):
		C=0.2
	if(i>2):
		C+=0.1	
	file=np.loadtxt(infile,unpack=True)
	weights = np.ones_like(file)/len(file)
	n, bins,patches = ax.hist(file,30,alpha=0.5,weights=weights,label=['C=%03.2f' %C],color=next(colors1))
	ax.legend()
	ax.set_xlabel(r'$\omega_{ij}$',fontsize=20,labelpad=10)
	ax.set_ylabel('Probability', fontsize=20)
	ax.tick_params(axis='both', which='major', labelsize=15)
	ax_inset=fig.add_axes([0.3,0.5,0.3,0.3])
	n, bins,patches = ax_inset.hist(file,30,alpha=0.5,weights=weights,color=next(colors2))
	plt.setp(ax_inset,xlim=([0.0,0.2]))
	plt.savefig('Prova.pdf')

