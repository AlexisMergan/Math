# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math

#State Space X
K= np.linspace(0,5,1000)

#Initial value fct
V=np.linspace(0,0,1000)

#Starting Capital (in K) (Here K1=2.5)


#Parameter Values
sigma=1.5
beta=0.95
alpha=0.3
delta=0.1
epsilon=10**(-3)
#theta=float(input("give us the elsatticity of consumption:"))

#beta=float(input("give us the input for the discount rate:"))


#Include non-negativity constraint
def u(c):
    utility=(c**(1-sigma)-1)/(1-sigma)
    if c<0:
        return -math.exp(200)
    else:
        return utility

#delta= float(input("give us the detrition rate:"))
#alpha=float(input("give us the marginal return of capital:"))
        
    #i is the index for k1 / j for k2--> i tells us what the starting capital is equal to
def ct(i, j, K):
    kt1 = K[int(i)]
    kt2 = K[int(j)]
    thisct=((kt1**alpha)+(1-delta)*kt1-kt2)
    return thisct

#Check for k1=0.005 and k2=0.03
print(ct(1,6,K))
#Check for k1=2.5 and k2=5
#print(ct(500,999,K))
#print(ct(100,105,K))


cstr="Violation of Non-negativity Constraint"
#Objective Function - FCT1

def obj(i, j, K):
    cons = ct(i,j,K)
    if cons >=0:
        #############Need to define V properly
        return u(cons)+ beta*V[0]
    else: 
        return -math.exp(200)
    
#For k1_2 and k2_11 we find a negative Utility --> Still ok?:
print(obj(2,11,K))
#print(obj(500,999,K))


#Maximizing the Objective function

length=range(len(K))

 
def fct2(i,K):
    values_i=[]
    for j in length:
            values_i.append(float(obj(i,j,K)))
    return values_i


print("Function2")
print(fct2(2,K))
#print(max(fct2(i,K)))
def g(i):
    g=np.argmax(fct2(i,K))
    return g


    
#print(np.argmax(fct2(i,K))) 
f=[]
for i in length: 
    f.append(g(i))




def maximizer(i,K):
    v=max(fct2(i,K))
    return v 
####works until here. But need to define V properly 

def TV(i):
    i=i+1
    V[int(i)]=maximizer(i,K)
    return TV

V=[0]
TV_list=[]
for i in length:
    TV_list.append(float(maximizer(i,K)))
    V.append(float(maximizer(i,K)))
    
    
V=V[:1000]

TVdiff=[]

zip_object = zip(TV_list, V)
for i, j in zip_object:
    TVdiff.append(np.abs(i-j))
    
def maxdist(i):
    maxd=max(TVdiff)
    return maxd

for i in length:
    while epsilon < maxdist(i):
        v_i=maximizer(i,K)
        print ("|TV-V|="+ str((maxdist(i))))