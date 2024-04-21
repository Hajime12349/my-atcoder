import sys
sys.setrecursionlimit(999999999)

N,Q=map(int,input().split())
T=list(map(int,input().split()))

l=[True]*N

for t in T:
    l[t-1]=not l[t-1]

count=0
for li in l:
    if li:
        count+=1

print(count)
