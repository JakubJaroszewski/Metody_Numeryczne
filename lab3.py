import numpy as np

AA=np.array([[9,8,-2,2,-2],[7,-3,-2,7,2],[2,-2,2,-7,6],[4,8,-3,3,-1],[2,2,-1,1,4.]])
b=np.array([21.,11,-4,16,9])
A=np.append(AA,b[:,None],axis=1)
nr,nc=A.shape
np.round(A,3)
np.linalg.solve(AA,b)
def gauss(A):
  n = nr
  for i in range(0,n):
    k=A[i,i]
    A[i,:]=A[i,:]/k
    for j in range(n):
      if(j!=i):
        A[j,:]-=A[i]*A[j,i]
  return A
def rozw(A):
  print("Rozwizania:")
  print(np.round(A[:, -1], 2))
A=gauss(A)
print("Macierz pocztkowa:",AA)
print("Macierz gaussa:")
print(A)
rozw(A)
b=np.array([[9,7,2,4,2],[17,4,0,12,4],[15,2,2,9,3],[17,9,-5,12,4],[15,11,1,11,8.]])
for i in range(5):
  D=np.append(AA,b[i][:,None],axis=1)
  print(np.matrix(gauss(D)))
  rozw(D)
