#!/usr/bin/python

import matplotlib
#matplotlib.use('Agg')
import networkx as nx
import matplotlib.pyplot as plt
import pylab
import os
import numpy as np
import community

File_Dat1="./Input/Kex.dat"
File_Dat2="./Input/Kin.dat"

#Which_network=str(os.getenv('Network'))
nNodes=int(os.getenv('Nodes'))
#initial_nodes=int(os.getenv('Initial_Nodes'))
#Seed=int(os.getenv('Seed'))

fout1=open(File_Dat1,'w')
fout2=open(File_Dat2,'w')

print >>fout1,nNodes
print >>fout2,nNodes

A=nx.path_graph(nNodes)
G=nx.Graph()
H=nx.Graph()
G.add_nodes_from(A)
H.add_nodes_from(A)

G.add_weighted_edges_from([(0,1,0.216),(0,3,0.216),(0,5,0.216),(0,7,0.216),(0,10,0.216),
(1,2,42.0),(3,4,172.0),(5,6,8.0),(7,8,29.0),(7,9,29.0),(10,11,45.0)])
H.add_weighted_edges_from([(0,1,0.216),(0,3,0.216),(0,5,0.216),(0,7,0.216),(0,10,0.216),
(1,2,30.0),(3,4,12.0),(5,6,17.0),(7,8,16.26),(7,9,16.26),(10,11,15.0)])

'''
G.add_weighted_edges_from([(0,1,0.216),(0,3,0.216),(0,5,0.216),(0,7,0.216),(0,10,0.216),
(1,2,24.0),(3,4,172.0),(5,6,14.0),(7,8,41.0*0.707),(7,9,41.0*0.707),(10,11,45.0)])
H.add_weighted_edges_from([(0,1,0.216),(0,3,0.216),(0,5,0.216),(0,7,0.216),(0,10,0.216),
(1,2,18.0),(3,4,12.0),(5,6,18.0),(7,8,24.0*0.707),(7,9,24.0*0.707),(10,11,15.0)])
'''

#for u,v,d in sorted(G.edges(data=True)): #u,v -> pairs, d=weight
#	d['weight']=1./np.sqrt(G.degree(u)*G.degree(v))
#	d['weight']=1./np.sqrt(H.degree(u)*H.degree(v))
np.savetxt(fout1,nx.adjacency_matrix(G),'%5.3f')
np.savetxt(fout2,nx.adjacency_matrix(H),'%5.3f')
partition = community.best_partition(G)

#print nx.adjacency_matrix(G)
#dendo = community.generate_dendogram(G)
#for level in range(len(dendo) - 1) :
#    print "partition at level", level, "is", community.partition_at_level(dendo, level)
#G = nx.erdos_renyi_graph(30, 0.5)

#drawing
size = float(len(set(partition.values())))
position = {0:  ([ 0.50788554,  0.53467435]), 1:  ([ 0.89932043,  0.16764832]), 2:  ([ 0.980826  ,  0.10493138]), 3:  ([ 0.82313434,  0.87589409]), 4:  ([ 0.87033908 ,  0.92522786]), 5:  ([ 0.08502763,  0.91967086]), 6:  ([ 0.02645139,  1.        ]), 7:  ([ 0.48393774,  0.15002812]), 8:  ([ 0.5314409 ,  0.00065677]), 9:  ([ 0.42192192,  0.03559108]), 10:  ([ 0.10033976,  0.10279914]), 11:  ([ 0.,  0.])}
nx.set_node_attributes(G,'pos',position)

count = 0.
for com in set(partition.values()) :
   	 count = count + 1.
   	 list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
   	 nx.draw_networkx_nodes(G, position, list_nodes, node_size = 200,node_color = str(count / size),cmap=matplotlib.cm.gnuplot,labels=None)
nx.draw_networkx_edges(G,position, alpha=0.5)
plt.savefig('./Input/Network_partitions.ps')
#plt.show()
	