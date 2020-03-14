import numpy as np
import math

#Parameter Values
sigma=1.5
beta=0.95
alpha=0.3
delta=0.1
epsilon=10**(-3)


K= np.linspace(0.01,5,1000)
V= np.linspace(0,0,1000)


def u(c):
    utility=((c**(1-sigma))-1)/(1-sigma)
    if c<=0:return -math.exp(200)
    else:
        return utility
    
def ct(i, j, K):
    kt1 = K[i]
    kt2 = K[j]
    ct1=((kt1**alpha)+(1-delta)*kt1-kt2)
    return ct1

def funct1(i,j,K,V):
    cons = ct(i,j,K)
    if cons >=0:
        return u(cons)+ beta*V[i]
    else: 
        return -math.exp(200)
#print(funct1(2,0,K,V))
#print(funct1(500,0,K,V))
#print(funct1(999,0,K,V))
#print(funct1(999,400,K,V))

length=range(len(K))
    
def maxlist(i,K):
    values_i=[]
    for j in length:
            values_i.append(float(funct1(i,j,K,V)))
    return values_i
#print(maxlist(2,K))

def funct2(i,K):
    v=max(maxlist(i,K))
    return v
#print(funct2(2,K))
#print(funct2(999,K))
#print(funct2(500,K))

dist = 100
while dist > epsilon:
    TV = []
    diff = []
    for i in length:
        TV.append(funct2(i,K))
        diff.append(TV[i]-V[i])
    dist=max(np.abs(diff))
    V=TV
    print(dist)
    
print(V)
