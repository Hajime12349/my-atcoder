import sys
sys.setrecursionlimit(999999999)


def main():
    #N=int(input())
    #S=input().split()
    N,L,R=map(int,input().split())
    
    N+=1
    ans=[]
    for i in range(1,N):
        if i<L:
            ans.append(i)
        else:
            tmp=[]
            for j in range(i,N):
                if j<=R:
                    tmp.append(j)
                else:
                    break
            #print(tmp)
            for j in range(len(tmp)):
                ans.append(tmp[len(tmp)-j-1])
            
            break
    for i in range(R+1,N):
        ans.append(i)
    
    print(*ans)    
    
    #A=[]
    #for _ in range(N):
    #    A.append(list(map(int,input().split())))
    pass


if __name__ == "__main__":
    main()
