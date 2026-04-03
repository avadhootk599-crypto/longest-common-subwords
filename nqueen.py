board={}
def initialize(n):
    board.clear()
    board['queen']={i:-1 for i in range(n)}
    board['rows']={i:0 for i in range(n)}
    board['col']={i:0 for i in range(n)}
    board['swtone']={i:0 for i in range(2*n-1)}
    board['nwtose']={i:0 for i in range(-(n-1),n)}

def printboard():
    for r in range(len(board['queen'])):
        print((r,board['queen'][r]))

def free(i,j):
    return(board['rows'][i]==0 and board['col'][j]==0 and board['swtone'][i+j]==0 and board['nwtose'][j-i]==0)

def add(i,j):
    board['queen'][i]=j
    board['rows'][i]=1
    board['col'][j]=1
    board['swtone'][i+j]=1
    board['nwtose'][j-i]=1

def remove(i,j):
    board['queen'][i]=-1
    board['rows'][i]=0
    board['col'][j]=0
    board['swtone'][i+j]=0
    board['nwtose'][j-i]=0

def placequeen(i):
    n=len(board['queen'])
    for j in range(n):
        if free(i,j):
            add(i,j)
            if i == n-1:
                return True
            if placequeen(i+1):
                return True
            remove(i,j)
    return False

n = int(input("Enter board size: "))
initialize(n)

if placequeen(0):
    printboard()
else:
    print("No solution")