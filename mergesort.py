def merge(A,B):
    (C,M,N)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j<M+N:
        if i==M:
            C.append(B[j])
            j+=1
        elif j==N:
            C.append(A[i])
            i+=1
        elif A[i]<B[j]:
            C.append(A[i])
            i+=1
        elif A[i]>B[j]:
            C.append(B[j])
            j+=1
    return C

def mergesort(L):
    if len(L)<=1:
        return L
    mid=len(L)//2
    left=mergesort(L[:mid])
    right=mergesort(L[mid:])
    return merge(left,right)

import random

n=int(input("enter length of list :"))
L=random.sample(range(1,n+1),n)
print(mergesort(L))

