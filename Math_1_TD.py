# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:58:19 2020

@author: dulak
"""

import numpy as np
import copy

sigma = 1.5
beta = 0.95
alpha = 0.3
delta = 0.1
epsilon = 10**(-1)

K= np.linspace(0.005,5,1000)
V= np.linspace(0,0,200)
N = 1000

def u(c):
    utility = (c**(1-sigma)-1)/(1-sigma)
    return utility
    
def ct(i,j):
    kt1 = K[i]
    kt2 = K[j]
    ct1 = ((kt1**alpha)+(1-delta)*kt1-kt2)
    return ct1

def funct1(i,j,V):
    cons = ct(i,j)
    if cons >= 0 :
        return u(cons)+ beta*V[j]
    else: 
        return -np.Inf
    
def ulist(i,V):
    values = np.zeros(N)
    for j in range(N) :
            values[j] = funct1(i,j,V)
    return values

def funct2(i,V):
    valuemax = ulist(i,V)
    g = np.argmax(valuemax)
    v = valuemax[g]
    return v,g

def mainloop(K):
    V = np.zeros(N)
    TV = np.zeros(N)
    g = np.zeros(N)
    dist = 1
    while dist > epsilon :
        for i in range(N):
            TV[i],g[i] = funct2(i,V)
        dist = max(np.abs(TV-V))
        V = copy.deepcopy(TV)
        print(dist)
        
    return TV,g

V,g = mainloop(K)