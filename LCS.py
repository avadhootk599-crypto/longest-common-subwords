def LCS(u,v):
    Lcs={}
    for r in range(len(u)+1):
        Lcs[r]={}
        for c in range(len(v)+1):
            Lcs[r][c]=0
    lcsmax=0

    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r]==v[c]:
                Lcs[r][c]=1+Lcs[r+1][c+1]
            else:
                Lcs[r][c]=max(Lcs[r][c+1],Lcs[r+1][c])
            lcsmax=max(lcsmax,Lcs[r][c])

    return lcsmax

u=(input("enter string 1 :"))
v=(input("enter string 2 :"))
print(LCS(u,v))