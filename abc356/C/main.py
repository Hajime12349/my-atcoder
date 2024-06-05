import sys
import math
from itertools import chain,combinations
sys.setrecursionlimit(999999999)

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def main():
    #N=int(input())
    #S=input().split()
    #A=list(map(int,input().split()))
    N,M,K=map(int,input().split())
    
    I=[]
    data=[]
    for _ in range(M):
        I.append(list(input().split()))
        data=I[1:-1]
    

    comb_lst=list(combinations(range(1,N+1), K))
    ans_lst=[True]*len(comb_lst)
    #print(comb_lst)
    comb=int(math.factorial(N)/(math.factorial(K)*math.factorial(N-K)))
    
    ans_comb=[]
    for k in range(len(data)):
        original=range(1,N+1)
        if I[k+1][-1]=="x":
            for v in powerset(data[k]):
                ans_comb.append(list(map(int,list(v))))
        
        # if row[-1]=="x":
        #     for i in range(len(comb_lst)):
        #         isRemove=True
        #         for v in comb_lst[i]:
        #             if not str(v) in row[1:-1]:
        #                 #print(v,row[1:-1])
        #                 isRemove=False
                
        #         if isRemove:
        #             comb-=1
    
    print(ans_comb)
    tr_ans=[]
    for v_ans in ans_comb:
        if not v_ans in tr_ans:
            tr_ans.append(v_ans)
    
    comb=len(tr_ans)



    print(comb)

    pass


if __name__ == "__main__":
    main()
