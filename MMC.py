def MMC(R,C):
    n=len(R)
    mmc=[[0] * n for _ in range(n)]

    for length in range(2,n+1):
        for r in range(n-length+1):
            c=r+length-1
            mmc[r][c]=float('inf')

            for k in range(r,c):
                cost=mmc[r][k]+mmc[k+1][c]+R[r]*C[k]*C[c]

            mmc[r][c]=min(mmc[r][c],cost)

    return(mmc[0][n-1])

n = int(input("Enter number of matrices: "))

print("Enter rows of all matrices:")
R = []
for i in range(n):
    R.append(int(input(f"R[{i}] = ")))

print("Enter columns of all matrices:")
C = []
for i in range(n):
    C.append(int(input(f"C[{i}] = ")))

answer = MMC(R, C)

print("\nMinimum multiplication cost =", answer)