import matplotlib
matplotlib.use('Agg')
import time
import scipy.cluster.hierarchy as hcluster
import numpy.random as random
import numpy
import scipy
import os

import pylab
pylab.ion()



fout=open('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Regularity_Average.dat','a')

Reg_1 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0001/Regularity/Regularity.dat',unpack=False)
Reg_2 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0002/Regularity/Regularity.dat',unpack=False)
Reg_3 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0003/Regularity/Regularity.dat',unpack=False)
Reg_4 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0004/Regularity/Regularity.dat',unpack=False)
Reg_5 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0005/Regularity/Regularity.dat',unpack=False)
Reg_6 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0006/Regularity/Regularity.dat',unpack=False)
Reg_7 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0007/Regularity/Regularity.dat',unpack=False)
Reg_8 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0008/Regularity/Regularity.dat',unpack=False)
Reg_9 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0009/Regularity/Regularity.dat',unpack=False)
#Reg_10 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0010/Regularity/Regularity.dat',unpack=False)
Reg_11 = numpy.loadtxt('/media/Backup/Simulations_Lausanne_August_2013/groups/nhrg/avilla/run_1/Output/Output_0011/Regularity/Regularity.dat',unpack=False)

Reg=numpy.zeros([len(Reg_1)])
Reg_std=numpy.zeros([len(Reg_1)])

for i in range(len(Reg_1)):
	Reg[i]=(Reg_1[i][2]+Reg_2[i][2]+Reg_3[i][2]+Reg_4[i][2]+Reg_5[i][2]+Reg_6[i][2]+Reg_7[i][2]+Reg_8[i][2]+Reg_9[i][2]+Reg_11[i][2])/10
	Reg_std[i]=numpy.sqrt((pow((Reg_1[i][2]-Reg[i]),2.0)+pow((Reg_2[i][2]-Reg[i]),2.0)+pow((Reg_3[i][2]-Reg[i]),2.0)+pow((Reg_4[i][2]-Reg[i]),2.0)+pow((Reg_5[i][2]-Reg[i]),2.0)+pow((Reg_6[i][2]-Reg[i]),2.0)+pow((Reg_7[i][2]-Reg[i]),2.0)+pow((Reg_8[i][2]-Reg[i]),2.0)+pow((Reg_9[i][2]-Reg[i]),2.0)+pow((Reg_11[i][2]-Reg[i]),2.0))/10)
	#Reg_std[i]=numpy.sqrt((Reg_1[i][2]-Reg[i])**2)
	if(Reg_1[i][0]!=Reg_1[i-1][0]):
		print >>fout, " "
	print >>fout,Reg_1[i][0],Reg_1[i][1], Reg[i],Reg_std[i]



	


 








