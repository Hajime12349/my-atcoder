import sys
sys.setrecursionlimit(999999999)

N=int(input())
A=[]
B=[]
for _ in range(N):
    A.append(list(input()))
for _ in range(N):
    B.append(list(input()))

#print(type(A[0][1]))
for i in range(N):
    for j in range(N):
        #print(i,j)
        if not A[i][j]==B[i][j]:
            print(i+1,j+1)
            break


#a=list(map(int,input().split()))
# for _ in range(N):
#     a.append(list(map(int,input().split())))
