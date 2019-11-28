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
	for alpha in $(seq 45.00 05.00 45.00)
		do
		for beta in $(seq 30.00 05.00 30.00)
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

						mkdir -p Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
						
						if [ $Create_Data -eq 1 ];then
						Dir_Time_Occurence="Input/Time_Occurrences/${Attractor}"
						Time_Occurence="Input/Time_Occurrences/${Attractor}/Time_Occurrence_Timescale_Miliseconds_2.dat"
						Dir_Output="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
						Dir_Poincare="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
       					Data_Dat="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_${Num_p}.dat" 
						Init_Cond_Dat="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Init_Cond_${Num_seed}.dat"
						Poincare_Dat="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Section_tau_0_equal_${Num_sec}.dat"
						Counter=$(wc -l < "$Time_Occurrence")
				
						./nmm.exe > Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/P_Hist_alpha_${Num_alpha}_beta_${Num_beta}.dat  
						#python ./Analysis/embedding.py
						fi
						#tar rf Output.tar Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/*  
						#tar czf Output.tar.gz Output.tar
						#rm -r Output
						export P_Dir="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}"
						export P_OP="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/OrderParameter"
						mkdir -p Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Regularity/
						export P_Reg="Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Regularity"
						mkdir -p Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/OrderParameter
						
						if [ $Analysis -eq 1 ];then
						printf "Analysing ...\n"
						bash ./Bash_archives/Analysis.bash
						printf "...Analysed!\n"
						fi
						if [ $Copy_images -eq 1 ];then
						printf "Copying images...\n"
						#convert -density 100 -rotate 90 Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Sections.ps Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Sections.png
						#convert -density 100 -rotate 90 Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_0155.ps Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_0155.png
						convert -density 100 Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Histogram_2D_${Attractor}_output.eps Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Histogram_2D_${Attractor}_output.png 
						#convert -density 100 Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Degree_vs_Similarity.eps Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Degree_vs_Similarity.png 

						mkdir -p /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Time_Scale_1/Output_Scale_Free/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
						#cp Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Poincare_Sections.png /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Time_Scale_1/Output_Scale_Free_RP_0.0/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
						#cp Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Data_0155.png /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Time_Scale_1/Output_Scale_Free_RP_0.0/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
						cp Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Histogram_2D_${Attractor}_output.png /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Time_Scale_1/Output_Scale_Free/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}
						#cp Output_Scale_Free/Output_No_Noise/Output_Clustering_0.5/Output_Time_Scale_1/1_variable/${Attractor}/Output_${Num_seed}/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}/Degree_vs_Similarity.png /home/dani/Escriptori/Deterministic_processing/${Attractor}/50_Nodes/Time_Scale_1/Output_Scale_Free_RP_0.0/Output_alpha_${Num_alpha}/Output_beta_${Num_beta}						
						printf "done!\n"
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


