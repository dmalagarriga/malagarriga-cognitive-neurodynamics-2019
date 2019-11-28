# -*- coding: utf-8 -*-
from pylab import *
from numpy import *
from scipy import *
import random

#rescale_Duffing=0.05
rescale_Ikeda=0.15
rescale_Henon=0.1
rescale_Chen=0.25
rescale_Zavslaskii=0.05


#rescale_Duffing=0.5
#rescale_Ikeda=1.0
#rescale_Henon=0.5
#rescale_Chen=0.05
#rescale_Zaslavsky=1.0
Deterministic=0
Noise=1
random.seed(1)
if Deterministic==1:
	Attractor='Chen'

	if Attractor=='Zavslaskii':
		Att_All = []
		fout2=open('./Input/Time_Occurrences/%s/Time_Occurrence_Timescale_Miliseconds.dat' %Attractor,'w')
		Zavs=loadtxt('./Attractors/Converted_Attractor_Sequence_%s.dat' %Attractor,unpack=True)
		#for i in range(len(Zavs[0])):
		#	Att_All.append(Zavs[0,i]-Zavs[0,i-1])
		#Att_All_rescaled=Att_All-min(Att_All)
		Att_All=Zavs[0]
		Att_All_rescaled=Zavs[0]-min(Att_All)
		t_occurrence=zeros([len(Att_All_rescaled)])
		for i in range(len(Att_All_rescaled)):
			t_occurrence[i]=t_occurrence[i-1]+ Att_All_rescaled[i]*rescale_Zavslaskii
			print >> fout2,t_occurrence[i] 
	else:
		
		
		Att=loadtxt('./Attractors/%s_Attractor.dat' %Attractor, unpack=True)
		fout2=open('./Input/Time_Occurrences/%s/Time_Occurrence_Timescale_Miliseconds.dat' %Attractor,'w')
		Att_out=open('./Attractors/Converted_Attractor_Sequence_%s.dat' %Attractor,'w')
		Att_All = []
		Att_All_rescaled=[]


		Trans=16942
	
		for i in range(len(Att[0][:Trans])):
			Att_All.append(Att[0,i]-Att[0,i-1])
		
	
		Att_All_rescaled=Att_All-min(Att_All)
		if Attractor=='Chen':
			for i in range(len(Att_All_rescaled)):
				print >> Att_out, Att_All_rescaled[i-1]/30,Att_All_rescaled[i]/30
		else:
			for i in range(len(Att_All_rescaled)):
				print >> Att_out, Att_All_rescaled[i-1],Att_All_rescaled[i]


		Trans1=len(Att_All_rescaled)
		Trans2=5000
		t_range = arange(0, 10, 0.001)
		t_old=0

		t_occurrence=zeros([len(Att_All_rescaled[:Trans1])])

		for i in range(len(Att_All_rescaled[:Trans1])):
			if Attractor == 'Ikeda':
				t_occurrence[i]=t_occurrence[i-1]+ Att_All_rescaled[i]*rescale_Ikeda
				print>>fout2,t_occurrence[i]
			if Attractor == 'Henon':
				t_occurrence[i]=t_occurrence[i-1]+ Att_All_rescaled[i]*rescale_Henon
				print>>fout2,t_occurrence[i]
			if Attractor == 'Chen':
				t_occurrence[i]=t_occurrence[i-1]+ Att_All_rescaled[i]*rescale_Chen/30
				print>>fout2,t_occurrence[i]
if Noise==1:
	Attractor='Noise'
	fout2=open('./Input/Time_Occurrences/%s/Time_Occurrence_Timescale_Miliseconds_1.dat' %Attractor,'w')
	#Att_out=open('./Attractors/Converted_Attractor_Sequence_%s.dat' %Attractor,'w')
	random_numbers=[]
	Trans=16942
	t_occurrence=zeros([Trans])	
	for i in range(Trans):
		#random_numbers.append(np.random.normal(0.25,0.01)) # For Chen and Henon
		random_numbers.append(np.random.normal(0.35,0.1)) # For Zaslavskii
		#random_numbers.append(np.random.poisson(5, 1))
	for i in range(Trans):
		t_occurrence[i]=t_occurrence[i-1]+random_numbers[i]	
		print>>fout2, t_occurrence[i]






		

