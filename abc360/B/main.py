import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    S,T=input().split()
    #A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    
    I=int(len(S)/len(T))
    last_ans=""

    
    #print(i,int(len(S)/i),len(T))
    
    for i in range(1,101):
        ans=False
        if i<len(S):
            a=[]
            a.append([])
            idx=0
            for s in S:
                a[-1].append(s)
                if (idx+1)%i==0:
                    a.append([])
                idx+=1
            if len(a[-1])==0:
                a.pop(-1)
            #print(a)
            if len(a)==len(T) or len(a)==len(T)+1:
                for m in range(i):
                    ans_str=""
                    for l in range(len(T)):
                        if len(a[l])>m:
                            ans_str+=a[l][m]
                            #print(T[l],a[l][m])
                        #     if T[l]!=a[l][m]:
                        #         ans=False
                        #         break
                        #     else:
                        #         ans=True
                        #         print(a,T[l],a[l][m],l,m)
                        # # if len(a)!=i:
                        #     continueaa
                    
                    #print(a,ans_str)
                    if T==ans_str:
                        ans=True
                        #print(a,ans_str)
                        #print(a,i)
                        break
                
        if ans:
            last_ans="Yes"
            #print(a)
            break
        else:
            last_ans="No"
    else:
        last_ans="No"
    
    print(last_ans)



if __name__ == "__main__":
    main()
