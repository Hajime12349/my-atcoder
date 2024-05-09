import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    S=list(input())
    T=list(input())
    
    #A=list(map(int,input().split()))
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    


    count=0
    idx=0
    #print(list_s)
    end=len(S)
    ans=[]
    for t in T:
        count+=1
        #print(f'{S[idx]},{t}')
        if S[idx]==t:
            ans.append(count)
            idx+=1
            if idx>=end:
                break 
    
    print(*ans)

    
    pass


if __name__ == "__main__":
    main()
