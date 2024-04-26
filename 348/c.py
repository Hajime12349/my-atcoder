import sys
sys.setrecursionlimit(999999999)

N=int(input())
C_minA={}
L=[]
ans=0
for _ in range(N):
    L.append(list(map(int,input().split())))
    a,c=L[-1]
    if c in C_minA: 
        if C_minA[c]>a:
            C_minA[c]=a
            ans=min(ans,a)
    else:
        C_minA[c]=a

for l in L:
    a,c=l
    if a==C_minA[c]:
        ans=max(ans,a)

print(ans)

# ans_index=-1
# ans=0
# for l in L:
#     a,c=l
#     if not c in C_minA: 
#         C_minA[c]=a
#         ans=a

# print(ans)
    

