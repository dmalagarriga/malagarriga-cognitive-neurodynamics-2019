#!/bin/bash 



File_Gnu="/tmp/Gnuplot.gnu"
File_Dat="$1"
File_Ps1="${File_Dat/.dat/_phase_synchronization_GATE.ps}"

File_Ps5="${File_Dat/.dat/_XNOR_GATE.ps}"

cat > $File_Gnu << EOF
set term post color solid enhanced font "Helvetica,25" 
#set title "K = $K/nNodes" font "Helvetica,25"
set output "${File_Ps1}"
set xlabel 'Time (s)'
set ylabel 'y_1(t)-y_2(t) (mV)'
set xrange[1:21]
plot for [i in "7 8"] "${File_Dat}" using (\$0*0.005):i every ::6000::7000 w l notitle lw 2  
#plot "${File_Dat}" using (\$0*0.005):3 every ::6000::7000 w l notitle lw 2 lc rgb "#aa0000", "${File_Dat}" using (\$0*0.005):51 every ::6000::7000 w l notitle lw 2 lc rgb "#006400"

set term post color solid enhanced font "Helvetica,25" 
#set title "K = $K/nNodes" font "Helvetica,25"
set output "${File_Ps5}"
set xlabel 'Time (s)'
set ylabel 'y_1(t)-y_2(t) (mV)'
set xtics 0.5
set xrange[1:21]
#plot "<head -1000 ${File_Dat}" using (\$0*0.005):2 every ::20 notitle w l lt 1  linewidth 2 lc rgb "#aa0000","<head -1000 ${File_Dat}" using (\$0*0.005):3 every ::20 notitle w l lt 1 linewidth 2 lc rgb "#00aa00","<head -1000 ${File_Dat}" using (\$0*0.005):4 every ::20 notitle w l lt 1 linewidth 2 lc rgb "#0000aa","<head -1000 ${File_Dat}" using (\$0*0.005):5 every ::20 notitle w l lt 1 linewidth 2 lc rgb "orange","<head -1000 ${File_Dat}" using (\$0*0.005):6 every ::20 notitle w l lt 1 linewidth 2 lc rgb "brown","<head -1000 ${File_Dat}" using (\$0*0.005):7 every ::20 notitle w l lt 1 linewidth 2 lc rgb "yellow","<head -1000 ${File_Dat}" using (\$0*0.005):8 every ::20 notitle w l lt 1 linewidth 2 lc rgb "magenta","<head -1000 ${File_Dat}" using (\$0*0.005):9 every ::20 notitle w l lt 1 linewidth 2 lc rgb "gray","<head -1000 ${File_Dat}" using (\$0*0.005):10 every ::20 notitle w l lt 1 linewidth 2 lc rgb "black" 
plot for [i in "12 13"] "<tail -1000 ${File_Dat}" using (\$0*0.005):i w l notitle lw 2 
#plot "${File_Dat}" using (\$0*0.005):25 every ::6000::7000 w l notitle lw 2 lc rgb "#7FFF00", "${File_Dat}" using (\$0*0.005):19 every ::9000::10000 w l notitle lw 2 lc rgb "#006400"


EOF

gnuplot ${File_Gnu}

# Tail tells to plot the last -n lines of the data. The simulations have a ntout=5, so each time interval between written points is 0.005.
# That is why we have (\$0*0.005) (each point is equal to 0.005).
