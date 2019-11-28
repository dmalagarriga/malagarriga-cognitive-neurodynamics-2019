#!/bin/bash 



File_Gnu="/tmp/Gnuplot.gnu"
File_Dat="$1"
File_Ps1="${File_Dat/.dat/_1.ps}"
File_Ps2="${File_Dat/.dat/_2.ps}"
File_Ps3="${File_Dat/.dat/_3.ps}"
File_Ps3="${File_Dat/.dat/_4.ps}"



cat > $File_Gnu << EOF
set term post color solid enhanced font "Helvetica,25" 
#set title "K = ${K_Conn}/nNodes" font "Helvetica,25"
set output "${File_Ps1}"
set xlabel 'Time (s)'
set ylabel 'y_1(t)-y_2(t) (mV)'

#set multiplot
#set origin 0.0,0.0
#set yrange[-3:15]
#plot for [i=2:26] "<tail -1000 ${File_Dat}" using (\$0*0.005):i w l notitle  
plot "<tail -1000 ${File_Dat}" using (\$0*0.005):2 w lp notitle pt 9 pointinterval 20 lc rgb "black" lw 3, "<tail -1000 ${File_Dat}" using (\$0*0.005):3 w lp pt 3 ps 0.5 pointinterval 10 lc rgb "#AA5500" lw 5.5 notitle, "<tail -1000 ${File_Dat}" using (\$0*0.005):4 w lp pt 5 ps 1.0 pointinterval 15 lc rgb "#AC2400" lw 4 notitle
#plot for [i in "17 19"] "<tail -1000 ${File_Dat}" using (\$0*0.005):i w l notitle lw 2

#set origin 0.09,0.12
#set size 0.5,0.3
#set xrange[10:20]
#set notitle
#set noxlabel 
#set noylabel 
#unset label
#set ytics 5.0 font "Helvetica,12"
#set xtics 5.0 font "Helvetica,12"
#plot for [i=2:26] "${File_Dat}" using (\$0*0.005):i notitle w l
#plot "${File_Dat}" using (\$0*0.005):2 notitle w l lc rgb "blue"
#plot for [i in "17 19"] "${File_Dat}" using (\$0*0.005):i w l notitle 
#set origin 0.46,0.12
#set size 0.5,0.3
#set xrange[40:50]
#set noxlabel 
#set noylabel 
#set notitle
#set nokey
#set noytics
#set ytics 5.0 font "Helvetica,12"
#set xtics 5.0 font "Helvetica,12"
#plot for [i=2:26] "${File_Dat}" using (\$0*0.005):i notitle w l
#plot "${File_Dat}" using (\$0*0.005):2 notitle w l lc rgb "blue"
#plot for [i in "17 19"] "${File_Dat}" using (\$0*0.005):i w l notitle
#set nomultiplot

#set term post color enhanced font "Helvetica,20" 
#set title "K = ${K_Conn}/nNodes" font "Helvetica,25"
#set output "${F1ile_Ps2}"
#set xrange[50:100]
#set xlabel 'Time (s)'
#set ylabel 'y_1-y_2 (mV)'
#plot "${File_Dat}" using (\$0*0.005):5 notitle w l lt 1 lc rgb "#aa0000"


#set term post color enhanced font "Helvetica,20" 
#set title "K = ${K_Conn}/nNodes" font "Helvetica,25"
#set output "${File_Ps3}"
#set xrange[250:300]
#set xlabel 'Time (s)'
#set ylabel 'y_1-y_2 (mV)'
#plot "${File_Dat}" using (\$0*0.005):5 notitle w l lt 1 lc rgb "#aa0000"

EOF

gnuplot ${File_Gnu}
