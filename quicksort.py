def quicksort(L):
    if len(L)<=1:
        return L 
    pivot=L[0]
    left=[]
    right=[]

    for i in range(1,len(L)):
        if L[i]<=pivot:
            left.append(L[i])
        else:
            right.append(L[i])
    
    return (quicksort(left)+[pivot]+quicksort(right))

import random

n=int(input("enter length of list :"))
L=random.sample(range(1,n+1),n)
print(quicksort(L))