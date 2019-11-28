from math import log
log2= lambda x:log(x,2)
from scipy import histogram, digitize, stats, mean, std
from collections import defaultdict
import numpy
from pylab import *
from numpy import *
from scipy import *
from scipy.stats import mode
from scipy.misc.common import factorial
from scipy.spatial.distance import correlation,euclidean
 
def mutual_information(x,y):
    return entropy(y) - conditional_entropy(x,y)
 
def conditional_entropy(x, y):
    """
    x: vector de numeros reales
    y: vector de numeros enteros
 
    devuelve H(Y|X)
    """
    # discretizacion de X 
    hx, bx= histogram(x, bins=x.size/10, density=True)
 
    Py= compute_distribution(y)
    Px= compute_distribution(digitize(x,bx))
 
    res= 0
    for ey in set(y):
        # P(X | Y)
        x1= x[y==ey]
        condPxy= compute_distribution(digitize(x1,bx))
 
        for k, v in condPxy.iteritems():
            res+= (v*Py[ey]*(log2(Px[k]) - log2(v*Py[ey])))
    return res
        
def entropy(y):
    """
    Computa la entropia de un vector discreto
    """
    # P(Y)
    Py= compute_distribution(y)
    res=0.0
    for k, v in Py.iteritems():
        res+=v*log2(v)
    return -res
 
def compute_distribution(v):
    """
    v: vector de valores enteros
 
    devuelve un diccionario con la probabilidad de cada valor
    computado como la frecuencia de ocurrencia
    """
    d= defaultdict(int)
    for e in v: d[e]+=1
    s= float(sum(d.values()))
    return dict((k, v/s) for k, v in d.items())
    
#Mutual information
'''
Definition:

                                        p(x,y)
    I(X;Y) = sum     sum    p(x,y) log --------
            x in X  y in Y             p(x)p(y)

'''


def log2(n):  return log(n)*1.0/log(2)
def log10(n):  return log(n)*1.0/log(10)

def mutual_info(x,y):
    N=double(x.size)
    I=0.0
    eps = numpy.finfo(float).eps
    for l1 in unique(x):
        for l2 in unique(y):
            #Find the intersections
            l1_ids=nonzero(x==l1)[0]
            l2_ids=nonzero(y==l2)[0]
            pxy=(double(intersect1d(l1_ids,l2_ids).size)/N)+eps
            I+=pxy*log2(pxy/((l1_ids.size/N)*(l2_ids.size/N)))
    return I

    
#Normalized mutual information
def nmi(x,y):
    N=x.size
    I=mutual_info(x,y)
    Hx=0
    for l1 in unique(x):
        l1_count=nonzero(x==l1)[0].size
        Hx+=-(double(l1_count)/N)*log2(double(l1_count)/N)
    Hy=0
    for l2 in unique(y):
        l2_count=nonzero(y==l2)[0].size
        Hy+=-(double(l2_count)/N)*log2(double(l2_count)/N)
    return I/((Hx+Hy)/2)