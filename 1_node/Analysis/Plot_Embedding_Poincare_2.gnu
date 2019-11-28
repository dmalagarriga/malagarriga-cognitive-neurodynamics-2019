#!/opt/local/bin/gnuplot -persist
#
#    
#    	G N U P L O T
#    	Version 5.0 patchlevel 0    last modified 2015-01-01 
#    
#    	Copyright (C) 1986-1993, 1998, 2004, 2007-2015
#    	Thomas Williams, Colin Kelley and many others
#    
#    	gnuplot home:     http://www.gnuplot.info
#    	faq, bugs, etc:   type "help FAQ"
#    	immediate help:   type "help"  (plot window: hit 'h')
 set terminal postscript eps enhanced defaultplex \
   leveldefault color colortext \
   dashlength 1.0 linewidth 1.0 butt noclip \
   nobackground \
   palfuncparam 2000,0.003 \
   "Helvetica" 25  fontscale 1.0 

unset clip points
set clip one
unset clip two
set bar 1.000000 front
set border 31 front lt black linewidth 1.000 dashtype solid
set zdata 
set ydata 
set xdata 
set y2data 
set x2data 
set boxwidth
set style fill  empty border
set style rectangle back fc  bgnd fillstyle   solid 1.00 border lt -1
set style circle radius graph 0.02, first 0.00000, 0.00000 
set style ellipse size graph 0.05, 0.03, first 0.00000 angle 0 units xy
set dummy u, v
set format x "% h" 
set format y "% h" 
set format x2 "% h" 
set format y2 "% h" 
set format z "% h" 
set format cb "% h" 
set format r "% h" 
set timefmt "%d/%m/%y,%H:%M"
set angles radians
unset grid
set raxis
set style parallel front  lt black linewidth 2.000 dashtype solid
set key title ""
set key inside right top vertical Right noreverse enhanced autotitle nobox
set key noinvert samplen 4 spacing 1 width 0 height 0 
set key maxcolumns 0 maxrows 0
set key noopaque
unset label
unset arrow
set style increment default
unset style line
unset style arrow
set style histogram clustered gap 2 title textcolor lt -1
unset object
set style textbox transparent margins  1.0,  1.0 border
unset logscale
set offsets 0, 0, 0, 0
set pointsize 1
set pointintervalbox 1
set encoding default
unset polar
set parametric
unset decimalsign
set view 60, 30, 1, 1
set samples 100, 100
set isosamples 100, 100
set surface 
unset contour
set cntrlabel  format '%8.3g' font '' start 5 interval 20
set mapping cartesian
set datafile separator whitespace
set hidden3d back offset 1 trianglepattern 3 undefined 1 altdiagonal bentover
set cntrparam order 4
set cntrparam linear
set cntrparam levels auto 5
set cntrparam points 5
set size ratio 0 1,1
set origin 0,0
set style data points
set style function lines
unset xzeroaxis
unset yzeroaxis
unset zzeroaxis
unset x2zeroaxis
unset y2zeroaxis
set ticslevel 0.5
set tics scale  1, 0.5, 1, 1, 1
set mxtics default
set mytics default
set mztics default
set mx2tics default
set my2tics default
set mcbtics default
set mrtics default
set xtics border in scale 1,0.5 mirror norotate  autojustify
set xtics autofreq  norangelimit
set ytics border in scale 1,0.5 mirror norotate  autojustify
set ytics autofreq  norangelimit
set ztics border in scale 1,0.5 nomirror norotate  autojustify
set ztics autofreq  norangelimit
unset x2tics
unset y2tics
set cbtics border in scale 1,0.5 mirror norotate  autojustify
set cbtics autofreq  norangelimit
set rtics axis in scale 1,0.5 nomirror norotate  autojustify
set rtics autofreq  norangelimit
unset paxis 1 tics
unset paxis 2 tics
unset paxis 3 tics
unset paxis 4 tics
unset paxis 5 tics
unset paxis 6 tics
unset paxis 7 tics
set title "" 
set title  font "" norotate
set timestamp bottom 
set timestamp "" 
set timestamp  font "" norotate
set rrange [ * : * ] noreverse nowriteback
set trange [ * : * ] noreverse nowriteback
set urange [ * : * ] noreverse nowriteback
set vrange [ * : * ] noreverse nowriteback
set xlabel "y(t-3{/Symbol t})" 
set xlabel  font "" textcolor lt -1 norotate
set x2label "" 
set x2label  font "" textcolor lt -1 norotate
set xrange [ * : * ] noreverse nowriteback
set x2range [ * : * ] noreverse nowriteback
set ylabel "y(t-2{/Symbol t})" 
set ylabel  font "" textcolor lt -1 rotate by -270
set y2label "" 
set y2label  font "" textcolor lt -1 rotate by -270
set yrange [ * : * ] noreverse nowriteback
set y2range [ * : * ] noreverse nowriteback
set zlabel "y(t-{/Symbol t})" 
set zlabel  font "" textcolor lt -1 norotate
set zrange [ * : * ] noreverse nowriteback
set cblabel "" 
set cblabel  font "" textcolor lt -1 rotate by -270
set cbrange [ * : * ] noreverse nowriteback
set paxis 1 range [ * : * ] noreverse nowriteback
set paxis 2 range [ * : * ] noreverse nowriteback
set paxis 3 range [ * : * ] noreverse nowriteback
set paxis 4 range [ * : * ] noreverse nowriteback
set paxis 5 range [ * : * ] noreverse nowriteback
set paxis 6 range [ * : * ] noreverse nowriteback
set paxis 7 range [ * : * ] noreverse nowriteback
set zero 1e-08
set lmargin  -1
set bmargin  -1
set rmargin  -1
set tmargin  -1
set locale "es_ES.UTF-8"
set pm3d explicit at s
set pm3d scansautomatic
set pm3d interpolate 1,1 flush begin noftriangles noborder corners2color mean
set palette positive nops_allcF maxcolors 0 gamma 1.5 color model RGB 
set palette rgbformulae 7, 5, 15
set colorbox default
set colorbox vertical origin screen 0.9, 0.2, 0 size screen 0.05, 0.6, 0 front bdefault
set style boxplot candles range  1.50 outliers pt 7 separation 1 labels auto unsorted
set loadpath 
set fontpath 
set psdir
set fit brief errorvariables nocovariancevariables errorscaling prescale nowrap v5
GNUTERM = "aqua"
ARGC = 0
ARG0 = ""
set ticslevel 0
set xtics 0,10,30
set ytics 0,10,30
set ztics 0,10,30
set zlabel offset 2,0
set xlabel offset .5,-.5
set xlabel "y(t-{/Symbol t})"
set ylabel "y(t-2{/Symbol t})"
set zlabel "y(t)"
#set output 'Embedding_Poincare_Henon_3.eps'
#set output 'Embedding_Poincare_Chen_3.eps'
set output 'Embedding_Poincare_Zaslavskii_3.eps'
#x = 0.0
#u = 0.0
#v = 0.0
## Last datafile plotted: "Output/1_variable/Henon/Output_0001/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat"
#splot [-5:25] [-5:25] [-5:25] "Output/1_variable/Henon/GOOD/Output_0001/Output_alpha_01.00/Output_beta_01.00/Emb_plot.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, u,8,v lc rgb 'gray' notitle, "Output/1_variable/Henon/Output_0001_1/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'green' ps 0.4 notitle
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Henon/Output_0001_1/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, [u = 0:5] u,8,v lc rgb 'gray' notitle, "Output/1_variable/Henon/Output_0001_1/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'green' ps 0.4 notitle
### HENON
# With the plane
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Henon/Output_0001_1/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, [u = 0:5] u,8,v lc rgb 'gray' notitle, "Output/1_variable/Henon/Output_0001_1/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'green' ps 0.4 notitle

# Without the plane
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Henon/Output_0001_1/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, "Output/1_variable/Henon/Output_0001_1/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'green' ps 0.4 notitle

### ZASLAVSKII
# With the plane
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Zavslaskii/Output_0001/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, [u = 0:5] u,8,v lc rgb 'gray' notitle, "Output/1_variable/Zavslaskii/Output_0001/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'blue' ps 0.4 notitle

# Without the plane
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Zavslaskii/Output_0001/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle,  "Output/1_variable/Zavslaskii/Output_0001/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'blue' ps 0.4 notitle

### IKEDA
# With the plane
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Ikeda/Output_0001/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, [u = 0:5] u,8,v lc rgb 'gray' notitle, "Output/1_variable/Ikeda/Output_0001/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'blue' ps 0.4 notitle

# Without the plane
splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Ikeda/Output_0001/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, "Output/1_variable/Ikeda/Output_0001/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'blue' ps 0.4 notitle

### Chen
# With the plane
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Chen/Output_0001/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle, [u = 0:5] u,8,v lc rgb 'gray' notitle, "Output/1_variable/Chen/Output_0001/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'red' ps 0.4 notitle

# Without the plane
#splot [-5:30] [-5:30] [-5:30] "Output/1_variable/Chen/Output_0001/Output_alpha_01.00/Output_beta_01.00/Emb_plot_Delay_10.00.dat" u 1:2:3 every :100:10000 w l lc rgb 'black' notitle,  "Output/1_variable/Chen/Output_0001/Output_alpha_01.00/Output_beta_01.00/Poincare_Section_tau_10_equal_08.00.dat" u 2:(8):3 w p pt 7 lc rgb 'red' ps 0.4 notitle

# plot "my.dat" every A:B:C:D:E:F

# A: line increment
# B: data block increment
# C: The first line
# D: The first data block
# E: The last line
# F: The last data block

#    EOF
