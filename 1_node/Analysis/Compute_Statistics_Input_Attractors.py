# -*- coding: utf-8 -*-
import io
import matplotlib
matplotlib.use('Agg')
from matplotlib import gridspec
import numpy as np
import commands
from scipy.signal import find_peaks_cwt
from itertools import tee, izip
import matplotlib.pyplot as plt
import pylab
import os




pylab.rcParams['xtick.major.pad']='8'
pylab.rcParams['ytick.major.pad']='8'


Input=os.getenv('Input')
#path_att=os.getenv('P_Att')
#path = os.getenv('P_Dir')
att=os.getenv('Attractor')

def window(iterable, size):
    iters = tee(iterable, size)
    for i in xrange(1, size):
        for each in iters[i:]:
            next(each, None)
    return izip(*iters)

# Calculation of the multiunit activity #

Attractor = np.loadtxt('%s/Time_Occurrence_Timescale_Miliseconds_1.dat' %Input,unpack=True)

fout = open('%s/Multi_Unit_Activity_Attractor_%s.dat' %(Input,att),'w')
fout_2 = open('%s/Histogram_%s_input.dat' %(Input,att),'w')


Bursts = []
MUA = [] # multi-unit activity


for i in range(int(max(Attractor[:2000]*10))):
    #Bursts.append(float(list(Attractor*10).count(i)))
	Bursts.append(list(np.array(Attractor*10).astype(int)).count(i))
	#print i, list(np.array(Attractor*10).astype(int)).count(i)
    
for i,each in enumerate(window(Bursts,10)):
    print>>fout, float(i)/10.0,np.sum(each)
    #MUA.append((i,np.average(each)))
    MUA.append(np.sum(each))

counts = np.bincount(MUA)


fig, ax = plt.subplots()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(7.5,7.5)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)

ax.bar(range(len(counts)), counts, width=1, align='center')
ax.set(xticks=range(10), xlim=[-1, 10])

#plt.tight_layout()
plt.xlabel(r'$Pulse/s$',fontsize=30,labelpad=15)
plt.ylabel('Counts',fontsize=20,labelpad=15)
plt.title(r'$\mathrm{Histogram\ of\ Pulse/s\ of\ %s}$' %att)
plt.xlim([0.0,10.0])
plt.ylim([0,4500])
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15,labelbottom=5)
plt.savefig('%s/Histogram_%s_input.eps' %(Input,att))

for i in range(len(counts)):
	print >> fout_2,i,counts[i]
'''

n, bins,patches = plt.hist(MUA, 6, facecolor='grey',  normed=False, alpha=0.75)
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8.5,8.5)

plt.xlabel(r'$Pulse/s$',fontsize=30,labelpad=15)
#plt.ylabel(r'$\mathrm{Probability}$')
plt.ylabel('Probability',fontsize=20,labelpad=15)
plt.title(r'$\mathrm{Histogram\ of\ Pulse/s\ of\ %s}$' %att)
#plt.axis([40, 160, 0, 0.03])
plt.xlim([0.0,8.0])
plt.grid(True)
plt.tick_params(axis='both', which='major', labelsize=15,labelbottom=5)
plt.savefig('%s/Histogram_%s_input.eps' %(Input,att))
plt.close()
'''
