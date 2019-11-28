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
#from matplotlib.backends.backend_pdf import PdfPages


def comparacio(a,b):
        
	(Sepa,numa) = a.split('_')
	(pa,exta) = numa.split('.')	

	(Sepb,numb) = b.split('_')
	(pb,extb) = numb.split('.')
        value=float(pa)-float (pb)
        return int(value/abs(value))



nTrans=1
path=os.getenv('P_In_Attractor')

#p=os.getenv('p')
infile = ( '%s/Time_Occurrence_Timescale_Miliseconds.dat' %(path))
		
	
#(Sep,num) = infile.split('_')
         
#(p,ext) = num.split('.')

#Load data 
#########################################################################
y0 = loadtxt(infile, unpack=True)
time_course=[]
Evolution=[]
time = arange(0,y0[999],0.001)
spikes_per_second=[]
Trans=10000
for i in range(len(y0)-Trans):
	for j in range(i):
		if 0.9 < y0[i]-y0[i-j]< 1.0:
			#print y0[i]-y0[i-j]
			spikes_per_second.append(j)
			#print j			
			#time_course.append(j)
		#else:
		#	print "0"
print sum(spikes_per_second)/len(spikes_per_second)
'''
for i in range(10):
	Evolution.appedn()y0[i+1:i+10]

for i in range(0,1):
	#f=y0[i][nTrans:]
	
	#A = average(y0[i])
	
	#M = y0[i][nTrans:] - A		
	
	#time = loadtxt(infile, unpack=True, usecols = [0])
	
	(pxx,freqs)=spectrum.PSD(y0[nTrans:], A[nTrans:],16384)	
	#(pxx,freqs)=spectrum.PSD(time[nTrans:], y0[i][nTrans:]-y0[i][nTrans:].mean(),16384)
	plot(freqs, pxx)
	grid('on')
	#title('P= %s' %p)
	xlabel('Frequency')
	ylabel('PSD (1/Hz)')
	xlim([0, 40])	
	#ylim([-6, 5])
	MAXTAB1 = list(pxx)
	MAX1= MAXTAB1.index(max(MAXTAB1))
	xs,ys =freqs[MAX1],max(MAXTAB1)
	ax = gca()
	#ax.annotate('(Frequency = %.3f, PSD = %.3f)' %(freqs[MAX1],max(MAXTAB1)),xy=(freqs[MAX1],max(MAXTAB1)))
	ax.annotate('%.3f' %(freqs[MAX1]),xy=(freqs[MAX1],max(MAXTAB1)))
	plot(xs,ys,marker='o')
	#hold()
	#spectrum.savefig(pjoin(path, 'Spectrum_%s_%i.eps' % (p,i)))	
	#spectrum.savefig(pjoin(path, 'Spectrum_%s.eps' % (p)))	

	
	#close()	
	
#################################################################
	
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

	
	file1 = 'Spectrum_Timescale_Miliseconds.dat'	
	path_file12 = pjoin(path, file1)
	arx1 = open(path_file12,'w')
	
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
	
	for j in range(len(freqs)):
		
		print >>arx1, freqs[j], str(pxx[j]).strip('[]')
	#print >>arx1, p, str(max(MAXTAB[1])).strip('[]')#convert to string to write without brackets	
	arx1.close()			 
	#print >>Arx1, p, freqs[MAX1]
	
close()



#Arx1.close()
'''	
		
