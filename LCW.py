def LCW(u,v):
    Lcw={}
    for r in range(len(u)+2):
        Lcw[r]={}
        for c in range(len(v)+2):
            Lcw[r][c]=0

    lcwmax=0

    for c in range(len(v)-1,-1,-1):
        for r in range(len(u)-1,-1,-1):
            if u[r] == v[c]:
                Lcw[r][c]=1+Lcw[r+1][c+1]
            else:
                Lcw[r][c]=0
            
            if lcwmax<Lcw[r][c]:
                lcwmax=Lcw[r][c]

    return lcwmax

u=(input("enter string 1 :"))
v=(input("enter string 2 :"))
print(LCW(u,v))