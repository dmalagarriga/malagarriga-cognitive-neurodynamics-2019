#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from scipy import *
from pylab import *
from numpy import * 
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

nNodes = 1
path = os.getenv('P_Dir')
fout=open('%s/List_Reg.dat' %(path),'w')

Trans=400000
path = os.getenv('P_Dir')

infiles = sorted(glob.glob( '%s/Data_0155.dat' %path), cmp=comparacio)
indexmax=0
posmax=0
posmin=0
indexmin=0

t=[]
for infile in infiles:
	
	#Load data sets
	
	s = loadtxt(infile, unpack=True) # Voxels 1,2,3
	A=[]
	indexmax1=[]
	indexmin1=[]
	posmax1=[]
	posmin1=[]
	#Compute the auto-correlation.
	#fout1=open('%s/A.dat' %(path),'w')
	
	for i in range(1,nNodes+1):
		b=acorr(s[i][Trans:]-s[i][Trans:].mean(),normed=True,usevlines=False,maxlags=None,ls='-',marker='None')
	
		MaxTab,MinTab= spectrum.peakdet(b[1],0.1)
			
	
		for i in range(len(MaxTab)):
			indexmax,posmax=MaxTab[i]
			indexmax1.append(indexmax)
			posmax1.append(posmax)
		
		for i in range(len(MinTab)):
			indexmin,posmin=MinTab[i]
			indexmin1.append(indexmin)
			posmin1.append(posmin)		
		
		#print >>fout,sorted(posmax1,reverse=True)[1], sorted(posmin1,reverse=True)[1],		
		print >> fout,indexmax1[posmax1.index(sorted(posmax1,reverse=True)[1])],indexmin1[posmin1.index(sorted(posmin1,reverse=True)[1])]		
		posmax1=[]
		posmin1=[]
	
	
		
		
		
		
		
		
				

					
		


