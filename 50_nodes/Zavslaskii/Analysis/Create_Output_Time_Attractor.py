from pylab import *
from numpy import *
from scipy import *
import os

path = os.getenv('P_Dir')
Attractor= 'Henon'
Att_out = open('%s/Reconstructed_Attractor_from_Poincare_Section_Time.dat' %path, 'w')
t_occurrence = loadtxt('%s/Poincare_Section_%s_y0_equal_0.1.dat' %(path,Attractor),unpack=True)


for i in range(len(t_occurrence[0])):
	print >> Att_out,t_occurrence[0][i]-t_occurrence[0][i-1],t_occurrence[0][i+1]-t_occurrence[0][i]

