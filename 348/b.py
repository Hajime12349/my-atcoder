import sys
import math
sys.setrecursionlimit(999999999)

N=int(input())
#s=input().split()
a=[]
ans=[]

for _ in range(N):
    a.append(list(map(int,input().split())))

for ai in a:
    aix,aiy=ai
    max_calc=0
    max_index=-1
    count=0
    for aj in a:
        ajx,ajy=aj
        #print(ai,aj)
        calc=math.sqrt(math.pow((aix-ajx),2)+math.pow((aiy-ajy),2))
        #print(calc,max_calc)
        if max_calc<calc:
            max_calc=calc
            max_index=count
        count+=1
    print(max_index+1)
