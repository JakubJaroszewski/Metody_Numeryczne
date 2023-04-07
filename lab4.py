import numpy as np

A=np.array([[1,2,-1],[1,4,5],[1,4,1.]])
def fun(A,i): # v wektor A macierz i koluma
    W,K=A.shape
    B=np.zeros((W,1))
    B[i]=1
    if(i==0):
        return A[:,i]+np.linalg.norm(A[:,i])*B.T
    elif(i==1):
        A[0,i]=0
        return A[:,i]+np.linalg.norm(A[:,i])*B.T
a1=[]
b1=[]
H=[]
for i in range(2):
    Va=fun(A,i)
    Vc=Va.T
    z=Va.shape
    a1.append(Vc@Va)
    b1.append(Va@Vc)
    H.append(np.identity(A.shape[0])-(2/b1[i])*a1[i])
np.set_printoptions(precision=3, suppress=True)
print("Macierz R obliczona teoretycznie")
print(H[1]@H[0]@A)
print("Macierz Q obliczona teoretycznie")
print(H[0]@H[1])
Q,R=np.linalg.qr(A)
print("Macierz R obliczona przez Pythona")
print(R)
print("Macierz Q obliczona przez Pythona")
print(Q)