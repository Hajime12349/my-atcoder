import sys
sys.setrecursionlimit(999999999)

N=int(input())
A=list(map(int,input().split()))

B=[0]*(N+1)

count=0
for a in A:
    #print(a)
    B[a]=count
    count+=1
#print(B)
ans = []
for i in range(N):
    if A[i] == i+1:
        continue
    idx = B[i+1]
    A[i],A[idx] = A[idx],A[i]
    B[i+1],B[A[idx]]=i,B[i+1]

    #print(B)
    ans.append((i+1,idx+1))
print(len(ans))
for a in ans:
    print(*a)

