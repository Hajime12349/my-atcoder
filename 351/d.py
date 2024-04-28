import sys
sys.setrecursionlimit(999999999)

H,W=map(int,input().split())



#n=int(input())
#a=list(map(int,input().split()))
# for _ in range(N):
#     a.append(list(map(int,input().split())))

S=[]
for _ in range(H):
    S.append(list(input()))

A=[[0]*W for _ in range(H)]

ans=0


def Search(A,i,j):
    p=0
    A[i][j]=1

    if i+1>=H or i-1<0 or j+1>=W or i-1<0:
        return 0

    if S[i+1][j]=='#':
        return 1
    elif A[i+1][j]==0:
        p=max(p,Search(A,i+1,j))

    if S[i-1][j]=='#':
        return 1
    elif A[i-1][j]==0:
        p=max(p,Search(A,i-1,j))

    if S[i][j+1]=='#':
        return 1
    elif A[i][j+1]==0:
        p=max(p,Search(A,i,j+1))

    if S[i][j-1]=='#':
        return 1
    elif A[i][j-1]==0:
        p=max(p,Search(A,i,j-1))

    return p+1 #自分のいる位置＋

for i in range(H):
    for j in range(W):
        ans=Search(A,i,j)

print(ans)

