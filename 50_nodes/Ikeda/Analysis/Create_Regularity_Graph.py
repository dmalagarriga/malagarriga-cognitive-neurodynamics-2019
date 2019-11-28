import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pylab
import os


initial_nodes=1

nodeListEXCA=[]

Colormap1=[]


path = os.getenv('P_Dir')

alpha=os.getenv('alpha')
beta=os.getenv('beta')
nNodes=int(os.getenv('Nodes'))
C1 = np.loadtxt('%s/List_Reg_not_sorted.dat' %path,unpack=True)


C1.view('f8,f8,f8').sort(order=['f0'], axis=-1) #Sort for colormapping

A=nx.path_graph(12)
G=nx.Graph()
G.add_nodes_from(A)
G.add_weighted_edges_from([(0,1,0.216),(0,3,0.216),(0,5,0.216),(0,7,0.216),(0,10,0.216),
(1,2,42.0),(3,4,172.0),(5,6,14.0),(7,8,29.0),(7,9,29.0),(10,11,45.0)])

for i in range(nNodes):
	
	nodeListEXCA.append(i)
	
	
	Colormap1.append(C1[2][i])


position={0: ([ 0.43224494,  0.45644897]), 1: ([ 0.19816788,  0.03833383]), 2: ([ 0.16721438,  -0.1        ]), 3: ([ -0.13149633,  0.35415439]), 4: ([ -0.5        ,  0.35790021]), 5: ([ 0.74438606,  0.93341973]), 6: ([ 0.98438582,  1.        ]), 7: ([ 0.09947127,  0.75868411]), 8: ([ -0.1677758,  0.76432184]), 9: ([ 0.22681519,  0.91381584]), 10: ([ 0.68950865,  0.06751937]), 11: ([ 0.71308757,  -0.12555264])}
nx.set_node_attributes(G,'pos',position)

node_color_EXCA = []



for i in range(len(nodeListEXCA)):
	node_color_EXCA.append(Colormap1[nodeListEXCA[i]])




nx.draw_networkx_nodes(G,pos=position, nodelist=nodeListEXCA, node_color=np.array(node_color_EXCA),node_size = 500,cmap=matplotlib.cm.gnuplot,label=nodeListEXCA)

nx.draw_networkx_edges(G,position)
nx.draw_networkx_labels(G,position)


cb=plt.colorbar(shrink=0.7)
cb.set_alpha(1)
cb.set_ticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
cb.set_ticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
for a in cb.ax.get_yticklabels():
	a.set_fontsize(20)
plt.clim([0.0,1.0])
cb.set_label('Reg',fontsize=20,labelpad=15)

ax1=plt.gca()
ax1.set_frame_on(False)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_xticklabels([])
#ax1.set_ytickslabels([])

pylab.savefig('%s/Colorgraph.eps' %(path))
pylab.close()

