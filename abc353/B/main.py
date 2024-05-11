import sys
sys.setrecursionlimit(999999999)


def main():
    N,K=map(int,input().split())
    #S=input().split()
    A=list(map(int,input().split()))
    
    k=K
    ans=1

    for a in A:
        if k<a:
            ans+=1
            k=K
            k-=a
        else:
            k-=a
        
    print(ans)
    
    pass


if __name__ == "__main__":
    main()
