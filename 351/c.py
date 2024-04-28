import sys
sys.setrecursionlimit(999999999)

N=int(input())
#s=input().split()
A=list(map(int,input().split()))
# for _ in range(N):
#     a.append(list(map(int,input().split())))

S=[]

for n in range(N):
    S.append(A[n])
    while True:
        if len(S)<=1:
            break
        elif S[-1]==S[-2]:
            v=S.pop(-1)
            S[-1]+=1
        else:
            break
    #print(S)

#rint(S)
print(len(S))
