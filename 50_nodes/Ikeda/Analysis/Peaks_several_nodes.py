#!/usr/bin/python
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
       

path=os.getenv('P_Dir')
nNodes=int(os.getenv('Nodes'))
#fout=open('%s/Poincare_Section_Maxima.dat' %path,'w')
#fout2=open('%s/Position_Peaks_Poincare_Section_Maxima.dat' %path,'w')

infiles=sorted(glob.glob('%s/Data_0155.dat' %path))

indexmax=0
posmax=0
indexmax1=[]
posmax1=[]

indexin=0
posmin=0
indexmin1=[]
posmin1=[]



for infile in infiles:
	Trans=50000
	iterator =[]
	for i in range(1,nNodes+1):
		iterator.append(i)
	s = loadtxt(infile,usecols=(iterator), unpack=True)
	
	for i in range(nNodes):
		fout=open('%s/Poincare_Section_Maxima_Node_%02i.dat' %(path,i),'w')
		fout2=open('%s/Position_Peaks_Poincare_Section_Maxima_Node_%02i.dat' %(path,i),'w')
		MaxTab,MinTab= spectrum.peakdet(s[i][:len(s[i])],0.001)
		

		Val_Max=[]
		Pos_Max=[]
		Real_Spikes1=[]
		Real_Spikes2=[]
	
		for j in range(len(MaxTab)):
		
			Val_Max.append(MaxTab[j][1]) # Amplitude of the signal
			Pos_Max.append(MaxTab[j][0]) # Position of the maxima
		#	print>>fout, (MaxTab[i+1][0]-MaxTab[i][0])*0.001,(MaxTab[i][0]-MaxTab[i-1][0])*0.001, (MaxTab[i+1][1]-MaxTab[i][1])*0.001,(MaxTab[i][1]-MaxTab[i-1][1])*0.001
		# average ISI = 0.294367311072
	
		for k in range(0,len(Pos_Max)):
			#if(Val_Max[k]>2.0*std(Val_Max)):
			#if(Val_Max[k]>12.0):
			if (Val_Max[k]>1.2*average(Val_Max) and Val_Max[k]<max(Val_Max)):
			
				Real_Spikes2.append(Val_Max[k])
				Real_Spikes1.append(Pos_Max[k]*0.005)
				print >>fout2,Pos_Max[k]*0.005,Val_Max[k]
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
				print >> fout,(Real_Spikes1[l-1]-Real_Spikes1[l-2]),(Real_Spikes1[l]-Real_Spikes1[l-1])
					
				#print>>fout, Real_Spikes1[l], "2"
			#print>>fout, MaxTab[i-1][0], MaxTab[i][0] #MinTab[i][1]
			#print >>fout,abs(MaxTab[i][1]-MinTab[i][1]),abs(MaxTab[i+1][1]-MinTab[i+1][1])
			#print >>fout,MaxTab[i][1]-MinTab[i][1],MaxTab[i+1][1]-MinTab[i+1][1]
	

	
	
	
	

