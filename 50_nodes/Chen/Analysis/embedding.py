from scipy import *
from matplotlib import *
from pylab import *

Delay=10
Delay2=20
#section=float(os.getenv('Section'))
path=os.getenv('P_Dir')
#K1=os.getenv('K1')
#fout=open('%s/Emb_plot_K_%s.dat' %(path,K1),'w')
fout=open('%s/Emb_plot_Delay_%05.2f.dat' %(path,Delay),'w')
Lines=open('%s/Data_0155.dat' %path,'r').readlines()

for i,Line in enumerate(Lines):
    if i>Delay:
       Words=Line.split()
       Words2=Lines[i-Delay].split()
       Words3=Lines[i-Delay2].split()	
       print >> fout, Words3[1],Words2[1],Words[1]#, Words2[2],Words[2]
