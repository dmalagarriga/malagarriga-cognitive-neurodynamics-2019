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
from spectrum import *
import itertools
import random 
from Template import *
#from skimage.feature import match_template

'''
This program computes the distance between two maps: input
map and output reconstructed map. Then it tries to guess
which transformation has been performed in each point to
move the points from the input into the output. By this method
one can aproximate the transformation function.
'''
section=8.0
Thresh=5

path_input = os.getenv('P_In')
path_output_chen = os.getenv('P_Out_Chen')
path_output_henon = os.getenv('P_Out_Henon')
path_output_ikeda = os.getenv('P_Out_Ikeda')

random.seed(1)

Trans=5000 # max is len(Output) which is aprox 11.000

Input_Chen = loadtxt('%s/Converted_Attractor_Sequence_Chen.dat' %(path_input),unpack=True)
#Output_Chen = loadtxt('%s/Poincare_Section_Chen_y0_equal_0.1_more_points.dat' %(path_output_chen),unpack=True)
Output_Chen = loadtxt('%s/Poincare_Section_tau_20_equal_%05.2f.dat' %(path_output_chen,section),unpack=True)

Input_Henon = loadtxt('%s/Converted_Attractor_Sequence_Henon.dat' %(path_input),unpack=True)
#Output_Henon = loadtxt('%s/Poincare_Section_Henon_y0_equal_0.1_more_points.dat' %(path_output_henon),unpack=True)
Output_Henon = loadtxt('%s/Poincare_Section_tau_20_equal_%05.2f.dat' %(path_output_henon,section),unpack=True)

Input_Ikeda = loadtxt('%s/Converted_Attractor_Sequence_Ikeda.dat' %(path_input),unpack=True)
#Output_Ikeda = loadtxt('%s/Poincare_Section_Ikeda_y0_equal_0.1_more_points.dat' %(path_output_ikeda),unpack=True)
Output_Ikeda = loadtxt('%s/Poincare_Section_tau_20_equal_%05.2f.dat' %(path_output_ikeda,section),unpack=True)


Distances_x_Chen=zeros([len(Input_Chen[0][:Trans]),len(Input_Chen[0][:Trans])])
Distances_y_Chen=zeros([len(Input_Chen[0][:Trans]),len(Input_Chen[0][:Trans])])

Distances_x_Henon=zeros([len(Input_Henon[0][:Trans]),len(Input_Henon[0][:Trans])])
Distances_y_Henon=zeros([len(Input_Henon[0][:Trans]),len(Input_Henon[0][:Trans])])

Distances_x_Ikeda=zeros([len(Input_Ikeda[0][:Trans]),len(Input_Ikeda[0][:Trans])])
Distances_y_Ikeda=zeros([len(Input_Ikeda[0][:Trans]),len(Input_Ikeda[0][:Trans])])

for i in range( len(Input_Chen[0][:Trans])):
	for j in range(len(Input_Chen[0][:Trans])):	
		
		Distances_x_Chen[i,j]=Input_Chen[0][i] - Output_Chen[1][j]
		Distances_y_Chen[i,j]=Input_Chen[1][i] - Output_Chen[2][j]


		Distances_x_Henon[i,j]=Input_Henon[0][i] - Output_Henon[1][j]
		Distances_y_Henon[i,j]=Input_Henon[1][i] - Output_Henon[2][j]

		Distances_x_Ikeda[i,j]=Input_Ikeda[0][i] - Output_Ikeda[1][j]
		Distances_y_Ikeda[i,j]=Input_Ikeda[1][i] - Output_Ikeda[2][j]

'''
We can calculate all possible mappings between
the points in the two maps and then see which one
best fits the 3 maps transformation (brute force!)
'''

N=len(Input_Chen[0][:Trans])
perm_list = set()
#Distances_Chen=[]
#Distances_Henon=[]
#Distances_Ikeda=[]

Diff_Distances_ChenHenon=[]
Diff_Distances_HenonIkeda=[]
Diff_Distances_IkedaChen=[]
while len(perm_list)<2:
    temp = range(N)
    random.shuffle(temp)
    perm_list.add(tuple(temp)) 
for k in range(1,2):
	counter_ChenHenon = 0
	counter_HenonIkeda = 0
	counter_IkedaChen = 0
	for i,j in enumerate(list(perm_list)[k]):
		
		Diff_Distances_ChenHenon.append((Distances_x_Chen[i,j]-Distances_x_Henon[i,j],Distances_y_Chen[i,j]-Distances_y_Henon[i,j]))
		Diff_Distances_HenonIkeda.append((Distances_x_Henon[i,j]-Distances_x_Ikeda[i,j],Distances_y_Henon[i,j]-Distances_y_Ikeda[i,j]))
		Diff_Distances_IkedaChen.append((Distances_x_Ikeda[i,j]-Distances_x_Chen[i,j],Distances_y_Ikeda[i,j]-Distances_y_Chen[i,j]))
		
	for i,j in Diff_Distances_ChenHenon:
		if sqrt(i*i+j*j)<Thresh:
			counter_ChenHenon +=1
	for i,j in Diff_Distances_HenonIkeda:
		if sqrt(i*i+j*j)<Thresh:
			counter_HenonIkeda +=1
	for i,j in Diff_Distances_IkedaChen:
		if sqrt(i*i+j*j)<Thresh:
			counter_IkedaChen +=1
	
	print float(counter_ChenHenon)/float(len(Diff_Distances_ChenHenon)),float(counter_HenonIkeda)/float(len(Diff_Distances_HenonIkeda)),float(counter_IkedaChen)/float(len(Diff_Distances_IkedaChen))
	Diff_Distances_ChenHenon=[]
	Diff_Distances_HenonIkeda=[]
	Diff_Distances_IkedaChen=[]
		#Distances_Chen.append((Distances_x_Chen[i,j],Distances_y_Chen[i,j]))
		#Distances_Henon.append((Distances_x_Henon[i,j],Distances_y_Henon[i,j]))
		#Distances_Ikeda.append((Distances_x_Ikeda[i,j],Distances_y_Ikeda[i,j]))
		#print Distances_x_Henon[i,j],Distances_y_Henon[i,j]
		
		#print Distances_x_Ikeda[i,j],Distances_y_Ikeda[i,j]

	#print k,round(match_template(array(Distances_Chen),array(Distances_Henon)),6),round(match_template(array(Distances_Chen),array(Distances_Ikeda)),6),round(match_template(array(Distances_Ikeda),array(Distances_Henon)),6)
	#print match_template(array(Distances_Chen),array(Distances_Henon))
	
	#Distances_Chen=[]
	#Distances_Henon=[]
	#Distances_Ikeda=[]


		

