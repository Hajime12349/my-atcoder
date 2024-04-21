import sys
sys.setrecursionlimit(999999999)

s=input()

d={}

v={}

ans=True

for c in s:
    if c in d:
        d[c]+=1
    else:
        d[c]=1

for dv in d.values():
    #print(dv)
    sdv=str(dv)
    if sdv in v:
        v[sdv]+=1
    else:
        v[sdv]=1
    
for vi in v.values():
    #print(vi)
    if vi!=2:
        ans=False

if ans:
    print("Yes")
else:
    print("No")
