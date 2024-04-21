import sys
sys.setrecursionlimit(999999999)

l,r=list(map(int,input().split()))

max_multi=60

ans_list=[]

for i in range(max_multi+1):
    j=0
    #multi=max_multi-i
    multi=i
    vi=pow(2,multi)
    
    while r>=vi:
        lv=vi*j
        rv=vi*j+1
        ans_tapple=(lv,rv)
        ans_list.append(ans_tapple)

        j+=1


