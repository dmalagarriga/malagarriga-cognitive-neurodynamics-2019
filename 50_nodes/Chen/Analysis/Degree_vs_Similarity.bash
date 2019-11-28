#!/bin/bash 



File_Gnu="/tmp/Gnuplot.gnu"


cat > $File_Gnu << EOF
set term post eps color solid enhanced font "Helvetica,25" 

set output "./`echo $P_Dir`/Degree_vs_Similarity.eps"
set xlabel 'Degree'
set ylabel 'Similarity (d)'
set yrange[0:1.0]
set ytics 0,0.2,1.0
#plot for [i in "2 4 7 9"] "${File_Dat}" using (\$0*0.005):i every ::6000::7000 w l notitle lw 2 
plot "./`echo $P_Dir`/Degree_vs_Similarity.dat" using 1:2 w lp pt 7 ps 1.5 lc rgb 'magenta' notitle  
#plot "${File_Dat}" using (\$0*0.005):3 every ::6000::7000 w l notitle lw 2 lc rgb "#aa0000", "${File_Dat}" using (\$0*0.005):51 every ::6000::7000 w l notitle lw 2 lc rgb "#006400"


EOF

gnuplot ${File_Gnu}

# Tail tells to plot the last -n lines of the data. The simulations have a ntout=5, so each time interval between written points is 0.005.
# That is why we have (\$0*0.005) (each point is equal to 0.005).
