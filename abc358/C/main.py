import sys
sys.setrecursionlimit(999999999)
from itertools import chain,combinations
from collections import Counter

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def main():
    #N=int(input())
    N,M=map(int,input().split())
    
    #S=input().split()
    #A=list(map(int,input().split()))
    
    S=[]
    for _ in range(N):
        tmp=input()
        s_lst=[]
        for t in tmp:
            if t=="o":
                s_lst.append(1)
            else:
                s_lst.append(0)
        S.append(s_lst)

    itr=list(range(N))
    
    ps_lst=powerset(itr)

    for ps in ps_lst:
        ans=[0]*M
        for s in ps:
            v=int(s)
            for i in range(M):
                ans[i]+=S[v][i]

        if ans.count(0)==0:
            print(len(ps))
            break


    pass


if __name__ == "__main__":
    main()
