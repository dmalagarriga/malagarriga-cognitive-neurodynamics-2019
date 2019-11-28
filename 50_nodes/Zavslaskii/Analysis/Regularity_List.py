##!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
from matplotlib.collections import LineCollection
import glob
import os
from os.path import join as pjoin
import spectrum

def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))
       

path = os.getenv('P_Dir')
alpha=float(os.getenv('alpha'))
beta=float(os.getenv('beta'))
#Freq=float(os.getenv('Frequencia'))
nNodes=int(os.getenv('Nodes'))

fout=open('%s/List_Reg_alpha_%s_beta_%s.dat' %(path,alpha,beta),'w')
#fout2=open('%s/List_Reg_not_sorted_alpha_%s_beta_%s.dat' %(path,alpha,beta),'w')
#infiles=sorted(glob.glob('%s/A_%s_alpha_%s_beta_%s.dat' %(path,alpha,beta)))

indexmax=0
posmax=0
#indexmax1=[]
#posmax1=[]

Trans=1000
Data=loadtxt('%s/Data_0155.dat' %path, unpack=True)

t=[]
for infile in infiles:
	#One,two,thre,four,five,six = infile.split('/')
	#seven,eight=six.split('_')
	#Column,ext=eight.split('.')

	inline = "/users/avilla/run1/Analysis_Lausanne/Results/Output_0009/A_10_alpha_0.0_beta_0.0.dat"
	x = inline.find('_',59)
	Column = int(inline[59:x])
	
	s = loadtxt(infile, unpack=True)
	indexmax1=[]
	posmax1=[]
	MaxTab,MinTab= spectrum.peakdet(s[:401],0.1)
	
	for i in range(len(MaxTab)):
		indexmax,posmax=MaxTab[i]
		indexmax1.append(indexmax)
		posmax1.append(posmax)
	t.append((Column, Data[int(Column)][Trans:].mean(), sorted(posmax1,reverse=True)[1]))
	print >> fout2, Column, Data[int(Column)][Trans:].mean(), sorted(posmax1,reverse=True)[1]
A = sorted(t,key=lambda item: item[1],reverse=True)
for i in range(len(t)):
	print >> fout,A[i][0],A[i][1],A[i][2]


	
	
	
	
	
	
