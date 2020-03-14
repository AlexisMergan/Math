#definition of parameters
sig=1.5
print(sig)
delt=0.1
beta=0.95
alpha=0.3
n_inf=float("-inf")

#threshold for convergence
eps=0.0001

#grid size
N=1000

#state space
def capital_grid(x,y,n):
    h=(y-x)/n
    K=[]
    j=x
    while j<=y:
        K.append(j)
        j+=h
    return(K)

def capital_grid_round(x,y,n):
    h=(y-x)/n
    K=[]
    j=x
    while j<=y:
        r=round(j, 4)
        K.append(r)
        j+=h
    return(K)

K=capital_grid_round(0,5,1000)


#utility function
def u(c):
    if c==0: u=n_inf
    else: u=((c**(1-sig))-1)/(1-sig)
    return(u)


#constraint set
def upperbound(k):
    b=(k**alpha)+((1-delt)*k)
    return(b)


#remark: to get the first element of a list, use index 0!
v=[1,2,3,5]
print(v[0])
print(v[3])#last element of the list in this case


#F function, depending on current capital stock K[i], next capital stock K[j]
#and value function (in vector/list form) V
#The constraint set (correspondence gamma) is also taken into account.
def F(i,j,V,K):
    if K[j-1]<0 or K[j-1]>upperbound(K[i-1]):
        return("constraint not satisfied")
    else:
        cons=(K[i-1]**alpha)+((1-delt)*K[i-1])-K[j-1]
        return(u(cons)+(beta*V[j-1]))
    


#maximum function:
def max(liste):
    a=liste[0]
    x=1
    while x<len(liste):
        if liste[x]>a:
            a=liste[x]
        x+=1
    return(a)

#remark: e.g. range(6) is not the values of 0 to 6, but the values 0 to 5
for i in range(6): print(i)
M=[]
for p in range(6): M.append(p)
print(M)


#Bellman operator, to get (TV)(K[i]) (or (TV)[K[i-1]), because of the notation
#in python)
def T(i,V,K):
    Val=[]
    for p in range(N):
        j=p+1
        if F(i,j,V,K)=="constraint not satisfied":
            Val.append(n_inf)
        else:
            Val.append(F(i,j,V,K))
    TVi=max(Val)
    if TVi<-10000000000000000000000:
        for p in range(N):
            if F(i,p+1,V,K)!="constraint not satisfied" and F(i,p+1,V,K) <-100000000000000:
                argmax_index=p+1
    else:
        for p in range(N):
            if Val[p]==TVi:
                argmax_index=p+1
    return(TVi,argmax_index)
#Thuse, if there is only one capital stock that satisfies the constraint, but this capital stock is 0 so it gives consumption=0, then TVi will be
#equal to -inf in any case. The argmax_index on the other hand will be the index which corresponds to the 0 capital stock (i.e. the capital stock
#that satisfies the constraint).


#Norm of a function, which is defined as the maximum value the function takes
#on its domain (with the domain being in this case a discrete set, i.e. a set or
#list or vector of N (or another number of) values):
def abs(x):
    if x>=0:
        return x
    else:
        return -x
print(abs(20))
print(abs(-20))

import math
x = float('nan')
print(math.isnan(x))

def norm(v):
    w=[]
    for i in range(len(v)):
        if math.isnan(v[i])==True:
            w.append(n_inf)
        else:
            w.append(abs(v[i]))
    return max(w)
print(norm([1,4,3,-5,2]))
print(norm([n_inf-n_inf]))
#In the case where V[i] is -inf for all capital stocks (for all indices j from 1 to N), then TV[i] will also be -inf.
#And in that case, (TV[i]-V[i]) will be -inf - (-inf), which is undetermined (or 'nan'). To account for this when computing the norm of TV-V,
#we take -inf instead of the absolute value of the difference when the difference is undetermined, so that this element i will never be a
#maximum of the absolute values of the elements in the vector TV-V.


#function that returns the (approximate) fixed point of the Bellman operator
#(as well as the list of optimal next capital stock indices),
#with the approximation based on a given grid of capital values K and an
#initial value function Vinit;
#and where eps is used as a distance threshold:

#For the following definition I take 90 instead of eps, just so that the result
#comes faster for the example below.
def FixP_1(K,Vinit):
    dist=100
    V=Vinit
    while dist>=0.01:
        TV=[]
        diff=[]
        g=[]
        for i in range(N):
            g.append(1)
        for i in range(N):
            TV.append(T(i+1,V,K)[0])
            diff.append(TV[i]-V[i])
            g[i]=T(i+1,V,K)[1]
        dist=norm(diff)
        V=TV
    return(V, dist, g)

#check for initial zero function (zero vector Vinit):
Vinit1=[]
for i in range(N):
    Vinit1.append(0)
print(FixP_1(K,Vinit1))
