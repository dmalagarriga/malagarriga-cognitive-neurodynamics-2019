#!/bin/bash

source Bash_archives/Environment_Variables.bash

Create_Data=1
Analysis=0
Compile=1
Copy_images=0

if [ $Compile -eq 1 ];then
printf "Compiling ... \n "
make
printf "Compiled!\n"
fi
printf "Running ...\n "
for p in 155
	do
	for alpha in $(seq 00.00 05.00 50.00)
		do
		for beta in $(seq 00.00 05.00 50.00)
			do
			for ((SEED=1;SEED<=1;SEED++))
				do
				for Frequencia in 08.50
					do
					for Amplitud in 0
						do
						
						printf -v Num_p "%04i" $p
						printf -v Num_alpha "%05.2f" $alpha
						printf -v Num_beta "%05.2f" $beta
						printf -v Num_seed "%04i" $SEED
						printf -v Num_freq "%04s" $Frequencia
						printf -v Num_amp "%04i" $Amplitud
						printf -v Num_sec "%05.2f" $Section

						mkdir -p Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
						
						if [ $Create_Data -eq 1 ];then
						Dir_Time_Occurence="Input/Time_Occurrences/${Attractor}"
						Time_Occurence="Input/Time_Occurrences/${Attractor}/Time_Occurrence_Timescale_Miliseconds.dat"
						Dir_Output="Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
						Dir_Poincare="Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
       					Data_Dat="Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_${Num_p}.dat" 
						Init_Cond_Dat="Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Init_Cond_${Num_seed}.dat"
						Poincare_Dat="Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Section_tau_0_equal_${Num_sec}.dat"
						Counter=$(wc -l < "$Time_Occurrence")
				
						./nmm.exe > Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/P_Hist_alpha_${Num_alpha}_beta_${Num_beta}.dat  
						#python ./Analysis/embedding.py
						fi
						#tar rf Output.tar Output/1_variable/${Attractor}/*  
						#tar czf Output.tar.gz Output.tar
						#rm -r Output
						export P_Dir="Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
						export P_OP="Output/1_variable/${Attractor}/Output_${Num_seed}/OrderParameter"
						mkdir -p Output/1_variable/${Attractor}/Output_${Num_seed}/Regularity/
						export P_Reg="Output/1_variable/${Attractor}/Output_${Num_seed}/Regularity"
						mkdir -p Output/1_variable/${Attractor}/Output_${Num_seed}/OrderParameter
						
						if [ $Analysis -eq 1 ];then
						bash ./Bash_archives/Analysis.bash
						fi
						if [ $Copy_images -eq 1 ];then
						convert -density 100 -rotate 90 Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Sections.ps Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Sections.png
						convert -density 100 -rotate 90 Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_0155.ps Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_0155.png

						mkdir -p /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
						cp Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Sections.png /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/
						cp Output/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_0155.png /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/
						
						fi
						done
					done
				
				done
		alpha_old=${alpha}
		done
	#rm Output.tar
	
	done
	
	#rm Output.tar
done

#gnuplot Plot_SurfPlot_OP.gnu
#gnuplot Plot_SurfPlot_Reg.gnu
 
printf "done\n"
rm -f nmm.exe


