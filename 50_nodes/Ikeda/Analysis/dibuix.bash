#!/bin/bash 



File_Gnu="/tmp/Gnuplot.gnu"


cat > $File_Gnu << EOF
set term post color solid enhanced font "Helvetica,25" 

set output "./`echo $P_Dir`/Data_0155.ps"
set xlabel 'Time (s)'
set ylabel 'y_1(t)-y_2(t) (mV)'
#plot for [i in "2 4 7 9"] "${File_Dat}" using (\$0*0.005):i every ::6000::7000 w l notitle lw 2 
plot for [i=6:9] "./`echo $P_Dir`/Data_0155.dat" using (\$0*0.005):i every ::6000::7000 w l notitle lw 2 
#plot "${File_Dat}" using (\$0*0.005):3 every ::6000::7000 w l notitle lw 2 lc rgb "#aa0000", "${File_Dat}" using (\$0*0.005):51 every ::6000::7000 w l notitle lw 2 lc rgb "#006400"

set term post color solid enhanced font "Helvetica,25" 
set xtics 0,0.2,1.0
set ytics 0,0.2,1.0
set output "./`echo $P_Dir`/Poincare_Sections.ps"
set xlabel 'i+1-th IPI'
set ylabel 'i-th IPI'
#plot "<head -1000 ${File_Dat}" using (\$0*0.005):2 every ::20 notitle w l lt 1  linewidth 2 lc rgb "#aa0000","<head -1000 ${File_Dat}" using (\$0*0.005):3 every ::20 notitle w l lt 1 linewidth 2 lc rgb "#00aa00","<head -1000 ${File_Dat}" using (\$0*0.005):4 every ::20 notitle w l lt 1 linewidth 2 lc rgb "#0000aa","<head -1000 ${File_Dat}" using (\$0*0.005):5 every ::20 notitle w l lt 1 linewidth 2 lc rgb "orange","<head -1000 ${File_Dat}" using (\$0*0.005):6 every ::20 notitle w l lt 1 linewidth 2 lc rgb "brown","<head -1000 ${File_Dat}" using (\$0*0.005):7 every ::20 notitle w l lt 1 linewidth 2 lc rgb "yellow","<head -1000 ${File_Dat}" using (\$0*0.005):8 every ::20 notitle w l lt 1 linewidth 2 lc rgb "magenta","<head -1000 ${File_Dat}" using (\$0*0.005):9 every ::20 notitle w l lt 1 linewidth 2 lc rgb "gray","<head -1000 ${File_Dat}" using (\$0*0.005):10 every ::20 notitle w l lt 1 linewidth 2 lc rgb "black" 
plot for [i=0:9]"./`echo $P_Dir`/Poincare_Section_Maxima_Node_0".i.".dat" u 1:2 w p pt 7 ps 0.3 notitle #"Node".i
#plot "${File_Dat}" using (\$0*0.005):25 every ::6000::7000 w l notitle lw 2 lc rgb "#7FFF00", "${File_Dat}" using (\$0*0.005):19 every ::9000::10000 w l notitle lw 2 lc rgb "#006400"


EOF

gnuplot ${File_Gnu}

# Tail tells to plot the last -n lines of the data. The simulations have a ntout=5, so each time interval between written points is 0.005.
# That is why we have (\$0*0.005) (each point is equal to 0.005).
