import matplotlib.pyplot as plt
import numpy as np


x=[]

def f(x):
    return x**3-2*x**2+2
def FindRoots(a,b,e,krok):
    if(f(a)*f(b) < 0):
        x0=a+(b-a)/2
        krok+=1
        if abs(f(x0))<e:
            print('pierwiastek:',x0)
            print(krok)
            x.append(krok)
        elif f(x0)*f(a) > 0 :
            FindRoots(x0,b,e,krok)
        elif f(x0)*f(b) > 0 :
            FindRoots(a,x0,e,krok)
    else:
        print('W przedziale nie ma pierwistka')
a = -2
b = 2
krok=0
ep=(10**(-np.arange(2.0,20.0,1.0)))
for i in range(18):
    FindRoots(a,b,ep[i],krok)
def k(a,b,ep):
    return np.log2((b-a)/ep)

plt.semilogx(ep, k(a,b,ep),marker = ".")
plt.semilogx(ep, x,marker = ".")
plt.show()