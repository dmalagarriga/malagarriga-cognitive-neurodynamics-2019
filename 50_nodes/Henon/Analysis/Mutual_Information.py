from Information_processing import *
from Information_and_Network_Analysis_Tools import *
import os
import glob
from numpy import *

path_input_attractor = os.getenv('P_In')
path_output_peaks = os.getenv('P_Out')

Input = loadtxt('%s/Time_Occurrence_Timescale_Seconds_Chen.dat,1_ss' %path_input_attractor,unpack=True)
Output = loadtxt('%s/Position_Peaks_Chen.dat,1_ss' %path_output_peaks,unpack=True,usecols=(0,))

path_output='Output/Ikeda/'
fout=open('%s/Mutual_Info_Input_Output.dat' %path_output,'w')


if len(Output)<len(Input):
	Matrix=column_stack((Input[:len(Output)],Output))
else:
	Matrix=column_stack((Input,Output[:len(Input)]))

print mutual_info(Matrix, n_bins=100, normalized=True, fast=True)
component_1=[]
component_2=[]

for i in range(len(Matrix)):
	component_1.append(Matrix[i][0])
	component_2.append(Matrix[i][1])
print nmi(array(component_1),array(component_2))
